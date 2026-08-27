package com.example.drivelint.sample

import androidx.car.app.model.Pane
import androidx.car.app.model.PaneTemplate
import androidx.car.app.model.Row

class PaneTooManyRowsScreen {
    fun buildTemplate(): PaneTemplate {
        val pane = Pane.Builder()
            .addRow(Row.Builder().setTitle("속도").build())
            .addRow(Row.Builder().setTitle("거리").build())
            .addRow(Row.Builder().setTitle("도착 예정 시간").build())
            .addRow(Row.Builder().setTitle("남은 연료").build())
            .addRow(Row.Builder().setTitle("현재 기어").build())
            .build()

        return PaneTemplate.Builder(pane)
            .setTitle("주행 정보")
            .build()
    }
}
