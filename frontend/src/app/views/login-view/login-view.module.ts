import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { LoginViewRoutingModule } from './login-view-routing.module';
import { LoginViewComponent } from './login-view.component';
import { LoginModule } from '@features/login/login.module';

@NgModule({
  imports: [
    CommonModule,
    LoginViewRoutingModule,
    LoginModule
  ],
  declarations: [LoginViewComponent]
})
export class LoginViewModule { }
