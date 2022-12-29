#  SPDX-FileCopyrightText: © 2022 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import klovve.pieces.dropdown
import klovve.drivers.curses

import viwid.widgets.dropdown

"""
class PopUpDialog(urwid.WidgetWrap):

    def __init__(self, model):
        lw = urwid.SimpleFocusListWalker([])
        libo = self.ListBox(lw)
        for item in model.items:
            bn = urwid.Button((model.item_label_func or str)(item))
            lw.append(bn)
        self.__super.__init__( urwid.Filler( libo))


class ThingWithAPopUp(urwid.PopUpLauncher):

    def __init__(self, model):
        self.__btn = self.Button("")
        self.__super.__init__(self.__btn)
        self.__model = model
        urwid.connect_signal(self.original_widget, 'click', lambda button: self.open_pop_up())

    def set_label(self, s):
        self.__btn.set_label(s)

    def create_pop_up(self):
        pop_up = PopUpDialog(self.__model)
        #urwid.connect_signal(pop_up, 'close', lambda button: self.close_pop_up())
        return pop_up

    def get_pop_up_parameters(self):
        return {'left':0, 'top':1, 'overlay_width':32, 'overlay_height':7}

"""
class View(klovve.pieces.dropdown.View, klovve.drivers.curses.View):

    def get_native(self, model, model_bind):

        btn = viwid.widgets.dropdown.DropDown()

        @klovve.reaction(owner=btn)
        def _handle_selection():
           # if model.selected_item is not None:  # TODO pass
                btn.selected_index = model.items.index(model.selected_item) if model.selected_item is not None else None
          #  else:
            #    btn.selected_index = None

        @klovve.reaction(owner=btn)
        def _handle_items():
            btn.items = [(model.item_label_func or str)(item) for item in model.items]

        def mkclick(ite):
            def f(_):
                model.selected_item = ite
                uloop.widget = ulooporigwidget
            return f

        def drodo():
            lw = urwid.SimpleFocusListWalker([])
            libo = self.ListBox(lw)
            for item in model.items:
                bn = urwid.Button((model.item_label_func or str)(item))
                urwid.connect_signal(bn, "click", mkclick(item))
                lw.append(bn)

            uloop.widget = urwid.Overlay(
                libo, uloop.widget,
                align=("relative", 50),
                valign=("relative", 50),
                width=("relative", 98),
                height=("relative", 60)
            )

        #btn.on_click.append(drodo)

        def sei():
            model.selected_item = model.items[btn.selected_index] if btn.selected_index is not None else None

        btn.listen_property("selected_index", sei)

        return btn

        return urwid.Text("TODO")

        gtk = klovve.drivers.gtk.Gtk
        tree_store = gtk.TreeStore(str)
        combo_box = self.gtk_new(gtk.ComboBox, hexpand=True, halign=gtk.Align.CENTER, model=tree_store)
        cell_renderer = gtk.CellRendererText(text=0)
        combo_box.pack_start(cell_renderer, True)
        combo_box.add_attribute(cell_renderer, 'text', 0)

        def foo(w):
            x = None
            idx = combo_box.get_active()
            if idx >= 0:
                x = idx
            model.selected_item = model.items[x] if (x is not None) else None
        combo_box.connect("changed", foo)

        _refs = []  # TODO

      #  @klovve.reaction(owner=tree_store)
        def _handle_items():
            selected_item = model.selected_item
            #for olditem in self.combo_box.get_children():
            #    self.combo_box.remove(olditem)
            item_label_func = (model.item_label_func or str)
            select_row = None
            _refs.clear()
            def bla(ll, itm):
                @klovve.reaction(owner=None)
                def flg():
                    vv = item_label_func(itm)
                    ll.props.label = vv
                return flg
            for i, item in enumerate(model.items):
                row = gtk.Label(xalign=0, visible=True)
                _refs.append(row)
                _refs.append(bla(row, item))
                combo_box.append(row)
                if item == selected_item:
                    select_row = i
            combo_box.select_row(None if (select_row is None) else combo_box.get_row_at_index(select_row))
            if select_row is None:
                foo(None, None)

   #     @klovve.reaction(owner=tree_store)
        def _handle_selection():
            selected_item = model.selected_item
            select_row = -1
            for i, item in enumerate(model.items):
                if item == selected_item:
                    select_row = i
                    break
            combo_box.set_active(select_row)
            if select_row is None:
                foo(None)

        item_label_func = (model.item_label_func or str)

        class ItemsObserver(klovve.ListObserver):

            def item_added(self, index, item):
                newitemiter = tree_store.insert(None, index, [""])

                #@klovve.reaction(owner=item)
                def _item_message():
                    tree_store.set_value(newitemiter, 0, item_label_func(item))
                _item_message()

            def item_removed(self, index):
                tree_store.remove(tree_store.iter_nth_child(None, index))

            def item_moved(self, from_index, to_index):
                print("TODO rca", from_index, to_index)

        klovve.data.model.observe_list(model, "items", ItemsObserver())

        return combo_box
