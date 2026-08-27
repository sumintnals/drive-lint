package com.example.drivelint.sample

import androidx.car.app.model.Pane
import androidx.car.app.model.PaneTemplate
import androidx.car.app.model.Row

class PanePassScreen {
    fun buildTemplate(): PaneTemplate {
        val pane = Pane.Builder()
            .addRow(Row.Builder().setTitle("속도").build())
            .addRow(Row.Builder().setTitle("거리").build())
            .addRow(Row.Builder().setTitle("도착 예정 시간").build())
            .build()

        return PaneTemplate.Builder(pane)
            .setTitle("주행 정보")
            .build()
    }
}
