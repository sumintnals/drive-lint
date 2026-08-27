package com.example.drivelint.sample

import androidx.car.app.model.LongMessageTemplate

class LongMessagePassScreen {
    fun buildTemplate(): LongMessageTemplate {
        return LongMessageTemplate.Builder("여기에 이용약관 전문이 들어갑니다...")
            .setTitle("이용약관")
            .build()
    }
}
