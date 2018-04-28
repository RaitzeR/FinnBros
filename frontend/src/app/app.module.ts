import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';

import { AppComponent } from './app.component';
import { NavModule } from './features/nav/nav.module';
import { FoodService } from './services/food.service';
import { FirebaseModule } from './modules/firebase/firebase.module';
import { HttpClientModule } from '@angular/common/http';
import { MatButtonModule } from '@angular/material';

@NgModule({
  declarations: [AppComponent],
  imports: [
    BrowserModule,
    AppRoutingModule,
    NavModule,
    FirebaseModule,
    HttpClientModule,
    MatButtonModule
  ],
  providers: [FoodService],
  bootstrap: [AppComponent]
})
export class AppModule {}
