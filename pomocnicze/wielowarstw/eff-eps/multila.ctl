(define-param sx 300)
(define-param pad 2)
(define-param dlfali 30)
(define-param sx2 (/ sx 2))
(define-param sx4 (/ sx 4))
(set! geometry-lattice (make lattice (size (+ (* 2 pad) sx) (+ (* 2 pad) sx) no-size)))
(set! pml-layers (list (make pml (thickness pad))))
(set-param! resolution 1)

(define ((pw-amp k x0) x)
(exp (* 0+1i (vector3-dot k (vector3+ x x0)))))
(define-param fcen 0.8) ; pulse center frequency
(define-param df 0.02) ; turn-on bandwidth
(define-param kdir (vector3 1 1)) ; direction of k (length is irrelevant)
(define k (vector3-scale (* 2 pi fcen)
(unit-vector3 kdir))) ; k with correct length

(set! sources (list
               (make source
                 (src (make  continuous-src (wavelength dlfali)  ))
                 (component Ez) (center (* -1 sx4 ) (* -1 sx4 )) (size sx2)
		 (amp-func (pw-amp k (vector3 0 0.5)))
		)
	       )
	      
)

(run-until (* 2 sx)
           (at-beginning output-epsilon)
           (after-time  sx (at-every (/ dlfali 6) output-tot-pwr))
)

