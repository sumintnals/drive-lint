package com.example.drivelint.sample

import androidx.car.app.model.signin.SignInTemplate
import androidx.car.app.model.signin.PinSignInMethod

class SignInPassScreen {
    fun buildTemplate(): SignInTemplate {
        return SignInTemplate.Builder(PinSignInMethod("123456"))
            .setTitle("로그인")
            .build()
    }
}
