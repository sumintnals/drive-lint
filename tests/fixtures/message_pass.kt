package com.example.drivelint.sample

import androidx.car.app.model.MessageTemplate

class MessagePassScreen {
    fun buildTemplate(): MessageTemplate {
        return MessageTemplate.Builder("연결이 끊어졌습니다. 다시 시도해주세요.")
            .setTitle("안내")
            .build()
    }
}
