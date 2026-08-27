package com.example.drivelint.sample

import androidx.car.app.model.Tab
import androidx.car.app.model.TabTemplate

class TabTooFewScreen {
    fun buildTemplate(): TabTemplate {
        return TabTemplate.Builder(tabContents)
            .addTab(Tab.Builder().setTitle("홈").build())
            .build()
    }
}
