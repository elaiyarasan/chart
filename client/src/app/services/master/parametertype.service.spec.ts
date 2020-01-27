import { TestBed } from '@angular/core/testing';

import { ParametertypeService } from './parametertype.service';

describe('ParametertypeService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: ParametertypeService = TestBed.get(ParametertypeService);
    expect(service).toBeTruthy();
  });
});
