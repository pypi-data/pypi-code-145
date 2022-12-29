#  SPDX-FileCopyrightText: © 2022 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import asyncio
import contextlib
import inspect
import traceback
import os
import klovve.application
import klovve.drivers.gtk
import klovve.pieces.window


class View(klovve.pieces.window.View, klovve.drivers.gtk.View):

    def get_native(self, model, model_bind):
        gtk = klovve.drivers.gtk.Gtk
        gdk = klovve.drivers.gtk.Gdk
        window = self.gtk_new(klovve.drivers.gtk.Gtk.Window, title=model_bind(twoway=False).title)  # TODO gtk main window / appl. wnd.?
        css_provider = gtk.CssProvider()
        css_provider.load_from_path(f"{os.path.dirname(__file__)}/-data/main.css")
        gtk.StyleContext.add_provider_for_display(gdk.Display.get_default(), css_provider,
                                                  gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

        async def do():
            do_close = klovve.application.call_with_kwargs_maybe_async(
                model.close_func or (lambda context: True), asyncio.get_running_loop(),
                context=Context(self._view_factory, window)
            )
            if inspect.isawaitable(do_close):  # TODO
                do_close = await do_close
            if do_close:
              #TODO needed?  for foo in klovve.drivers.gtk.children(window):
               #     window.remove(foo)
                model.is_closed = True
                window.destroy()

        window.connect("close-request", lambda *_: klovve.drivers.gtk.GLib.idle_add(
            lambda: klovve.application.call_with_kwargs_maybe_async(
                do, asyncio.get_running_loop()
            ) and False# TODO needed for idle_add
        ) or True)

        @klovve.reaction(owner=window)
        def set_body():
            window.set_child(model.body.view().get_native_stuff())

        return window


class Context:  # TODO  dedup (button)

    def __init__(self, fabric, main_window):
        self.__fabric = fabric
        self.__main_window = main_window

    @contextlib.asynccontextmanager
    async def error_message_for_exceptions(self, *exception_types):
        try:
            yield
        except Exception as ex:
            if isinstance(ex, exception_types):
                await self.dialog(self.__fabric.interact.message(message=str(ex)))
                traceback.print_exc()#TODO weg
            else:
                raise ex

    async def dialog(self, view):
        view = view.view()
        gtk = klovve.drivers.gtk.Gtk
        dialog = gtk.Window(transient_for=self.__main_window, modal=True)
        dialog.append(view.get_native_stuff())
        done_future = asyncio.Future()
        @klovve.reaction(owner=None)
        def _wf():
            nonlocal done_future
            if view._model.is_answered:
                done_future.set_result(None)
                dialog.destroy()
        dialog.show()
        await done_future
        return view._model.answer

    @property
    def fabric(self):
        return self.__fabric
