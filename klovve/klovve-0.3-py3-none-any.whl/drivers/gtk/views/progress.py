#  SPDX-FileCopyrightText: © 2021 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import klovve.pieces.progress
import klovve.drivers.gtk


class View(klovve.pieces.progress.View, klovve.drivers.gtk.View):

    def get_native(self, model, model_bind):
        return self.gtk_new(klovve.drivers.gtk.Gtk.ProgressBar, fraction=model_bind.value)
