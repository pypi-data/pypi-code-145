#  SPDX-FileCopyrightText: © 2022 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import klovve.drivers.gtk
import klovve.pieces.property_panel


class View(klovve.pieces.property_panel.View, klovve.drivers.gtk.View):

    def get_native(self, model, model_bind):
        widget = self.gtk_new(klovve.drivers.gtk.Gtk.Grid)
        values = model.values # TODO
        goof = []

        class ItemsObserver(klovve.ListObserver):  # TODO dedup

            def item_added(self, index, item):
                widget.insert_row(index)
                vv = values[item.name] = values.get(item.name, "")
                goof.insert(index, item)
                widget.attach(klovve.drivers.gtk.Gtk.Label(label=item.label or item.name), 0, index, 1, 1)
                widget.attach(ee := klovve.drivers.gtk.Gtk.Entry(text=vv), 1, index, 1, 1)
                def sdf(_, __):
                    values[item.name] = ee.get_text()
                ee.connect("notify::text", sdf)

            def item_removed(self, index):
                widget.remove_row(index)
                gof = goof.pop(index)
                values.pop(gof.name)

            def item_moved(self, from_index, to_index):
                ol = widget.get_child_at(from_index, 0)
                oc = widget.get_child_at(from_index, 1)
                widget.remove_row(from_index)
                widget.insert_row(to_index)
                widget.attach(ol, 0, to_index, 1, 1)
                widget.attach(oc, 1, to_index, 1, 1)
                goof.insert(to_index, goof.pop(from_index))

        klovve.data.model.observe_list(model, "entries", ItemsObserver())

        return widget
