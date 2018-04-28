import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { FoodProductModalComponent } from './food-product-modal.component';

describe('FoodProductModalComponent', () => {
  let component: FoodProductModalComponent;
  let fixture: ComponentFixture<FoodProductModalComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ FoodProductModalComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(FoodProductModalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
