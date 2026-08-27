package com.example.drivelint.sample

import androidx.car.app.model.Tab
import androidx.car.app.model.TabTemplate

class TabPassScreen {
    fun buildTemplate(): TabTemplate {
        return TabTemplate.Builder(tabContents)
            .addTab(Tab.Builder().setTitle("홈").build())
            .addTab(Tab.Builder().setTitle("즐겨찾기").build())
            .addTab(Tab.Builder().setTitle("최근").build())
            .build()
    }
}
