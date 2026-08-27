package com.example.drivelint.sample

import androidx.car.app.model.Pane
import androidx.car.app.model.PaneTemplate

class PaneEmptyScreen {
    fun buildTemplate(): PaneTemplate {
        val pane = Pane.Builder().build()

        return PaneTemplate.Builder(pane)
            .setTitle("주행 정보")
            .build()
    }
}
