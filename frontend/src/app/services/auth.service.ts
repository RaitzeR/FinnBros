import { Observable } from 'rxjs/Observable';
import { Injectable } from '@angular/core';
import { AngularFireAuth } from 'angularfire2/auth';
import {
  AngularFirestore,
  AngularFirestoreDocument
} from 'angularfire2/firestore';
import { Router } from '@angular/router';
import { BehaviorSubject } from 'rxjs/BehaviorSubject';

@Injectable()
export class AuthService {
  private user: Observable<User>;
  private userFetched = new BehaviorSubject<boolean>(false);

  constructor(
    private afa: AngularFireAuth,
    private afs: AngularFirestore,
    private router: Router
  ) {
    /// Get authenticated and user's data from Firestore || null
    this.user = this.afa.authState.switchMap(user => {
      this.userFetched.next(true);
      if (user) {
        const dbUser = user as User;
        return Observable.of(user);
      } else {
        return Observable.of(null);
      }
    });
  }

  // Singup
  public singupWithEmail(email: string, password: string) {
    this.afa.auth
      .createUserAndRetrieveDataWithEmailAndPassword(email, password)
      .then(authCredentials => {
        const uid = authCredentials.user.uid as string;
        const user: User = {
          uid,
          email
        };
        console.log('Logged in as:', user);
        this.router.navigate(['/find']);
      })
      .catch(console.error);
  }

  public getUser(): Observable<User> {
    // Send userObservable
    return this.user;
  }

  /// Login and signout methods
  public signOut() {
    this.afa.auth.signOut().then(() => {
      this.router.navigate(['/']);
    });
  }

  public loginWithEmail(email: string, password: string) {
    return this.afa.auth
      .signInWithEmailAndPassword(email, password)
      .then(user => {
        console.log('Logged in as:', user);
        this.router.navigate(['/find']);
      });
  }
}
