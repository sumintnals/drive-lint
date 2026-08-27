package com.example.drivelint.sample

import androidx.car.app.model.MessageTemplate

class MessageEmptyScreen {
    fun buildTemplate(): MessageTemplate {
        return MessageTemplate.Builder("")
            .setTitle("안내")
            .build()
    }
}
