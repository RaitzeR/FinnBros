import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';

import { AppComponent } from './app.component';
import { NavModule } from './features/nav/nav.module';
import { FoodService } from './services/food.service';
import { FirebaseModule } from './modules/firebase/firebase.module';
import { HttpClientModule } from '@angular/common/http';
import { MatButtonModule } from '@angular/material';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { DropZoneDirective } from './directives/drop-zone.directive';
import { AuthService } from './services/auth.service';

@NgModule({
  declarations: [AppComponent, DropZoneDirective],
  imports: [
    BrowserModule,
    AppRoutingModule,
    NavModule,
    FirebaseModule,
    HttpClientModule,
    MatButtonModule,
    BrowserAnimationsModule
  ],
  providers: [FoodService, AuthService],
  bootstrap: [AppComponent]
})
export class AppModule {}
