strengthens(d1, defendant).
strengthens(d2, defendant).
strengthens(d3, defendant).

case(c1, defendant).
val(c1, d1, 18). val(c1, d2, 60). mf(c1, d1, 12).

case(c2, defendant).
val(c2, d2, 35). val(c2, d3, 7). mf(c2, d3, 6).

case(c3, plaintiff).
val(c3, d2, 30). mf(c3, d2, 40).

focus_case(cf).
val(cf, d1, 16). val(cf, d2, 70). val(cf, d3, 8).
