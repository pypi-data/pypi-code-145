#  SPDX-FileCopyrightText: © 2022 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import sys
import klovve.pieces.label


class View(klovve.pieces.label.View, klovve.BaseView):

    def get_native(self, model, model_bind):
        class AA:pass
        result = AA()

        @klovve.reaction(owner=result)
        def _item_message():
            print(model.text, file=sys.stderr)
                
        return result
