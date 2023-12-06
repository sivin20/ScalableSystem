import { TestBed } from '@angular/core/testing';

import { FontPageService } from './font-page.service';

describe('FontPageService', () => {
  let service: FontPageService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(FontPageService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
