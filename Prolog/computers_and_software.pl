spec(comp1, pc, 32).                                     /* Fact  1 */
spec(comp2, mac, 128).                                   /* Fact  2 */
spec(comp3, pc, 64).                                     /* Fact  3 */
runs(pc, movie_edit, 96).                                /* Fact  4 */
runs(pc, vb, 16).                                        /* Fact  5 */
runs(pc, cpp, 28).                                       /* Fact  6 */
runs(mac, vb, 24).                                       /* Fact  7 */
runs(mac, prolog, 128).                                  /* Fact  8 */
access(judy, comp1).                                     /* Fact  9 */
access(peter, comp3).                                    /* Fact 10 */
access(david, comp1).                                    /* Fact 11 */
access(david, comp2).                                    /* Fact 12 */

can_use(P, SW) :- access(P, Comp), can_run(Comp, SW).    /* Rule  1 */

can_run(Comp, SW) :- spec(Comp, CompType, MemAvail),
                     runs(CompType, SW, MemNeeded),
                     MemAvail >= MemNeeded.              /* Rule  2 */
