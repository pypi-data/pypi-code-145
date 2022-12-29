#  SPDX-FileCopyrightText: © 2021 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import klovve.pieces.form
import klovve.drivers.curses

import viwid.widgets.box

class View(klovve.pieces.form.View, klovve.drivers.curses.View):

    def get_native(self, model, model_bind):
        box = viwid.widgets.box.Box(orientation=viwid.widgets.box.Orientation.VERTICAL,
                                    horizontal_expand_greedily=True,
                                    vertical_expand_greedily=True,
                                    )

        class ItemsObserver(klovve.ListObserver):

            def item_added(self, index, item):
                item_widget = item.view().get_native_stuff()
                box.children.insert(index, item_widget)
                box.children = box.children

            def item_removed(self, index):
                box.children.pop(index)
                box.children = box.children

            def item_moved(self, from_index, to_index):
                box.children.insert(to_index, box.widget_list.pop(from_index))
                box.children = box.children

        klovve.data.model.observe_list(model, "items", ItemsObserver())
        return box
