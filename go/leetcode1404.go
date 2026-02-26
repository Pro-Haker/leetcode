func numSteps(s string)int{t:=len(s)-1;o:=false;for i:=len(s)-1;i>0;i--{if s[i]=='1'!=o{o=true;t++}};if o{t++};return t}
