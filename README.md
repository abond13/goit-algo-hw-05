## Результати                       
```                       
                       Text_1 (Sub exists)    Text_2 (Sub exists)    Text_1 (Sub doesn't)   Text_2 (Sub doesn't)   
boyer_moore_search     0.06327525000000006    0.03471312500000001    0.03375949999999994    0.10906629200000006    
kmp_search             0.15077945800000003    0.19630695799999986    0.21007949999999997    0.28546645800000015    
rabin_karp_search      0.327987958            0.39611029200000014    0.4250579170000002     0.6089129579999999
```

## Висновки
У всіх випадках найкраще працює алгоритм Боєра-Мура, а найгірший -- алгоритм Рабіна-Карпа, який особливо погано працює для випадків, коли виконується пошук неіснуючого підрядка.