package com.example.drivelint.sample

import androidx.car.app.model.ListTemplate
import androidx.car.app.model.SectionedItemList

class ListWithHeaderScreen {
    fun buildTemplate(): ListTemplate {
        return ListTemplate.Builder()
            .addSectionedList(SectionedItemList.create(favoritesList, "즐겨찾기"))
            .build()
    }
}
