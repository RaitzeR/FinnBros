import { Component, OnInit } from '@angular/core';
import { AuthService } from '../../services/auth.service';
import { BehaviorSubject } from 'rxjs/BehaviorSubject';

@Component({
  selector: 'bro-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {
  public createNew = new BehaviorSubject<boolean>(false);
  public loginData = {
    email: undefined,
    password: undefined
  };

  constructor(private auth: AuthService) {}

  ngOnInit() {}

  toggleNew() {
    const newValue = !this.createNew.getValue();
    this.createNew.next(newValue);
  }

  login(form) {
    const attributes = {
      email: form.value.email as string,
      password: form.value.password as string
    };
    this.auth.loginWithEmail(attributes.email, attributes.password);
  }

  createAccount(form) {
    const attributes = {
      email: form.value.email as string,
      password: form.value.password as string
    };
    this.auth.singupWithEmail(attributes.email, attributes.password);
  }
}
