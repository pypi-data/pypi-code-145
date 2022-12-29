#  SPDX-FileCopyrightText: © 2022 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import sys

import klovve.drivers.curses
import klovve.pieces.horizontal_box
import viwid.widgets.box


class View(klovve.drivers.curses.View):

    def _orientation(self):
        raise NotImplementedError()

    def get_native(self, model, model_bind):
        box = viwid.widgets.box.Box(orientation=viwid.widgets.box.Orientation.HORIZONTAL if (self._orientation()==1) else viwid.widgets.box.Orientation.VERTICAL)

        self_ = self
        class ItemsObserver(klovve.ListObserver):

            def item_added(self, index, item):
                st = item.view().get_native_stuff()
                box.children.insert(index, st)

            def item_removed(self, index):
                box.children.pop(index)

            def item_moved(self, from_index, to_index):
                box.children.insert(to_index, box.widget_list.pop(from_index))

        klovve.data.model.observe_list(model, "items", ItemsObserver())
        return box
