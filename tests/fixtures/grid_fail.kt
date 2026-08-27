package com.example.drivelint.sample

import androidx.car.app.model.GridItem
import androidx.car.app.model.GridTemplate

class GridFailScreen {
    fun buildTemplate(): GridTemplate {
        return GridTemplate.Builder()
            .setTitle("음악 장르")
            .addItem(GridItem.Builder().setTitle("팝").build())
            .addItem(GridItem.Builder().setTitle("록").build())
            .addItem(GridItem.Builder().setTitle("재즈").build())
            .addItem(GridItem.Builder().setTitle("클래식").build())
            .addItem(GridItem.Builder().setTitle("힙합").build())
            .addItem(GridItem.Builder().setTitle("EDM").build())
            .addItem(GridItem.Builder().setTitle("트로트").build())
            .build()
    }
}
