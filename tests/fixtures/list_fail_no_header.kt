package com.example.drivelint.sample

import androidx.car.app.model.ListTemplate
import androidx.car.app.model.SectionedItemList

class ListNoHeaderScreen {
    fun buildTemplate(): ListTemplate {
        return ListTemplate.Builder()
            .addSectionedList(SectionedItemList.create(favoritesList, ""))
            .build()
    }
}
