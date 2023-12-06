import { TestBed } from '@angular/core/testing';

import { TaxiPriceService } from './taxi-price.service';

describe('FontPageService', () => {
  let service: TaxiPriceService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(TaxiPriceService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
