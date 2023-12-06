import { ComponentFixture, TestBed } from '@angular/core/testing';

import { WelcomePage } from './welcome-page.component';

describe('WelcomePageComponent', () => {
  let component: WelcomePage;
  let fixture: ComponentFixture<WelcomePage>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [WelcomePage]
    })
    .compileComponents();

    fixture = TestBed.createComponent(WelcomePage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
