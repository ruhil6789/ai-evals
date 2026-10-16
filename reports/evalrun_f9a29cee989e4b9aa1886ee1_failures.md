# Lyrics composer eval — failures

## Fail #1 (sample 1)
- gold: `annu malik`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "madan mohan", "annu malik"]}`
- title: `tan tanaa tan tan tan taaraa chalatii hai kyaa nau se baarah`
- [FAIL] Exact match (pred == gold composer): pred='laxmikantpyarelal' ref='annu malik'
- [PASS] Top-3 contains gold composer: ref='annu malik' in top3=['laxmikantpyarelal', 'madan mohan', 'annu malik']

## Fail #2 (sample 3)
- gold: `naushad`
- output: `{"pred": "c ramchandra", "top3": ["c ramchandra", "naushad", "s d burman"]}`
- title: `jale naa kyon paravaanaa`
- [FAIL] Exact match (pred == gold composer): pred='c ramchandra' ref='naushad'
- [PASS] Top-3 contains gold composer: ref='naushad' in top3=['c ramchandra', 'naushad', 's d burman']

## Fail #3 (sample 5)
- gold: `s d burman`
- output: `{"pred": "naushad", "top3": ["naushad", "shankarjaikishan", "s d burman"]}`
- title: `saanjh dhalii dil kii lagii thak chalii pukaar ke`
- [FAIL] Exact match (pred == gold composer): pred='naushad' ref='s d burman'
- [PASS] Top-3 contains gold composer: ref='s d burman' in top3=['naushad', 'shankarjaikishan', 's d burman']

## Fail #4 (sample 6)
- gold: `r d burman`
- output: `{"pred": "s d burman", "top3": ["s d burman", "shankarjaikishan", "r d burman"]}`
- title: `rimjhim gire saavan sulag sulag jaaye man  both versions`
- [FAIL] Exact match (pred == gold composer): pred='s d burman' ref='r d burman'
- [PASS] Top-3 contains gold composer: ref='r d burman' in top3=['s d burman', 'shankarjaikishan', 'r d burman']

## Fail #5 (sample 7)
- gold: `r d burman`
- output: `{"pred": "a r rahman", "top3": ["a r rahman", "kalyanjianandji", "s d burman"]}`
- title: `ek chatur naar kar ke singaar`
- [FAIL] Exact match (pred == gold composer): pred='a r rahman' ref='r d burman'
- [FAIL] Top-3 contains gold composer: ref='r d burman' in top3=['a r rahman', 'kalyanjianandji', 's d burman']

## Fail #6 (sample 8)
- gold: `s d burman`
- output: `{"pred": "madan mohan", "top3": ["madan mohan", "r d burman", "s d burman"]}`
- title: `ye raat ye chaandanii phir kahaan sun jaa dil kii lata version`
- [FAIL] Exact match (pred == gold composer): pred='madan mohan' ref='s d burman'
- [PASS] Top-3 contains gold composer: ref='s d burman' in top3=['madan mohan', 'r d burman', 's d burman']

## Fail #7 (sample 9)
- gold: `c ramchandra`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "naushad", "kalyanjianandji"]}`
- title: `maar kataarii mar jaanaa`
- [FAIL] Exact match (pred == gold composer): pred='shankarjaikishan' ref='c ramchandra'
- [FAIL] Top-3 contains gold composer: ref='c ramchandra' in top3=['shankarjaikishan', 'naushad', 'kalyanjianandji']

## Fail #8 (sample 10)
- gold: `r d burman`
- output: `{"pred": "annu malik", "top3": ["annu malik", "a r rahman", "laxmikantpyarelal"]}`
- title: `mriganayanii chandramukhii`
- [FAIL] Exact match (pred == gold composer): pred='annu malik' ref='r d burman'
- [FAIL] Top-3 contains gold composer: ref='r d burman' in top3=['annu malik', 'a r rahman', 'laxmikantpyarelal']

## Fail #9 (sample 11)
- gold: `naushad`
- output: `{"pred": "c ramchandra", "top3": ["c ramchandra", "naushad", "laxmikantpyarelal"]}`
- title: `ghar aayaa mahamaan koii jaan na pahachaan bane baalamaa`
- [FAIL] Exact match (pred == gold composer): pred='c ramchandra' ref='naushad'
- [PASS] Top-3 contains gold composer: ref='naushad' in top3=['c ramchandra', 'naushad', 'laxmikantpyarelal']

## Fail #10 (sample 12)
- gold: `a r rahman`
- output: `{"pred": "s d burman", "top3": ["s d burman", "a r rahman", "r d burman"]}`
- title: `rozaanaa zamaanaa paracham apanaa laharaaegaa`
- [FAIL] Exact match (pred == gold composer): pred='s d burman' ref='a r rahman'
- [PASS] Top-3 contains gold composer: ref='a r rahman' in top3=['s d burman', 'a r rahman', 'r d burman']

## Fail #11 (sample 13)
- gold: `laxmikantpyarelal`
- output: `{"pred": "r d burman", "top3": ["r d burman", "s d burman", "laxmikantpyarelal"]}`
- title: `agar dilabar kii rusvaaii hamen manzuur ho jaaye`
- [FAIL] Exact match (pred == gold composer): pred='r d burman' ref='laxmikantpyarelal'
- [PASS] Top-3 contains gold composer: ref='laxmikantpyarelal' in top3=['r d burman', 's d burman', 'laxmikantpyarelal']

## Fail #12 (sample 14)
- gold: `r d burman`
- output: `{"pred": "kalyanjianandji", "top3": ["kalyanjianandji", "r d burman", "laxmikantpyarelal"]}`
- title: `kaabul se aayaa meraa diladaar`
- [FAIL] Exact match (pred == gold composer): pred='kalyanjianandji' ref='r d burman'
- [PASS] Top-3 contains gold composer: ref='r d burman' in top3=['kalyanjianandji', 'r d burman', 'laxmikantpyarelal']

## Fail #13 (sample 15)
- gold: `shankarjaikishan`
- output: `{"pred": "r d burman", "top3": ["r d burman", "laxmikantpyarelal", "s d burman"]}`
- title: `lapak jhapak tuu aa re badaravaa`
- [FAIL] Exact match (pred == gold composer): pred='r d burman' ref='shankarjaikishan'
- [FAIL] Top-3 contains gold composer: ref='shankarjaikishan' in top3=['r d burman', 'laxmikantpyarelal', 's d burman']

## Fail #14 (sample 17)
- gold: `r d burman`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "laxmikantpyarelal", "annu malik"]}`
- title: `aate jaate hue main sab pe nazar rakhataa huun naam abdul hai`
- [FAIL] Exact match (pred == gold composer): pred='shankarjaikishan' ref='r d burman'
- [FAIL] Top-3 contains gold composer: ref='r d burman' in top3=['shankarjaikishan', 'laxmikantpyarelal', 'annu malik']

## Fail #15 (sample 18)
- gold: `a r rahman`
- output: `{"pred": "madan mohan", "top3": ["madan mohan", "a r rahman", "c ramchandra"]}`
- title: `thodaathodaa pyaar ho gayaa tumase`
- [FAIL] Exact match (pred == gold composer): pred='madan mohan' ref='a r rahman'
- [PASS] Top-3 contains gold composer: ref='a r rahman' in top3=['madan mohan', 'a r rahman', 'c ramchandra']

## Fail #16 (sample 19)
- gold: `laxmikantpyarelal`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "naushad", "laxmikantpyarelal"]}`
- title: `naach hasiinaa naach ki duniyaa dekhe`
- [FAIL] Exact match (pred == gold composer): pred='shankarjaikishan' ref='laxmikantpyarelal'
- [PASS] Top-3 contains gold composer: ref='laxmikantpyarelal' in top3=['shankarjaikishan', 'naushad', 'laxmikantpyarelal']

## Fail #17 (sample 20)
- gold: `laxmikantpyarelal`
- output: `{"pred": "r d burman", "top3": ["r d burman", "laxmikantpyarelal", "kalyanjianandji"]}`
- title: `i am in love  koii hai aashiq koii mahabuub hai`
- [FAIL] Exact match (pred == gold composer): pred='r d burman' ref='laxmikantpyarelal'
- [PASS] Top-3 contains gold composer: ref='laxmikantpyarelal' in top3=['r d burman', 'laxmikantpyarelal', 'kalyanjianandji']

## Fail #18 (sample 21)
- gold: `c ramchandra`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "s d burman", "r d burman"]}`
- title: `kaarii kaarii kaarii andhiyaarii`
- [FAIL] Exact match (pred == gold composer): pred='shankarjaikishan' ref='c ramchandra'
- [FAIL] Top-3 contains gold composer: ref='c ramchandra' in top3=['shankarjaikishan', 's d burman', 'r d burman']

## Fail #19 (sample 22)
- gold: `kalyanjianandji`
- output: `{"pred": "r d burman", "top3": ["r d burman", "kalyanjianandji", "annu malik"]}`
- title: `are diivaanon mujhe pahachaanon  main huun don`
- [FAIL] Exact match (pred == gold composer): pred='r d burman' ref='kalyanjianandji'
- [PASS] Top-3 contains gold composer: ref='kalyanjianandji' in top3=['r d burman', 'kalyanjianandji', 'annu malik']

## Fail #20 (sample 23)
- gold: `shankarjaikishan`
- output: `{"pred": "r d burman", "top3": ["r d burman", "madan mohan", "kalyanjianandji"]}`
- title: `tumhen main agar apanaa saathii banaa luun`
- [FAIL] Exact match (pred == gold composer): pred='r d burman' ref='shankarjaikishan'
- [FAIL] Top-3 contains gold composer: ref='shankarjaikishan' in top3=['r d burman', 'madan mohan', 'kalyanjianandji']

## Fail #21 (sample 25)
- gold: `shankarjaikishan`
- output: `{"pred": "s d burman", "top3": ["s d burman", "madan mohan", "r d burman"]}`
- title: `daag na lag jaaye`
- [FAIL] Exact match (pred == gold composer): pred='s d burman' ref='shankarjaikishan'
- [FAIL] Top-3 contains gold composer: ref='shankarjaikishan' in top3=['s d burman', 'madan mohan', 'r d burman']

## Fail #22 (sample 26)
- gold: `s d burman`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "s d burman", "c ramchandra"]}`
- title: `chale chalo prem ke saathii prem nagar hai jaanaa`
- [FAIL] Exact match (pred == gold composer): pred='laxmikantpyarelal' ref='s d burman'
- [PASS] Top-3 contains gold composer: ref='s d burman' in top3=['laxmikantpyarelal', 's d burman', 'c ramchandra']

## Fail #23 (sample 27)
- gold: `madan mohan`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "kalyanjianandji", "laxmikantpyarelal"]}`
- title: `jabjab tumhen bhulaayaa tum aur yaad aae`
- [FAIL] Exact match (pred == gold composer): pred='shankarjaikishan' ref='madan mohan'
- [FAIL] Top-3 contains gold composer: ref='madan mohan' in top3=['shankarjaikishan', 'kalyanjianandji', 'laxmikantpyarelal']

## Fail #24 (sample 29)
- gold: `shankarjaikishan`
- output: `{"pred": "s d burman", "top3": ["s d burman", "laxmikantpyarelal", "madan mohan"]}`
- title: `o basantii pavan paagal naa jaa re naa jaa roko koii`
- [FAIL] Exact match (pred == gold composer): pred='s d burman' ref='shankarjaikishan'
- [FAIL] Top-3 contains gold composer: ref='shankarjaikishan' in top3=['s d burman', 'laxmikantpyarelal', 'madan mohan']

## Fail #25 (sample 32)
- gold: `annu malik`
- output: `{"pred": "r d burman", "top3": ["r d burman", "annu malik", "naushad"]}`
- title: `aaj nahiin to kal aaoge tum idhar`
- [FAIL] Exact match (pred == gold composer): pred='r d burman' ref='annu malik'
- [PASS] Top-3 contains gold composer: ref='annu malik' in top3=['r d burman', 'annu malik', 'naushad']

## Fail #26 (sample 33)
- gold: `r d burman`
- output: `{"pred": "a r rahman", "top3": ["a r rahman", "s d burman", "c ramchandra"]}`
- title: `piyaa baanwarii piyaa baanwarii pii kahaan pii kahaan`
- [FAIL] Exact match (pred == gold composer): pred='a r rahman' ref='r d burman'
- [FAIL] Top-3 contains gold composer: ref='r d burman' in top3=['a r rahman', 's d burman', 'c ramchandra']

## Fail #27 (sample 34)
- gold: `c ramchandra`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "kalyanjianandji", "naushad"]}`
- title: `duaa kar gamedil khudaa se duaa kar`
- [FAIL] Exact match (pred == gold composer): pred='laxmikantpyarelal' ref='c ramchandra'
- [FAIL] Top-3 contains gold composer: ref='c ramchandra' in top3=['laxmikantpyarelal', 'kalyanjianandji', 'naushad']

## Fail #28 (sample 35)
- gold: `annu malik`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "kalyanjianandji", "annu malik"]}`
- title: `aaye dil jaanii chiichii vaalaa chhallaa  aankhon men kaajal maathe pe pasiinaa`
- [FAIL] Exact match (pred == gold composer): pred='laxmikantpyarelal' ref='annu malik'
- [PASS] Top-3 contains gold composer: ref='annu malik' in top3=['laxmikantpyarelal', 'kalyanjianandji', 'annu malik']

## Fail #29 (sample 36)
- gold: `s d burman`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "kalyanjianandji", "c ramchandra"]}`
- title: `main tere pyaar men kyaa kyaa na banaa`
- [FAIL] Exact match (pred == gold composer): pred='shankarjaikishan' ref='s d burman'
- [FAIL] Top-3 contains gold composer: ref='s d burman' in top3=['shankarjaikishan', 'kalyanjianandji', 'c ramchandra']

## Fail #30 (sample 37)
- gold: `r d burman`
- output: `{"pred": "kalyanjianandji", "top3": ["kalyanjianandji", "laxmikantpyarelal", "r d burman"]}`
- title: `diivaanaa mujh saa nahiin is ambar ke niiche`
- [FAIL] Exact match (pred == gold composer): pred='kalyanjianandji' ref='r d burman'
- [PASS] Top-3 contains gold composer: ref='r d burman' in top3=['kalyanjianandji', 'laxmikantpyarelal', 'r d burman']

## Fail #31 (sample 39)
- gold: `shankarjaikishan`
- output: `{"pred": "r d burman", "top3": ["r d burman", "s d burman", "naushad"]}`
- title: `o jaane vaale mud ke zaraa dekhate jaanaa`
- [FAIL] Exact match (pred == gold composer): pred='r d burman' ref='shankarjaikishan'
- [FAIL] Top-3 contains gold composer: ref='shankarjaikishan' in top3=['r d burman', 's d burman', 'naushad']

## Fail #32 (sample 40)
- gold: `a r rahman`
- output: `{"pred": "r d burman", "top3": ["r d burman", "annu malik", "a r rahman"]}`
- title: `telephone dhun men hansane vaalii`
- [FAIL] Exact match (pred == gold composer): pred='r d burman' ref='a r rahman'
- [PASS] Top-3 contains gold composer: ref='a r rahman' in top3=['r d burman', 'annu malik', 'a r rahman']

## Fail #33 (sample 41)
- gold: `shankarjaikishan`
- output: `{"pred": "r d burman", "top3": ["r d burman", "laxmikantpyarelal", "shankarjaikishan"]}`
- title: `chhuune na duungii haath re najariyon se dil bhar duungii`
- [FAIL] Exact match (pred == gold composer): pred='r d burman' ref='shankarjaikishan'
- [PASS] Top-3 contains gold composer: ref='shankarjaikishan' in top3=['r d burman', 'laxmikantpyarelal', 'shankarjaikishan']

## Fail #34 (sample 43)
- gold: `madan mohan`
- output: `{"pred": "kalyanjianandji", "top3": ["kalyanjianandji", "laxmikantpyarelal", "shankarjaikishan"]}`
- title: `husn haazir hai muhabbat kii sazaa paane ko`
- [FAIL] Exact match (pred == gold composer): pred='kalyanjianandji' ref='madan mohan'
- [FAIL] Top-3 contains gold composer: ref='madan mohan' in top3=['kalyanjianandji', 'laxmikantpyarelal', 'shankarjaikishan']

## Fail #35 (sample 44)
- gold: `naushad`
- output: `{"pred": "s d burman", "top3": ["s d burman", "naushad", "a r rahman"]}`
- title: `husnejaanaa idhar aa`
- [FAIL] Exact match (pred == gold composer): pred='s d burman' ref='naushad'
- [PASS] Top-3 contains gold composer: ref='naushad' in top3=['s d burman', 'naushad', 'a r rahman']

## Fail #36 (sample 45)
- gold: `naushad`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "laxmikantpyarelal", "madan mohan"]}`
- title: `nirdhan kaa ghar luutane vaalon luut lo dil kaa pyaar`
- [FAIL] Exact match (pred == gold composer): pred='shankarjaikishan' ref='naushad'
- [FAIL] Top-3 contains gold composer: ref='naushad' in top3=['shankarjaikishan', 'laxmikantpyarelal', 'madan mohan']

## Fail #37 (sample 47)
- gold: `r d burman`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "annu malik", "r d burman"]}`
- title: `jaane kyaa baat hai niind nahiin aatii badii lambii raat hai`
- [FAIL] Exact match (pred == gold composer): pred='laxmikantpyarelal' ref='r d burman'
- [PASS] Top-3 contains gold composer: ref='r d burman' in top3=['laxmikantpyarelal', 'annu malik', 'r d burman']

## Fail #38 (sample 48)
- gold: `laxmikantpyarelal`
- output: `{"pred": "r d burman", "top3": ["r d burman", "laxmikantpyarelal", "kalyanjianandji"]}`
- title: `dilabar jaanii chalii havaa mastaanii`
- [FAIL] Exact match (pred == gold composer): pred='r d burman' ref='laxmikantpyarelal'
- [PASS] Top-3 contains gold composer: ref='laxmikantpyarelal' in top3=['r d burman', 'laxmikantpyarelal', 'kalyanjianandji']

## Fail #39 (sample 50)
- gold: `r d burman`
- output: `{"pred": "kalyanjianandji", "top3": ["kalyanjianandji", "laxmikantpyarelal", "madan mohan"]}`
- title: `ye saaye hain ye duniyaa hai parachhaaiyon kii`
- [FAIL] Exact match (pred == gold composer): pred='kalyanjianandji' ref='r d burman'
- [FAIL] Top-3 contains gold composer: ref='r d burman' in top3=['kalyanjianandji', 'laxmikantpyarelal', 'madan mohan']

## Fail #40 (sample 51)
- gold: `s d burman`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "naushad", "annu malik"]}`
- title: `o lag gaiin ankhiyaan tum se morii`
- [FAIL] Exact match (pred == gold composer): pred='shankarjaikishan' ref='s d burman'
- [FAIL] Top-3 contains gold composer: ref='s d burman' in top3=['shankarjaikishan', 'naushad', 'annu malik']
