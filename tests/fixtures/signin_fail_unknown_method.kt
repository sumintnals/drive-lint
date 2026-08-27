package com.example.drivelint.sample

import androidx.car.app.model.signin.SignInTemplate

class SignInUnknownMethodScreen {
    fun buildTemplate(): SignInTemplate {
        return SignInTemplate.Builder(someMysteryMethod)
            .setTitle("로그인")
            .build()
    }
}
