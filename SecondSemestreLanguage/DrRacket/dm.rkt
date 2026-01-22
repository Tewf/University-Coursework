(require (lib "turtles.ss" "graphics"))
(turtles #t)

(define (axeHorizontal largeurdiag)
  ; int -> trace
  ; largeur diagramme  -> tracer l'axe horizontale
  (draw largeurdiag)
  (move (- largeurdiag))
  )
;(axeHorizontal 200)



(define (axeVertical longeurdiag echelle)
  (let ((position 0))
    (if (>= position longeurdiag)
        (move (- longeurdiag))
        (begin
          (turn 90)
          (draw (* echelle 5))
          (turn -90)
          (draw (* echelle 2))
          (move (- (* echelle 2)))
          (turn 90)
          (set! position (+ position 5))
          (if (>= position longeurdiag)
              (move (- longeurdiag))
               
              (begin
                (draw (* echelle 5))
                (turn -90)
                (draw (* echelle 5))
                (move (- (* echelle 5)))
                (set! position (+ position 5))
                (axeVertical (- longeurdiag 10) echelle)))))))  
;(axeVertical 55 3)




  
(define(traceRectangle hauteurRec largeurRec)
  ; int int -> trace
  ; largeur et hauteur du rectangle  -> tracer le rectangle
  ;reviens à la position initiale
  (draw largeurRec)
  (turn 90)
  (draw hauteurRec)
  (turn 90)
  (draw largeurRec)
  (turn 90)
  (draw hauteurRec)
  (turn 90)
  )
;(traceRectangle 160 160)

(define (traceRectanglePlein hauteurRec largeurRec)
  ; int int -> trace
  ; largeur et hauteur du rectangle  -> tracer le rectangle rempli de lignes paralles
  ;à chaque fois il avance d'un pas de 1 de facons qu'on aura pls lignes paralles de hauteur du rectangle souhaité
  ;position indique la position de la fleche où elle est
  (let ((position 1))
    (if (> position largeurRec)
        (move (- largeurRec))
        (begin
          (draw 1)
          (turn 90)
          (draw hauteurRec)
          (move (- hauteurRec))
          (turn -90)
          (+ 1 position)
          (traceRectanglePlein hauteurRec (- largeurRec 1))
          ))))

;(traceRectanglePlein 150 150)











(define (maxListe l)
  ; liste -> int
  ; liste des reels  -> le plus grand element
  (if (null? (cdr l)) 
      (car l) 
      (if (< (car l) (maxListe (cdr l)))  
          (maxListe (cdr l)) 
          (car l)
          )
      )
  )
;(maxListe '(1 2 30 4 85 106 7 8 9))


(define (multiplieListe lst n)
  ; liste reel -> liste
  ; liste des reels et un reel   -> liste des reels multiplié par 
  (cond ((null? lst) '())
        (else (cons (* (car lst) n) (multiplieListe (cdr lst) n)))))

;(multiplieListe '(1 2 3 4 5 6 7 8 9) 2)

(define (saisieListe n)
  (if (= n 0)
      '()
      (cons (read) (saisieListe (- n 1)))))
;(saisieListe 5)



(define (initialization)
  (define position (/ (- turtle-window-size 20) 2))
  (display position)
  (move (- position))
  (turn -90)
  (move position)
  (turn 90))
(initialization)

(axeHorizontal (- turtle-window-size 10))
(axeVertical longeurdiag 1)