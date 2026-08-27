package com.example.drivelint.sample

import androidx.car.app.model.LongMessageTemplate

class LongMessageEmptyScreen {
    fun buildTemplate(): LongMessageTemplate {
        return LongMessageTemplate.Builder("")
            .setTitle("이용약관")
            .build()
    }
}
