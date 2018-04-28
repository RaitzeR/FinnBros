import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { LoginViewRoutingModule } from './login-view-routing.module';
import { LoginViewComponent } from './login-view.component';

@NgModule({
  imports: [
    CommonModule,
    LoginViewRoutingModule
  ],
  declarations: [LoginViewComponent]
})
export class LoginViewModule { }
