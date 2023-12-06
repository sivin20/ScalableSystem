import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TaxiPricePageComponent } from './taxi-price-page.component';

describe('TaxiPricePageComponent', () => {
  let component: TaxiPricePageComponent;
  let fixture: ComponentFixture<TaxiPricePageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [TaxiPricePageComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(TaxiPricePageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
