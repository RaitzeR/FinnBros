import { TestBed, inject } from '@angular/core/testing';

import { FoodFormService } from './food-form.service';

describe('FoodFormService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [FoodFormService]
    });
  });

  it('should be created', inject([FoodFormService], (service: FoodFormService) => {
    expect(service).toBeTruthy();
  }));
});
