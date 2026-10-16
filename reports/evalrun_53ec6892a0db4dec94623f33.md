# Eval report: baseline-full

- **eval**: `Lyrics → Composer (ablation compare)` (`eval_264339e54137407d9da6fd4f`)
- **run**: `evalrun_53ec6892a0db4dec94623f33`
- **status**: `completed`
- **model**: `baseline-full`
- **pass rate**: **30%** (160/527; failed=367, errored=0)

## Per-criteria results

| Criteria | Passed | Failed |
|----------|--------|--------|
| `Exact match (pred == gold composer)-d2638ca3a879` | 160 | 367 |
| `Top-3 contains gold composer-f1506e76bfc5` | 335 | 192 |

## Samples

### #1 — FAIL

- item: `{'lyrics': ' aankh ladaa ke tuune maaraa ghaayal ho gayaa dil bechaaraa sunaa hai tere chaahane vaale aage das hain piichhe baarah mujhako apanaa chaand banaa le chamakaa de kismat kaa taaraa ek baar se dil nahiin bharataa mud ke dekh mujhe dobaaraa tan tanaa tan tan tan taaraa chalatii hai kyaa nau se baarah khadii khadii kyaa soch rahii hai chal ho jaaen nau do gyaarah tan tanaa tan threedots  raat ke show kii do tikaten hain khol ke purse main dikhalaauun chipak ke baithuun saath tere main taxi men le jaauun samajh na mujhako aisaa vaisaa mere batue men hai paisaa tujhe khilaauungaa jii bhar ke garam samosaa idalii dosaa tuu hai merii pepsii kolaa main teraa huun kokaa kolaa jaldii kar ki chadh na jaae thermometer kaa ye paaraa ek baar se dil threedots  filmii dhun pe dekh ke tujhako siitii roz bajaauun bahut dinon se soch rahaa thaa film main tujhe dikhaauun shukravaar kii shaam hasiin hai naii naii ye film lagii hai garmii kii na hogii tension theatre hai vo air conditioned film hasiin vo jaaneman hai ye filmon men number one hai govindaa hai hiiro usakaa aur maadhurii hiiroin hai pichhalii siit kii do tikaten hain gupachup pyaar karenge yaaraa ek baar se dil threedots ', 'correct_label': 'annu malik', 'label': 1, 'split': 'test', 'title': 'tan tanaa tan tan tan taaraa chalatii hai kyaa nau se baarah', 'year': '1996'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "madan mohan", "annu malik"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='annu malik'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='annu malik' in top3=['laxmikantpyarelal', 'madan mohan', 'annu malik']

### #2 — PASS

- item: `{'lyrics': ' ai husn zaraa jaag tujhe ishk jagaaye badale merii takadir jo tu hosh men aaye  2  ye pyaara ke nagame ye muhabbat ke taraane tujhako bade aramaan se laayaa huun sunaane ummid mere dil kii kahiin tut na jaaye ye husn threedots  saazedile khaamosh men ek soj jagaa de tu bhii merii avaaz men avaaz milaa de aayaa huun tere dar pe badii aas lagaaye ye husn threedots  ai shammaa tu aajaa zaraa chilamanase nikalake hasarat hai ki rahaa jaauun terii aag men jalake paravaanaa vo kyaa tujhape jo mitakar naa dikhaa de ye husn threedots', 'correct_label': 'naushad', 'label': 6, 'split': 'test', 'title': 'ai husn zaraa jaag tujhe ishq jagaaye', 'year': '1963'}`
- output: `{"pred": "naushad", "top3": ["naushad", "laxmikantpyarelal", "c ramchandra"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='naushad' ref='naushad'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='naushad' in top3=['naushad', 'laxmikantpyarelal', 'c ramchandra']

### #3 — FAIL

- item: `{'lyrics': ' jale naa kyon  2 jale naa kyon paravaanaa 2  2 shamaa dikhaakar husn ke jalave  2 banaa ke jab diivaanaa jale naa kyon paravaanaa  dil kii lagii kaa naam hai ulfat  dil kii lagii kaa naam ulfat hai  2 aur ulfat kaa hai ye matalab  2 chupake chupake dhiire dhiire hans hans ke jal jaanaa  2 jale naa kyon paravaanaa  jale naa kyon threedots  jalanaa hai to phir jal jaaye ho jalanaa hai to phir jal jaaye  husn ke saanche men dhal jaaye  2 ishq men donon ek hai ab to jiinaa yaa mar jaanaa  2 jale na kyon paravaanaa shamaa threedots diivaanaa jale na kyon paravaanaa ', 'correct_label': 'naushad', 'label': 6, 'split': 'test', 'title': 'jale naa kyon paravaanaa', 'year': '-1'}`
- output: `{"pred": "c ramchandra", "top3": ["c ramchandra", "naushad", "s d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='c ramchandra' ref='naushad'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='naushad' in top3=['c ramchandra', 'naushad', 's d burman']

### #4 — PASS

- item: `{'lyrics': ' koii jab raah na paae mere sang aae ke pag pag diip jalaae merii dostii meraa pyaar  jiivan kaa yahii hai dastuur pyaar binaa akelaa majabuur dostii ko maane to sab dukh duur koi kaahe thokar khaae mere sang aae threedots  dono ke hain ruup hazaar par merii sune jo sansaar dostii hai bhaaii to bahanaa hai pyaar koi mat chain churaae mere sang aae threedots  pyaar kaa hai pyaar hii naam kahiin miiraa kahiin ghanashyaam dostii kaa yaaro nahiin koi daam koi kahiin duur naa jaae mere sang aae threedots', 'correct_label': 'laxmikantpyarelal', 'label': 4, 'split': 'test', 'title': 'koii jab raah na paae mere sang aae', 'year': '1964'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "r d burman", "kalyanjianandji"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='laxmikantpyarelal' ref='laxmikantpyarelal'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='laxmikantpyarelal' in top3=['laxmikantpyarelal', 'r d burman', 'kalyanjianandji']

### #5 — FAIL

- item: `{'lyrics': '     ma \t saanjh dhalii dil kii lagii thak chalii pukaar ke \taa jaa aa jaa aa bhii jaa aa \tkyaa duun pahale se main baithii huun dil haar ke \tjaa jaa jaa jaa jaa tuu jaa  2  ma \tzid pe aa gayaa hai dil ke aaj yuun na lautanaa aa \tmerii suno laut jaao chhod do ye bachapanaa ma \tchaar din kii zindagii men din hain do bahaar ke  \taa jaa aa jaa aa bhii jaa aa \te he he he \tkyaa duun pahale se main baithii huun dil haar ke \tjaa jaa jaa jaa jaa tuu jaa  ma \taa aa aa \tjaa jaa  \tkaise kahuun kaisii ulajhanon men merii jaan hai ma \to ho ho \thaan ko naa samajh gaye ye pyaar kii zubaan hai aa \tkaatane hain din hamen kisii ke intazaar ke  \tjaa jaa jaa jaa jaa tuu jaa ma \to ho ho ho \tsaanjh dhalii dil kii lagii thak chalii pukaar ke \taa jaa aa jaa aa bhii jaa aa \te e e e  \tkyaa duun pahale se main baithii huun dil haar ke \tjaa jaa jaa jaa jaa tuu jaa  ma \tsun to le ke mere dil kaa tujhase kyaa sawaal hai aa \tkuchh na kar sakuungii main isii kaa to malaal hai ma \tdil na tod chaahe bol do hii bol pyaar ke  \taa jaa aa jaa aa bhii jaa aa \tkyaa duun pahale se main baithii huun dil haar ke \tjaa jaa jaa jaa jaa tuu jaa ma \tsaanjh dhalii dil kii lagii thak chalii pukaar ke \taa jaa aa jaa aa bhii jaa aa \tjaa jaa jaa jaa jaa tuu jaa ma \taa jaa aa jaa aa \tjaa tuu jaa ', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'saanjh dhalii dil kii lagii thak chalii pukaar ke', 'year': '1960'}`
- output: `{"pred": "naushad", "top3": ["naushad", "shankarjaikishan", "s d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='naushad' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='s d burman' in top3=['naushad', 'shankarjaikishan', 's d burman']

### #6 — FAIL

- item: `{'lyrics': ' rimjhim gire saavan sulag sulag jaae man bhiige aaj is mausam men lagii kaisii ye agan rimjhim gire saavan threedots  pahale bhii yuun to barase the baadal pahale bhii yuun to bhiigaa thaa aanchal ab ke baras kyuun sajan  sulag sulag jaae man bhiige aaj is mausam men lagii kaisii ye agan rimjhim gire saavan threedots  is baar saavan dahakaa huaa hai  is baar mausam bahakaa huaa hai jaane piike chalii kyaa pavan  sulag sulag jaae man bhiige aaj is mausam men lagii kaisii ye agan rimjhim gire saavan threedots  rimjhim gire saavan sulag sulag jaae man bhiige aaj is mausam men lagii kaisii ye agan rimjhim gire saavan threedots  jab ghungharuon sii bajatii hain buunde aramaan hamaare palake na muunde kaise dekhe sapane nayan  sulag sulag jaae man bhiige aaj is mausam men lagii kaisii ye agan rimjhim gire saavan threedots  mahafil men kaise kah den kisii se dil bandh rahaa hai kis ajanabii se haay kare ab kyaa jatan  sulag sulag jaae man bhiige aaj is mausam men lagii kaisii ye agan rimjhim gire saavan threedots', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'rimjhim gire saavan sulag sulag jaaye man  both versions', 'year': '1979'}`
- output: `{"pred": "s d burman", "top3": ["s d burman", "shankarjaikishan", "r d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='s d burman' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='r d burman' in top3=['s d burman', 'shankarjaikishan', 'r d burman']

### #7 — FAIL

- item: `{'lyrics': ' ek chatur nar kar ke singar  mere man ke dvar ye ghusat jaat  ham marat jaat are he he he  yak chatur nar kar ke singarthreedots   pa re sa sa sa sa ni dh sa sa re sa dha dha pa  pa dha sa re sa sa re ga dha pa   yak chatur nar kar ke singaathreedots r  ki ummm  dham  mah ayyo   ki are dham o dham o dham dham dham ruk  o a aa i ii u u e ai o au an a vowels  um nam nam nam nam nam nam  nam nam lama lama lama lama la  um bal bal bal bal re  bal bal bal bal re bal bal bal bal re  om   ek chatur nar badi hoshiyar  2  apane hi jaal men phasat jaat  ham hasat jaat are ho ho ho ho ho   ek chatur nar badi hoshiyar   su tuu kyonthreedots  mah chhi re   kare lakh lakh duniya chaturai  chhutti kar dunga main usaki  abake jo avaz lagai  chhutti kar dunga aa aa aathreedots ta jum taka jum taka num yaka jum  tak tankidiathreedots  ki padh ke botan chir bi chakkar  2  har bud khudibudi khud kar  2 chhitake to rere mon makhan  2 sab chale gaye sab chale gaye chidamudh chiting chitubud  chitubud gaay chitubud gaay chitubud haay haay haay   ja re jaa re kare kaga  ka ka ka kyon shor machaaye  us nari ka das na ban jo  rah chalat ko rah bulae   kaalaa re jaa re jaa re  are nale men jaake tuu munh dhoke aa  kaalaa re ga re ga re   mah ye gadabad ji ki o ga re ga re  mah ye sur badala  ki o ga re ga re  mah ye hamako mataka bola  ki  o ga re ga re  mah ye sur kidhar hai ji ye surthreedots yethreedots ennaya idhu tamil  yek chatur naarthreedots am chhodega nahiin ji  yek chatur naarthreedots am pakadake rakhega ji   ye ghusat jaat  ham marat jaat are aa aa aa   tuu kya jane kya hai nari  jis tan laage more naina  usape sari duniya vari   mah nach na jaane angan tedha  teeedha tedha tedha tedha tedha  4 naach na jaane aangan tedha tedha tedha tedha tedha  4 us sang lage more naina  abake jo avaz lagai  ki o tedhe  mah oy  ki o kede  mah o ya  ki are sidhe ho jaa re  sidhe ho jaa re  sidhe ho jaa  vah ri chandaniya vah re chakore  ram banai ye kaisii jodi  kare nachaya ta ta thaiyya  tal pe naache langadi ghodi  are dekhi  are dekhi teri chaturai  mah ye phir gadabad ki are dekhi teri chaturaai mah phir bhatakaya  ki tujhe suron ki samajh nahiin aai tune kori ghas hi khai  are ghode  mah ye ghoda bola  ki o nigode  mah ye gaali diya  ki are dekhi teri chaturai mah yek chatur naarthreedots ki ghode dekhi teri chaturai mah yek chatur naarthreedots ki ghode dekhi teri chaturai mah yek chatur naarthreedots ki ek chatur naarthreedots ki ek chatur naarthreedots mah ayyo ghode terithreedots ki are ghode terithreedots mah kya re ye ghodachatur ghodachatur bola  yek pe rahana ya ghoda bolo ya chatur bolothreedots gaao  ki ek chatur naar badi hoshiyaar  apane hi jaal men phasat jaat  ek chatur naar tune becomes faster here  badi hoshiyari  ye ghusat jaat  mah ham marat jaat marat jaat mahmood gets stuck  ye atak gayaa    ki sa re ga ma pa he aa aathreedots he threedots threedots ', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'ek chatur naar kar ke singaar', 'year': '1968'}`
- output: `{"pred": "a r rahman", "top3": ["a r rahman", "kalyanjianandji", "s d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='a r rahman' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='r d burman' in top3=['a r rahman', 'kalyanjianandji', 's d burman']

### #8 — FAIL

- item: `{'lyrics': ' ye raat ye chaandanii phir kahaan sun jaa dil kii daastaan chaandanii raaten pyaar kii baaten kho gayii jaane kahaan ye raat ye chaandanii phir kahaan sun jaa dil kii daastaan  aatii hai sadaa terii tuute hue taaron se aahat terii sunatii huun khaamosh nazaaron se bhiigii havaa umadii ghataa kahatii hai terii kahaanii tere liye bechain hai sholon me lipatii javaanii siine me bal khaa rahaa hai dhuaan sun jaa dil kii daastaan ye raat ye chaandanii phir kahaan sun jaa dil kii daastaan  laharon ke labon par hain khoye hue afasaane gulazaar ummiidon ke sab kho gaye viiraane teraa pataa paauun kahaan suune hain saare thikaane jaane kahaan gum ho gaye jaake vo agale zamaane barabaad hai aarazuu kaa jahaan sun jaa dil kii daastaan daastaan daastaan daastaan', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'ye raat ye chaandanii phir kahaan sun jaa dil kii lata version', 'year': '-1'}`
- output: `{"pred": "madan mohan", "top3": ["madan mohan", "r d burman", "s d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='madan mohan' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='s d burman' in top3=['madan mohan', 'r d burman', 's d burman']

### #9 — FAIL

- item: `{'lyrics': '  hamen kyaa pataa thaa  ki dil kii kalii ko masal denge vo hamen kyaa pataa thaa ki raahat ko gam men badal denge vo muhabbat ke vaade aur jhuuthii khaa qasamen kisii aur ke hoke chal denge vo  maar kataarii mar jaanaa maar kataarii mar jaanaa re ankhiyaan kisii se milaanaa naa ho milaanaa naa 2 khaa ke zahar mar jaanaa re man men kisii ko basaanaa naa ho basaanaa naa  haay duniyaa kii koii bhii chiiz ab bhaatii nahiin chain ab aataa nahiin hai niind ab aatii nahiin jinako aanaa thaa na aaye jaane vaale jaa chuke haay  dil ko jaanaa thaa gayaa par jaan kyon jaatii nahiin piichhe pade hai pachhataanaa piichhe pade hai pachhataanaa tuu apanaa kisii ko banaanaa naa ho banaanaa naa 2 maar kataarii mar jaanaa threedots  kyon in aankhon ne unakaa ab tak intazaar kiyaa kyon is bhole dil ne un par baarbaar aitabaar kiyaa jo yahii mohabat kaa badalaa mujhako milane waalaa thaa haay  kyon duniyaa ke taane sahake mainne unase pyaar kiyaa sunake hansegaa zamaanaa  sunake hansegaa zamaanaa  dukh apanaa kisii ko sunaanaa naa ho sunaanaa naa 2 maar kataarii mar jaanaa threedots ', 'correct_label': 'c ramchandra', 'label': 2, 'split': 'test', 'title': 'maar kataarii mar jaanaa', 'year': '1947'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "naushad", "kalyanjianandji"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='shankarjaikishan' ref='c ramchandra'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='c ramchandra' in top3=['shankarjaikishan', 'naushad', 'kalyanjianandji']

### #10 — FAIL

- item: `{'lyrics': '  pn  o mriganayanii chandramukhii 2        main huun teraa prem diivaanaa  ku   o sun rasiyaa man basiyaa mere2        mujhe tuu bhool na jaanaa pn   mriganayanii chandramukhii  pn  jab jab mere nainon se ulajhe       madbhare tere nainaa       tab tab nain men mahak uthe        vo pahalii suhaag kii rainaa        mriganayanii chandramukhii  ku   armaan yahii hai haathon se tere       paan sada main khaauun re       terii baahon men saans luun main       charanon men mar jaauun re  pn  o jaan merii phir aisii kabhii       baat zubaan pe naa laanaa       saath jiyen hain saath marenge       gaate gaate gaanaa                mriganayanii chandramukhii ', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'mriganayanii chandramukhii', 'year': '1983'}`
- output: `{"pred": "annu malik", "top3": ["annu malik", "a r rahman", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='annu malik' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='r d burman' in top3=['annu malik', 'a r rahman', 'laxmikantpyarelal']

### #11 — FAIL

- item: `{'lyrics': '  la ghar aayaa mahamaan koii jaan na pahachaan bane baalamaa o badaa zaalamaa ho badaa zaalamaa  ko o ghar aayaa mehamaan ghar aayaa mahamaan koii jaan na pahachaan bane baalamaa o badaa zaalamaa ho badaa zaalamaa  la pahale nainan men phir man men aayaa chaandanii mere jiivan men laayaa ho ko pahale nainan men phir man men aayaa ho chaandanii mere jiivan men laayaa ho la o o chandaa kii khidakii se dekhe jo ghuur khadaa duur jiyaa chuur ko hoy chandaa kii khidakii se dekhe jo ghuur khadaa duur jiyaa chuur la mohe chhede har aan  kare maan beimaan bane baalamaa o badaa zaalamaa ho badaa zaalamaa  la o kare natakhat ishaaron men batiyaan 2 jiyaa dhadake moraa 2 phadake ankhiyaan ko o phadake ankhiyaan la o o phadake ankhiyaan ho ko kare natakhat ishaaron men batiyaan ho jiyaa dhadake moraa phadake ankhiyaan la o o laage naa manavaa pe birahaa kaa tiir bahe niir uthe piir ko hoy laage naa manavaa pe birahaa kaa tiir bahe niir uthe piir la kahiin jaaye naa jaan main naadaan huun anajaan bane baalamaa o badaa zaalamaa ho badaa zaalamaa  ko o ghar aayaa mehamaan ghar aayaa mahamaan koii jaan na pahachaan bane baalamaa o badaa zaalamaa ho badaa zaalamaa ', 'correct_label': 'naushad', 'label': 6, 'split': 'test', 'title': 'ghar aayaa mahamaan koii jaan na pahachaan bane baalamaa', 'year': '1955'}`
- output: `{"pred": "c ramchandra", "top3": ["c ramchandra", "naushad", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='c ramchandra' ref='naushad'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='naushad' in top3=['c ramchandra', 'naushad', 'laxmikantpyarelal']

### #12 — FAIL

- item: `{'lyrics': '     phir machaa do tum dhuu  aa  rozaanaa zamaanaa paracham apanaa laharaaegaa ye maidaan hamaaraa duujaa finish ho jaayegaa  ham tham ke tez chalenge chupchup phir chakamaa denge dang ho ke sab dekhenge jam ke baazii khelenge hain itane ham hasiin us pe tum haa haa haa  rozaanaa zamaanaa paracham apanaa laharaaegaa   khat khat khat 4 oo yaa  bhanware jaise udate phirate matakmatak ke jhatakjhatak ke yahaan se nikale vahaan pe lapake aise hii laharaanaa hai  phuulon ke hii jaise ham mahakenge juganuu jaise chamcham ham chamakenge  ham tham ke tez chalenge chupchup phir chakamaa denge dang ho ke sab dekhenge jam ke baazii khelenge hain itane ham hasiin aur ek tum haa haa haa  rozaanaa zamaanaa paracham apanaa laharaaegaa ye maidaan hamaaraa duujaa finish ho jaayegaa   aa aa   jhonkaa aayaa tuufaan laayaa thirakthirak ke saraksarak ke ise jitaayaa use haraayaa shorsharaabaa aaj yahaan  ee haa  taaron se bhii aage ham chal denge chandaa se bhii zyaadaa ham chamakenge  ham tham ke tez chalenge chupchup phir chakamaa denge dang ho ke sab dekhenge jam ke baazii khelenge hain itane ham hasiin aur ek tum haa haa haa  rozaanaa zamaanaa paracham apanaa laharaaegaa ye maidaan hamaaraa duujaa finish ho jaayegaa     ', 'correct_label': 'a r rahman', 'label': 0, 'split': 'test', 'title': 'rozaanaa zamaanaa paracham apanaa laharaaegaa', 'year': '2004'}`
- output: `{"pred": "s d burman", "top3": ["s d burman", "a r rahman", "r d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='s d burman' ref='a r rahman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='a r rahman' in top3=['s d burman', 'a r rahman', 'r d burman']

### #13 — FAIL

- item: `{'lyrics': '  agar dilabar kii rusvaaii hamen manzuur ho jaaye sanam tuu bevafaa ke naam se mashhuur ho jaaye  2 agar dilbar kii threedots ho jaaye sanam threedots ho jaaye  hamen fursat nahiin milatii  2 kabhii aansuu bahaane se kaii gam paas aa baithe 2 tere ek duur jaane se  2 agar tuu paas aa jaaye to har gam duur ho jaaye  2 sanam tuu threedots ho jaaye  vafaa kaa vaastaa dekar  2 mohabbat aaj rotii hai na aise khel is dil se  2 ye nazuk chiiz hotii hai  2 zaraa sii thes lag jaaye to shiishaa chuur ho jaaye 2 sanam tuu threedots ho jaaye  tere rangiin honthon ko  2 kamal kahane se darate hain terii is berukii pe ham  2 gazal kahane se darate hain  2 kahiin aisaa na ho tuu aur bhii magaruur ho jaaye  2  agar dilbar ki three dots ho jaaye sanam tuu threedots ho jaaye ', 'correct_label': 'laxmikantpyarelal', 'label': 4, 'split': 'test', 'title': 'agar dilabar kii rusvaaii hamen manzuur ho jaaye', 'year': '1970'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "s d burman", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='r d burman' ref='laxmikantpyarelal'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='laxmikantpyarelal' in top3=['r d burman', 's d burman', 'laxmikantpyarelal']

### #14 — FAIL

- item: `{'lyrics': ' oo oo oo kaabul se aayaa hai meraa diladaar dilabar yaar dilabar yaar dilabar yaar kitane dinon ke baad karuungii aaj main us se pyaar yaar   threedots  ko dilabar yaar dilabar yaar dilabar yaar  threedots  kaabul se aayaa hai meraa diladaar  threedots  aaj savere merii chhat pe kaalaa kauvaa bolaa thaa aayegaa mahamaan koii dhak se dil meraa dolaa thaa kaajal daalaa jhaanjhar baandhii ho gayii main taiyaar yaar  threedots  ko dilabar yaar dilabar yaar dilabar yaar  threedots  kaabul se aayaa hai meraa diladaar  threedots  hay daravaaze pe dastak deke usane meraa naam liyaa main ne jhaankaa khidakii se to usane baazuu thaam liyaa karanaa chaahaa to bhii kar na paayii main inkaar yaar  threedots  ko dilabar yaar dilabar yaar dilabar yaar  threedots  kaabul se aayaa hai meraa diladaar  threedots  bulabul aayaa batuaa laayaa batue mein the paise bhii paise mujhako kyaa karane the main to khush thii vaise bhii are mar gayii karate karate main zaalim ka intazaar yaar  threedots  ko dilabar yaar dilabar yaar dilabar yaar  threedots  kaabul se aayaa hai meraa diladaar', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'kaabul se aayaa meraa diladaar', 'year': '1986'}`
- output: `{"pred": "kalyanjianandji", "top3": ["kalyanjianandji", "r d burman", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='kalyanjianandji' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='r d burman' in top3=['kalyanjianandji', 'r d burman', 'laxmikantpyarelal']

### #15 — FAIL

- item: `{'lyrics': ' lapak japak tuu aa re badaravaa sar kii khetii suukh rahii hai baras baras tuu aa re badaravaa  jhagad jhagad kar paanii laa tuu akad akad  bijalii chamakaa tuu tere ghade men paanii nahiin to panaghat se bhar laa re badaravaa   threedots  ban men koyal kuuk uthii hai sab ke man men huuk uthii hai bhuudal se tuu baal ugaa de jhat pat tuu barasaa re badaravaa   threedots     ', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'lapak jhapak tuu aa re badaravaa', 'year': '1954'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "laxmikantpyarelal", "s d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='r d burman' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='shankarjaikishan' in top3=['r d burman', 'laxmikantpyarelal', 's d burman']

### #16 — PASS

- item: `{'lyrics': ' jogiyaa jogiyaa ve jogiyaa jogiyaa jogiyaa ve  jogiyaa jogiyaa ve mere sone jogiyaa jogiyaa ve saarii duniyaa chhod ke he he he he  saarii duniyaa chhod ke tere pyaar kaa jog liyaa  jogiyaa jogiyaa aa aa aa aa jogiyaa jogiyaa jogiyaa jogiyaa haa haa haa haa jogiyaa jogiyaa   tere havaale kar diyaa maine saaraa jiivan apanaa  saaraa jiivan apanaa ho jaagiijaagii aankhon se bhii dekhuun teraa sapanaa  dekhuun teraa sapanaa ho udate baadal bahate paanii udate baadal bahate paanii jaisii merii kahaanii jaisii merii kahaanii  teraa meraa sangam ho nahiin sakataa premdiivaanii  tere naam kii maalaa japataa ab meraa jiyaa   koyal bolii sarason phuulii mahak uthii puravaaii  mahak uthii puravaaii chaaron dishaaon men chaahat kii bajane lagii shahanaaii  bajane lagii shahanaaii suuniisuunii maang men sinduurii rang hai sajaanaa  sinduurii rang hai sajaanaa aazaadii kii dulhan se hai mujh ko byaah rachaanaa  mainne bhii tanman se tujhe maanaa meraa piyaa ', 'correct_label': 'a r rahman', 'label': 0, 'split': 'test', 'title': 'jogiyaa jogiyaa ve', 'year': '2002'}`
- output: `{"pred": "a r rahman", "top3": ["a r rahman", "s d burman", "r d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='a r rahman' ref='a r rahman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='a r rahman' in top3=['a r rahman', 's d burman', 'r d burman']

### #17 — FAIL

- item: `{'lyrics': ' yaa alii  aate jaate hue main sab pe nazar rakhataa huun 2  naam abdul hai meraa kyaa  ho naam abdul hai meraa sab kii kabar rakhataa huun 2 2  kisane liyaa kisane diyaa kisane kahaan maal chhupaa rakhaa hai  main ne is dil men saarii duniyaa kaa haal chhupaa rakhaa hai 2 bol sakataa huun zubaan band magar rakhataa huun 2 naam abdul hai meraa threedots  sar kisiike saamane jhuk jaae meraa ye mujhe manzuur nahiin  aa pade vaqt to maut aae sahii par main majabuur nahiin 2 jaan par khel jaauun main vo jigar rakhataa huun 2 naam abdul hai meraa threedots', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'aate jaate hue main sab pe nazar rakhataa huun naam abdul hai', 'year': '1980'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "laxmikantpyarelal", "annu malik"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='shankarjaikishan' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='r d burman' in top3=['shankarjaikishan', 'laxmikantpyarelal', 'annu malik']

### #18 — FAIL

- item: `{'lyrics': ' thodaathodaa pyaar ho gayaa tumase thodaathodaa pyaar ho gayaa   dil beqaraar ho gayaa milane ko dil beqaraar ho gayaa  pyaar kii shabanam baras rahii hai tujh par jhuume man meraa 2  thodaathodaa pyaar ho gayaa tumase thodaathodaa pyaar ho gayaa   yahii hai vo bhuumii yahii hai vo nadiyaa jahaan ham mile the leke pahalaapahalaa pyaar  dilabarajaanii dil men basaa hai kitane janam se teraameraa pyaar  goregore gaalon ko chhuune de sajanii dil meraa apane hii bas men nahiin hai  dil beqaraar ho gayaa tumase thodaathodaa pyaar ho gayaa pyaar kii shabanam baras rahii hai tujh par jhuume man meraa thodaathodaa pyaar ho gayaa tumase thodaathodaa pyaar ho gayaa  sapanon men tumase milatemilate teraa divaanaa ho gayaa main  bachapan biitaa yaad men terii satarah baras kii ho gaii main  man men mastii hai saansen bahakii hain mere bhii dil kii kaliyaan mahakii hain  dil beqaraar ho gayaa balamaa thodaathodaa pyaar ho gayaa pyaar kii shabanam baras rahii hai tujh par jhuume man meraa thodaathodaa pyaar ho gayaa tumase thodaathodaa pyaar ho gayaa ', 'correct_label': 'a r rahman', 'label': 0, 'split': 'test', 'title': 'thodaathodaa pyaar ho gayaa tumase', 'year': '1995'}`
- output: `{"pred": "madan mohan", "top3": ["madan mohan", "a r rahman", "c ramchandra"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='madan mohan' ref='a r rahman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='a r rahman' in top3=['madan mohan', 'a r rahman', 'c ramchandra']

### #19 — FAIL

- item: `{'lyrics': '  mu \tnaach hasiinaa naach ki duniyaa dekhe \tthumakthumak ke naach ki duniyaa dekhe \ttere ishaaron pe naache zamaanaa \ttuu mere ishaaron pe naach ki duniyaa dekhe \tnaach hasiinaa naach threedots  \tinkaar kii gunjaaish nahiin 2 \ttakaraar kii gunjaaish nahiin \tab maan jaa bas jaan jaa merii nazaren pahachaan jaa \tjhuum hasiinaa jhuum ki duniyaa dekhe \tnaach hasiinaa naach threedots  raa \tla la laa  mu \tmastii men tuu madahosh hai 2 \tpar kisalie tuu kaamosh hai \tlaharaa ke balakhaa ke ghabaraa ke sharamaa ke \tbol hasiinaa bol ki duniyaa dekhe \tnaach hasiinaa naach threedots ', 'correct_label': 'laxmikantpyarelal', 'label': 4, 'split': 'test', 'title': 'naach hasiinaa naach ki duniyaa dekhe', 'year': '1972'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "naushad", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='shankarjaikishan' ref='laxmikantpyarelal'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='laxmikantpyarelal' in top3=['shankarjaikishan', 'naushad', 'laxmikantpyarelal']

### #20 — FAIL

- item: `{'lyrics': '   koii hai aashiq koii mahabuub hai yah duniyaa kuub hai 2  kahiin pe romiyojuuliyat kahiin raanjhaa kahiin hiir kahiin shiiriifarahaad ye naam sabako hai yaad sabake bahaane dil se manasuub hain yah duniyaa kuub hai threedots  kitane hain mausam lekin yah rut hai ek suhaanii barason kii zindagaanii men do din kii hai javaanii aur ye javaanii dil se manasuub hai yah duniyaa kuub hai threedots ', 'correct_label': 'laxmikantpyarelal', 'label': 4, 'split': 'test', 'title': 'i am in love  koii hai aashiq koii mahabuub hai', 'year': '1977'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "laxmikantpyarelal", "kalyanjianandji"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='r d burman' ref='laxmikantpyarelal'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='laxmikantpyarelal' in top3=['r d burman', 'laxmikantpyarelal', 'kalyanjianandji']

### #21 — FAIL

- item: `{'lyrics': ' kaarii kaarii kaarii andhiyaarii thii raat ek din kii baat jab sajan gagan se garaj uthii saavan kii ghataa ghuunghat men chhupakar chapalchapal bijalii kii chattaa ek naar karat shringaar ek naar tihike talvaar yathii vah kataar karake shringaar chalii us paar jahaan the usake kisan muraar chhamak chhamchham jamak jamjam chhamak chhamchham', 'correct_label': 'c ramchandra', 'label': 2, 'split': 'test', 'title': 'kaarii kaarii kaarii andhiyaarii', 'year': '-1'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "s d burman", "r d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='shankarjaikishan' ref='c ramchandra'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='c ramchandra' in top3=['shankarjaikishan', 's d burman', 'r d burman']

### #22 — FAIL

- item: `{'lyrics': '  are diivaanon mujhe pahachaanon kahaan se aayaa main huun kaun 2  main huun kaun  2  main huun  4 kaun  main huun don  2  main huun  4 don  are tumane jo dekhaa hai sochaa hai samajhaa hai jaanaa hai  vo main nahiin  2 logon kii nazaron ne mujhako yahaan jo bhii maanaa hai  vo main nahiin  2 aavaaraa baadal ko saudaaii paagaal ko duniyaa men samajhaa hai kaun are diivaanon threedots  are yaaron kaa vo yaar huun yaarii men jaan lutaa de jo  main huun vahii  2 dushman kaa dushman huun vo dushman ke chhakke chhudaa de jo  main huun vahii  2 tum jaano naa jaano maine to jaanaa hai mahafil men kaisaa hai kaun are diivaanon threedots  are maine kyaa sochaa hai kyaa kvaab hai merii aankhon men  tum jaano naa  2 maine bhii badalaa hai kyaa rang baaton hii baaton men  tum jaano naa  2 chehare pe cheharaa hai parade pe paradaa hai duniyaa men samajhaa hai kaun are diivaanon threedots ', 'correct_label': 'kalyanjianandji', 'label': 3, 'split': 'test', 'title': 'are diivaanon mujhe pahachaanon  main huun don', 'year': '1978'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "kalyanjianandji", "annu malik"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='r d burman' ref='kalyanjianandji'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='kalyanjianandji' in top3=['r d burman', 'kalyanjianandji', 'annu malik']

### #23 — FAIL

- item: `{'lyrics': '  la \ttumhen main agar apanaa saathii banaa luun \tbataa do saath doge kahaan tak ra \tzamiin se jahaan aasamaan mil rahaa hai \tna chhodenge daaman tumhaaraa vahaan tak  la \tyahaan har qadam par naii dilaqashii hai \tkahaan tak tumhaaraa bharosaa karuun main ra \tduaa hai ke benuur ho jaaen aankhen \tkisii aur kii jo tamannaa karuun main  la \tsalaamat hain jab tak ye zulfon ke saae \tto phir aur kisakaa aramaan hogaa ra \ttumhaare hii qadamon men maranaa huaa \tto ye maranaa kitanaa aasaan hogaa ', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'tumhen main agar apanaa saathii banaa luun', 'year': '1969'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "madan mohan", "kalyanjianandji"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='r d burman' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='shankarjaikishan' in top3=['r d burman', 'madan mohan', 'kalyanjianandji']

### #24 — PASS

- item: `{'lyrics': '  ham ko to jaan se pyaarii hain tumhaarii aankhen haay kaajal bharii madahosh ye pyaarii aankhen  mast aankhen hain ke gaate hue mayakhaane hain mast aankhen hain ke chhalke hue paimaane hain hamane dekhii nahiin aisii to kanvaarii aankhen haay kaajal bharii madahosh ye pyaarii aankhen ham ko to jaan se threedots  roshanii chaand men suuraj men hain jab tak kaayam jyot roshan rahe aankhon men tumhaarii har dam ye duaa hai ki salaamat rahe pyaarii aankhen haay kaajal bharii madahosh ye pyaarii aankhen ham ko to jaan se threedots ', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'ham ko to jaan se pyaarii hain tumhaarii aankhen', 'year': '1973'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "laxmikantpyarelal", "kalyanjianandji"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='shankarjaikishan' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='shankarjaikishan' in top3=['shankarjaikishan', 'laxmikantpyarelal', 'kalyanjianandji']

### #25 — FAIL

- item: `{'lyrics': ' aa \tdaag na lag jaaye haay \tkahiin daag na lag jaaye haay \tpyaar kiyaa to kar ke nibhaanaa 2 \tdaag na lag jaaye haan \tkahiin daag na lag jaaye haay mu \tgore tan se chamake bijariyaa 2 \taag na lag jaaye haan \tkahiin aag na lag jaaye  aa \tsochsamajh kar paanv badhaanaa \tmanzil ke diivaane \taag ko chhuunaa khel nahiin hai 2 \to paagal parawaane \tshole kii baanhon men \tbaanhon men \tshole kii baanhon men \taa mat jaanaa mu \tkyuun aa \tdaag na lag jaaye haan \tkahiin daag na lag jaaye haan \tkahiin daag na lag jaaye  mu \tmaine hameshaa sadamen uthaaye \tjis se bhii dil ko lagaayaa \tjab bhii hansaa main sabako hansaane 2 \taankhon men aansuu aayaa \tdil ke jale ko haan haan \tdil ke jale to tum naa jalaanaa aa \tkyuun mu \taag na lag jaaye \tkahiin aag na lag jaaye haan \tkahiin aag na lag jaaye  aa \tkahiin daag na lag jaaye haay \tkahiin daag na lag jaaye \tpyaar kiyaa to kar ke nibhaanaa 2 \taag na lag jaaye haay \tkahiin daag na lag jaaye mu \tgore tan se chamake bijariyaa 2 \taag na lag jaaye aa \thaan mu \tkahiin aag na lag jaaye aa \thaan mu \tkahiin aag na lag jaaye aa \tdekho daag na lag jaaye ', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'daag na lag jaaye', 'year': '1970'}`
- output: `{"pred": "s d burman", "top3": ["s d burman", "madan mohan", "r d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='s d burman' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='shankarjaikishan' in top3=['s d burman', 'madan mohan', 'r d burman']

### #26 — FAIL

- item: `{'lyrics': ' chale chalo prem ke saathii prem nagar hai jaanaa raah pe laanaa priit kii chaayaa prem kii paas  basaanaa chale chalo prem ke saathii  koyal pyaarii prem se bolii bolii bolii koyal pyaarii prem se bolii phuul kii kaliyaan sukh se dole dole phuul kii kaliyaan sukh se dole phuul kaa saathii aayaa bhanvaraa gaayaa prem taraanaa 2 chale chalo prem ke saathii  raah  sa chaand banaayaa 2 premiyon kaa man lalachaaya taare saarii mil hua jab 2 dil kii bedh chadaanaa 2 chale chalo prem ke saathii', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'chale chalo prem ke saathii prem nagar hai jaanaa', 'year': '-1'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "s d burman", "c ramchandra"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='s d burman' in top3=['laxmikantpyarelal', 's d burman', 'c ramchandra']

### #27 — FAIL

- item: `{'lyrics': '  jabjab tumhen bhulaayaa tum aur yaad aae  jabjab tumhen bhulaayaa haan tum aur yaad aae tum aur yaad aae  2 jaate nahiin hain dil se ab tak tumhaare saae 2 jaate nahiin hain dil se haan ab tak tumhaare saae jabjab tumhen bhulaayaa threedots  tumase bichhad ke hamane dil ko bahut sambhaalaa 4 dil ko bahut sambhaalaa gulashan men ye na bahalaa aa gulashan men ye na bahalaa saharaa men bhii sataae tum aur yaad aae jabjab tumhen bhulaayaa threedots  marane kii aarazuu men ham jii rahe hain aise 2 marane kii aarazuu men ho ham jii rahe hain aise 2 ham jii rahe hain aise jaise kii laash apanii khud hii koii uthaae tum aur yaad aae jabjab tumhen bhulaayaa threedots ', 'correct_label': 'madan mohan', 'label': 5, 'split': 'test', 'title': 'jabjab tumhen bhulaayaa tum aur yaad aae', 'year': '1964'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "kalyanjianandji", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='shankarjaikishan' ref='madan mohan'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='madan mohan' in top3=['shankarjaikishan', 'kalyanjianandji', 'laxmikantpyarelal']

### #28 — PASS

- item: `{'lyrics': '  le lo le lo sapanon kaa saudaagar aayaa le lo ye sapane le lo  tumase qismat khel chukii tum qismat se khelo ab tum qismat se khelo  ye rangbirange sapane ye jiivan ke ujiyaare ye tanahaaii ke saathii ye bhiid men sangsahaare ye chaand aur suuraj apane ye andhii raat ke taare 2 sapanon kaa saudaagar threedots  ik chhaliyaa aas ke piichhe daude to yahaan tak aaye har shaam ko dhalataa suuraj jaatejaate kah jaae vo tay kar letaa manzil jo ik sapanaa apanaae 2 sapanon kaa saudaagar threedots ', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'le lo le lo sapanon kaa saudaagar aayaa', 'year': '1968'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "s d burman", "madan mohan"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='shankarjaikishan' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='shankarjaikishan' in top3=['shankarjaikishan', 's d burman', 'madan mohan']

### #29 — FAIL

- item: `{'lyrics': ' o basanti pavan pagal na ja re na ja roko koi o basanti threedots  ban ke patthar ham pade the suni suni rah men ji uthe ham jab se teri banh ai banh men bah uthe nainon ke kajal na ja re na ja roko koi o basanti threedots  yad kar tune kaha tha pyar se sansar hai ham jo hare dil ki baji ye teri hi har hai sun ye kya kahati hai payal na ja re na ja roko koi o basanti threedots', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'o basantii pavan paagal naa jaa re naa jaa roko koii', 'year': '1960'}`
- output: `{"pred": "s d burman", "top3": ["s d burman", "laxmikantpyarelal", "madan mohan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='s d burman' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='shankarjaikishan' in top3=['s d burman', 'laxmikantpyarelal', 'madan mohan']

### #30 — PASS

- item: `{'lyrics': ' tere binaa suunii suunii hai merii phulawaarii re aajaa meraa bhanwaraa shikaarii  jaatii rahiin raaten aur aate rahe din aas liye baithii rahii ek abhaagin aaii hai bahaar magar suukh rahii kyaarii re  mere janam ke saathii terii priit rulaatii sahatii rahii dukh baraabar aur sahuungii par akele tere binaa kaise rahuungii terii judaaii men bane aansuu bhii chingaarii re', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'tere binaa suunii suunii hai merii phulawaarii re', 'year': '1946'}`
- output: `{"pred": "s d burman", "top3": ["s d burman", "c ramchandra", "r d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='s d burman' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='s d burman' in top3=['s d burman', 'c ramchandra', 'r d burman']

### #31 — PASS

- item: `{'lyrics': ' jaanaan jaanaan jaanaan jaanaan   dekhaa nahiin hai tujhe kal se palpal kate meraa mushkil se   aa puuchh le zaraa is dil se jaanaan   raahon ko main terii takataa huun jiijii ke main yahaan marataa huun   main pyaar bas tujhe karataa huun jaanaan jaanaan   samajhaaun kaise main is dil ko jaanaan ye maane naa jaanaan ye samajhe naa   palpal kate meraa mushkil se aa puuchh le zaraa is dil se jaanaan   ik pal bhii lagataa hai ik saal jaisaa tere binaa o jaanejaan   tuu saath naa ho mere ik saal ik pal lagane lagegaa jaanaan   tuu jhuuth bhii kah de hai pyaar tujhako mil jaayegii saarii duniyaa ye mujhako   main ban gayaa huun diivaanaa   dekhaa nahiin hai tujhe kal se palpal kate meraa mushkil se  aa puuchh le zaraa is dil se jaanaan  raahon ko main terii takataa huun jiijii ke main yahaan marataa huun  main pyaar bas tujhe karataa huun jaanaan jaanaan   tuu jo nahiin hai to lagataa hai aise kuchh bhii nahiin hai ye jahaan   mil ke judaa na hon ek baar aise mujhako merii jaan mil jaanaan   dekhuun to main dekhuun tujhako hii jaanam sochuun to main sochuun tujhako hii jaanam   mar jaaungaa tere binaa   dekhaa nahiin hai tujhe kal se palpal kate meraa mushkil se  aa puuchh le zaraa is dil se jaanaan  raahon ko main terii takataa huun jiijii ke main yahaan marataa huun  main pyaar bas tujhe karataa huun jaanaan jaanaan  samajhaaun kaise main is dil ko jaanaan ye maane naa jaanaan ye samajhe naa   dekhaa nahiin hai tujhe kal se palpal kate meraa mushkil se  aa puuchh le zaraa is dil se jaanaan ', 'correct_label': 'a r rahman', 'label': 0, 'split': 'test', 'title': 'jaanaan jaanaan dekhaa nahiin hai tujhe kal se', 'year': '1996'}`
- output: `{"pred": "a r rahman", "top3": ["a r rahman", "r d burman", "annu malik"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='a r rahman' ref='a r rahman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='a r rahman' in top3=['a r rahman', 'r d burman', 'annu malik']

### #32 — FAIL

- item: `{'lyrics': ' he aaj nahiin to kal aaoge tum idhar kahoge mujhas pyaar kar kahuungii jaa udhar main dil naa tumako duungii tumase ye kahuungii kanvaarii hii rahuungii  o diivaanii gulabadan kar na diivaanaapan aur bhii hain dilarubaa kahiin bhii dil lagaa main dil naa tumako duungaa tumase ye kahuungaa kanvaaraa hii rahuungaa aaj nahiin to kal threedots  mud ke dekh to idhar jaa re jaa jaa udhar dil se dil kii baat kar chup bhii kar baith udhar kyon khafaa hai is kadar khaa gaii meraa sar dekh main to ro paduungii haan haan are re mere piichhe kyon padii tujhape main mar mitii he raah roke kyon khadii paas aa do ghadii lagatii kyaa hai tuu merii tuu merii zindagii itanaa pyaar na jataa re jaa aaj nahiin to kal threedots  he chaahatii huun main tujhe ye mujhe pataa hai pyaar kar tuu mujhe ye bharam hai teraa chhoduungii naa main tujhe zid naa kar maan jaa bin tere naa jii sakuungii haan haan haan he rog dil ko na lagaa rog to lag chukaa ishq ye hai balaa hai balaa to bhii kyaa main akelaa hii bhalaa meraa phir hogaa kyaa teraa jo bhii hogaa jaa jaa he aaj nahiin to kal threedots ', 'correct_label': 'annu malik', 'label': 1, 'split': 'test', 'title': 'aaj nahiin to kal aaoge tum idhar', 'year': '1988'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "annu malik", "naushad"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='r d burman' ref='annu malik'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='annu malik' in top3=['r d burman', 'annu malik', 'naushad']

### #33 — FAIL

- item: `{'lyrics': '  aa \tni sa ga ma ni dha pa ma ga re sa \tni sa ga ma ni dha pa \tpiyaa baanwarii piyaa baanwarii \tpiyaa baanwarii piyaa baanwarii \tpii kahaan pii kahaan \tpiyaa piyaa bole re \tpiyaa baanwarii piyaa baanwarii \tpiyaa baanwarii  asho \ttaa dhik taa taa dhik taa \ttaa tik taa taa dhik taa \tthirakat nandan ban chhum chhananana \ttachhum tachhum tak tiinaa tirakat dhaa \tliye mang sab sakhaa sang \tman men umang rachit swang thaa \tkhelat bhuj melat lapatjhapat \traadhaa lalitaa chandraa \tbali diye bor rang bhor sar bhor \tbanawaarii \tmain haarii jaajaa rii 3  aa \taa \tdaardaar piyaa phuulon kii chaadar bunii \tphuulon kii chaadar rangon kii jhaalar bunii \to  \tdaardaar piyaa phuulon kii chaadar bunii \tphuulon kii chaadar rangon kii jhaalar bunii \tbhaii baanwarii huii baanwarii \tbaanwarii haan haan  \tpiyaa baanwarii piyaa baanwarii \tpiyaa baanwarii piyaa baanwarii \tpii kahaan pii kahaan \tdhi ni ma re pa ma ga \tpiyaa baanwarii piyaa baanwarii \tpiyaa baanwarii  \taa aa aa  \tkaalekaale piyaa saawan ke baadal chune \tbaadal chun ke aankhon men kaajal ghule \to \tkaalekaale piyaa saawan ke baadal chune \tbaadal chun ke aankhon men kaajal ghule \thuii baanwarii huii saanwarii \thuun huun huun  \tpiyaa baanwarii piyaa baanwarii \tpiyaa baanwarii piyaa baanwarii \tpii kahaan pii kahaan \tpiyaa piyaa bole re \tpiyaa baanwarii piyaa baanwarii \tpiyaa baanwarii piyaa baanwarii \tpiyaa baanwarii ', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'piyaa baanwarii piyaa baanwarii pii kahaan pii kahaan', 'year': '1980'}`
- output: `{"pred": "a r rahman", "top3": ["a r rahman", "s d burman", "c ramchandra"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='a r rahman' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='r d burman' in top3=['a r rahman', 's d burman', 'c ramchandra']

### #34 — FAIL

- item: `{'lyrics': ' duaa kar gamedil khudaa se duaa kar vafaaon kaa majabuur daaman bichhaa kar duaa kar gamedil khudaa se duaa kar jo bijalii chamakatii hai unake mahal par vo kar le tasallii meraa ghar jalaa kar duaa kar gamedil khudaa se duaa kar\t 2  salaamat rahe tuu merii jaan jaae\t\t 2 mujhe is bahaane se hii maut aae karuungii main kyaa chand saansen bachaa kar duaa kar gamedil khudaa se duaa kar\t 2  main kyaa duun tujhe meraa sab lut chukaa hai  duaa ke sivaa mere paas aur kyaa hai\t\t 2 gariibon kaa ek aasaraaekhudaa hai\t\t 2 magar merii tujhase yahii iltajaa hai na dil todanaa dil kii duniyaa basaa kar  duaa kar gamedil khudaa se duaa kar\t 2 vafaaon kaa majabuur daaman bichhaa kar duaa kar gamedil khudaa se duaa kar         2  ', 'correct_label': 'c ramchandra', 'label': 2, 'split': 'test', 'title': 'duaa kar gamedil khudaa se duaa kar', 'year': '1953'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "kalyanjianandji", "naushad"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='c ramchandra'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='c ramchandra' in top3=['laxmikantpyarelal', 'kalyanjianandji', 'naushad']

### #35 — FAIL

- item: `{'lyrics': ' aaye dil jaanii chiichii vaalaa chhallaa saanuu de jaa nishaanii aankhon men kaajal maathe pe pasiinaa kitanii pyaarii hai merii hasiinaa chorii chorii dekhe tujhe har hasiinaa mar jaauungii jo kisii ne tujhe chhiinaa aankhon men kaajal threedots  tumase izahaar main kar naa paaii pyaar tujhase hii main karatii aaii kyaa kahaa teraa munh chuum luun main baat sun ke naa kyon jhuum luun main o tere gore gore gaal terii moranii sii chaal shor galiyon men terii adaa kaa har savaal kaa javaab teraa cheharaa vo kitaab de rahaa sabak jo vafaa kaa naa dekhuun ik pal bhii to mushkil hai jiinaa mar jaauungii jo threedots  pyaar ke tere do pal bhii paa kar saaraa jiivan main kar duun nyauchhaavar pyaar kii pyaas itanii jagii hai haay kam kitanii ye zindagii hai o tere abaruu hain kamaan jaise kaamadev ke baan tere nainon se koii na bachaa hai mere tan men terii jaan tuu hii jiine kaa aramaan ek tujh men sabhii kuchh milaa hai chal de to hansanii bole to viinaa kitanii pyaarii hai merii hasiinaa mar jaauungii jo threedots ', 'correct_label': 'annu malik', 'label': 1, 'split': 'test', 'title': 'aaye dil jaanii chiichii vaalaa chhallaa  aankhon men kaajal maathe pe pasiinaa', 'year': '1989'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "kalyanjianandji", "annu malik"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='annu malik'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='annu malik' in top3=['laxmikantpyarelal', 'kalyanjianandji', 'annu malik']

### #36 — FAIL

- item: `{'lyrics': '  ma \tmain tere pyaar men kyaa kyaa na banaa dilabar \tjaane ye mausam 2 gii  \tmain ghataa pyaar bharii tuu hai meraa baadal \tjaane ye mausam 2  ma \ttuu hai merii banshii main huun teraa kaanhaa gii  \tteraa meraa pyaar hai sadiyon puraanaa ma \tdil ke har taar men hai raag teraa haradam gii  \tmain ghataa pyaar bharii threedots  ma \ttuu hai merii manzil main huun teraa saahil gii  \tkarake rahenge ik din tujhe haasil ma \tchale tuu hii gorii dil men sadaa chham chham gii  \tmain ghataa pyaar bharii threedots ', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'main tere pyaar men kyaa kyaa na banaa', 'year': '1964'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "kalyanjianandji", "c ramchandra"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='shankarjaikishan' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='s d burman' in top3=['shankarjaikishan', 'kalyanjianandji', 'c ramchandra']

### #37 — FAIL

- item: `{'lyrics': '  diivaanaa mujh saa nahiin is ambar ke niiche 2 aage hai qaatil meraa aur main piichhepiichhe diivaanaa mujh saa threedots  paayaa hai dushman ko jab se pyaar ke qaabil tab se ye aalam hai rastaa yaad na manzil niind men jaise chalataa hai koii chalanaa yuun hii aankhen miinche diivaanaa mujh saa threedots  hamane bhii rakh dii hain kal pe kal kii baaten 2 jiivan kaa haasil hain pal do pal kii baaten do hii ghadii kaa saath rahegaa karanaa kyaa hai tanahaa jii ke diivaanaa mujh saa threedots ', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'diivaanaa mujh saa nahiin is ambar ke niiche', 'year': '1966'}`
- output: `{"pred": "kalyanjianandji", "top3": ["kalyanjianandji", "laxmikantpyarelal", "r d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='kalyanjianandji' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='r d burman' in top3=['kalyanjianandji', 'laxmikantpyarelal', 'r d burman']

### #38 — PASS

- item: `{'lyrics': '  la \taashaaon ke saavan men 2 \tumangon kii bahaar men \ttum mujhako dhuundho main kho jaauun pyaar men ra \taashaaon ke saavan threedots la \taashaaon ke saavan threedots  ra \tsur se ye jiivan sangiit banaa \tterii paayal chhanakii giit banaa 2 la \tchhamchham ghungharuu gaate hain 2 \taaoaao tumhen ham pahanaate hain \tgiit piro ke in saanson ke haar men ra \taashaaon ke saavan threedots  \tjalate angaaron ko chhed gaii \trut man ke taaron ko chhed gaii la \tman men diip jale saragam se \tsaat suron ke is sangam men \tye sapanon ke phuul khile sansaar men \taashaaon ke saavan threedots ', 'correct_label': 'laxmikantpyarelal', 'label': 4, 'split': 'test', 'title': 'aashaaon ke saavan men  main kho jaauun pyaar men', 'year': '1980'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "shankarjaikishan", "naushad"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='laxmikantpyarelal' ref='laxmikantpyarelal'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='laxmikantpyarelal' in top3=['laxmikantpyarelal', 'shankarjaikishan', 'naushad']

### #39 — FAIL

- item: `{'lyrics': ' \tdila ko yuun naa tadapaao \tye iltijaa hai ke \tmuda muda ke dekhate jaao \t \tzaraa dekhate jaanaa \to jaanevaale mudake zaraa dekhate jaanaa \tzaraa dekhate jaanaa \tdila tod ke to chala diye mujhako naa bhulaanaa \tzaraa dekhate jaanaa \t \tfariyaad kar rahi hain khaamosh nigaahen khaamosh nigaahen  2 \taansuu kii taraha aankh se mujhako naa giraanaa \tzaraa dekhate jaanaa \to jaanevaale mudake zaraa dekhate jaanaa \tzaraa dekhate jaanaa  \tqismat ne kahaan aa kar merii baat bigaadii merii baat bigaadii \tmanzil pe aa ke lutaa mere dil kaa kazaanaa \tzaraa dekhate jaanaa \to jaanevaale mudake zaraa dekhate jaanaa \tzaraa dekhate jaanaa ', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'o jaane vaale mud ke zaraa dekhate jaanaa', 'year': '1955'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "s d burman", "naushad"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='r d burman' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='shankarjaikishan' in top3=['r d burman', 's d burman', 'naushad']

### #40 — FAIL

- item: `{'lyrics': ' o o o o o o o o o o 4      zaakir hussain tabalaa tuu hai kyaa  sonaa sonaa teraa chamake ruup salonaa  sonaa sonaa cellular phone tum to ho naa     tum naa hote to dhuup nahiin hotii rimajhim bhii naa hotii  tum naa hote to chaand nahiin hotaa sapanaa bhii nahiin sajataa  tum ko pukaaraa saansen kushbuu phailaa rahiin merii  tumase bichhadaa to bahatii havaayen band ho gaiin kyuun  paanii naa hotaa jharane naa hote ye vaadii naa hotii  milataa naa tuu to merii jaan nahiin hotii ye pyaas nahiin hotii  gori nadiyaa apane men har din mujhako dubaanaa  tum naa sharmaanaa zulfon men apanii kud ko chhupaa lenaa   o o o o o o o o o o 4  naam teraa kisii ko lene nahiin duungaa vo sukh bhii nahiin duungaa  gajaraa tumhaaraa girane nahiin duungaa murajhaane nahiin duungaa  mere alaavaa kisii aurat ko naa paas bulaanaa  tum naa kabhii bhii mother teresa ko chhod ke naam naa lenaa  terii galiyon men koii mard na chhoduungaa aurat bhii naa chhoduungaa  terii hansii ko udane nahiin duungaa mere dil men basaa luungaa   jiivan men priitam tumhen pyaar kii rekhaa paar karane naa duungii  zaakir hussain tabalaa tuu hai kyaa sonaa sonaa teraa chamake ruup salonaa sonaa sonaa cellular phone tum to ho naa ', 'correct_label': 'a r rahman', 'label': 0, 'split': 'test', 'title': 'telephone dhun men hansane vaalii', 'year': '1996'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "annu malik", "a r rahman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='r d burman' ref='a r rahman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='a r rahman' in top3=['r d burman', 'annu malik', 'a r rahman']

### #41 — FAIL

- item: `{'lyrics': '  chhuune na duungii haath re najariyon se dil bhar duungii baithii rahuungii saarii raat re najariyon se dil bhar duungii  dil kii hasarat na kabhii dil se nikalane duungii pyaar kaa koii bhii jaaduu na chalane duungii  ishq kii aag tez hai hamane maanaa dil ke motii ko haragiz na pighalane duungii hotii rahegii mulaakaat re najariyon se dil bhar duungii chhuune na duungii threedots ', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'chhuune na duungii haath re najariyon se dil bhar duungii', 'year': '1964'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "laxmikantpyarelal", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='r d burman' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='shankarjaikishan' in top3=['r d burman', 'laxmikantpyarelal', 'shankarjaikishan']

### #42 — PASS

- item: `{'lyrics': ' lata     iichak daanaa biichak daanaa daane uupar daanaa iichak daanaa           chhajje uupar ladakii naache ladakaa hai diivaanaa iichak daanaa  lata     ek jaanavar aisaa jisake dum par paisaa           sar pe bhii taaj hai baadashaah ke jaisaa           o           baadal dekhe chhamchham naache albelaa masataanaa iichak daana           bolo kyaa bachche  mor           iichak daanaa biichak daanaa   threedots  lata     harii thii man bharii thii laakh motii jadii thii           raajaa jii ke baag men dushaalaa odhe khadii thii           o           kachchepakke baal hain usake mukhadaa hai suhaanaa iichak daanaa           bolo kyaa raaj     buddhii bachche  bhuttaa  lata     chhotii sii chhokarii laalbaaii naam hai           pahane vo ghaagharaa ek paisaa daam hai           o           munh men sabake aag lagaaye aataa hai rulaanaa iichak daanaa           bolo kyaa bolo na bachche  michrii  mukesh   iichak daanaa biichak daanaa daane uupar daanaa iichak daanaa           chhajje uupar ladakii naache ladakaa hai diivaanaa iichak daanaa            chaalen vo chalakar dil men samaayaa           aa hii gayaa vo kiyaa hai safaayaa           tum bhii dekho bachakar rahanaa chakkar men na aanaa iichak daanaa lata     gam raaj     dhat ham ', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'iichak daanaa biichak daanaa', 'year': '1956'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "annu malik", "s d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='shankarjaikishan' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='shankarjaikishan' in top3=['shankarjaikishan', 'annu malik', 's d burman']

### #43 — FAIL

- item: `{'lyrics': '  husn haazir hai muhabbat kii sazaa paane ko koii patthar se na maare mere diivaane ko  mere diivaane ko itanaa na sataao logon ye to vahashii hai tumhiin hosh men aao logon bahut ranjuur hai ye gamon se chuur hai ye kudaa kaa kauf uthaao bahut majabuur hai ye kyon chale aaye ho bebas pe sitam dhaane ko koii patthar se na maare threedots  mere jalavon kii kataa hai jo ye diivaanaa huaa main huun mujarim ye agar hosh se begaanaa huaa mujhe suulii chadhaa do yaa sholon pe jalaa do koii shiqavaa nahiin hai jo jii chaahe sazaa do baksh do is ko main taiyaar huun mit jaane ko koii patthar se na maare threedots  pattharon ko bhii vafaa phuul banaa sakatii hai ye tamaashaa bhii sareaam dikhaa sakatii hai lo ab patthar uthaao zamaane ke kudaaon main tum ko aazamaauun mujhe tum aazamaao ab duaa arsh pe jaatii hai asar laane ko koii patthar se na maare threedots ', 'correct_label': 'madan mohan', 'label': 5, 'split': 'test', 'title': 'husn haazir hai muhabbat kii sazaa paane ko', 'year': '1976'}`
- output: `{"pred": "kalyanjianandji", "top3": ["kalyanjianandji", "laxmikantpyarelal", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='kalyanjianandji' ref='madan mohan'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='madan mohan' in top3=['kalyanjianandji', 'laxmikantpyarelal', 'shankarjaikishan']

### #44 — FAIL

- item: `{'lyrics': '  husne jaana idhar aa aaena hoon main tera main sawaroonga tujhe saare ghum de de mujhe bhigi palken na jhukaaaena hoon main tera   kitne hi daagh uthaye tu ne mere din raat sajaye tu ne chum loon aa mein teri palkon ko de doon ye umar teri zulfon ko leke aankhon ke diye muskura mere liye meri tasveere vafaaaena hoon main tera   teri chahat hai ibadat meri dekhta rahta hoon surat teri ghar tere dum se hai mandir mera tu hai devi mein pujari tera sajde sau bar karoonaa tujhe pyar karoon meri aaghosh men aaaaena hoon main tera husne jaana idhar aa ', 'correct_label': 'naushad', 'label': 6, 'split': 'test', 'title': 'husnejaanaa idhar aa', 'year': '1968'}`
- output: `{"pred": "s d burman", "top3": ["s d burman", "naushad", "a r rahman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='s d burman' ref='naushad'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='naushad' in top3=['s d burman', 'naushad', 'a r rahman']

### #45 — FAIL

- item: `{'lyrics': ' nirdhan kaa ghar lutane vaalon luut lo dil kaa pyaar pyaar vo dhan hai jisake aage sab dhan hai bekaar insaan bano insaan bano karalo bhalaai kaa koi kaam insaan bano duniyaa se chale jaaegaa rah jaaegaa badanaam insaan bano  o threedots is baag men suraj bhii nikalataa hai liye gam phulon kii hansii dekh ke ro detii hai shabanam kuchh der kii khushiyaan hain to kuchh der kaa maatam kis niind men ho threedots kis niind men ho jaago zaraa dekh lo anjaam insaan bano  o threedots laakhon yahaan shaan apanii dikhaate hue aaye dam bhar ko rahe naach gaye dhup men saaye vo bhul gaye the ke ye duniyaa hai saraay aataa hai koi threedots aataa hai koi subah ko jaata hai koi shaam insaan bano  o threedots kyon tumane bichhaaye hain yahaan zulm ke dere dhan saath na jaayegaa bane kyon ho lutere piite ho gariibon kaa lahuu shaam savere khud paap karo threedots khud paap karo naam ho shaitaan ka badanaam insaan bano', 'correct_label': 'naushad', 'label': 6, 'split': 'test', 'title': 'nirdhan kaa ghar luutane vaalon luut lo dil kaa pyaar', 'year': '-1'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "laxmikantpyarelal", "madan mohan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='shankarjaikishan' ref='naushad'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='naushad' in top3=['shankarjaikishan', 'laxmikantpyarelal', 'madan mohan']

### #46 — PASS

- item: `{'lyrics': '      mohan kii muraliyaa baaje ho sun thes jiyaa pe more laage  2  duur koii muralii kii dhun par giit milan ke gaaye jaane waale yaad men terii niind na mujhako aaye jab chain se duniyaa soye ho ek birahaa tamar man  jaage  mohan kii muraliyaa baaje ho sun thes jiyaa pe more laage  raat kahe dharatii par jagmag chaandanii ban kar barasuun aise men aa ke daras dikhaa jaa haay main roro tarasuun dil tod ke jaane waale ho mohe kuchh nahiin tujh bin saaje  mohan kii muraliyaa baaje ho sun thes jiyaa pe more laage  lutiin bahaaren saawan biitaa tuut gaye wo sapane jab se piyaa parades sidhaare rahe na din wo apane haay birahaa ke baadal kaale ho chhaayaa ghor andheraa more aage  mohan kii muraliyaa baaje ho sun thes jiyaa pe more laage ', 'correct_label': 'naushad', 'label': 6, 'split': 'test', 'title': 'mohan kii muraliyaa baaje', 'year': '1948'}`
- output: `{"pred": "naushad", "top3": ["naushad", "shankarjaikishan", "madan mohan"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='naushad' ref='naushad'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='naushad' in top3=['naushad', 'shankarjaikishan', 'madan mohan']

### #47 — FAIL

- item: `{'lyrics': '  jaane kyaa baat hai jaane kyaa baat hai niind nahiin aatii badii lambii raat hai  saarii saarii raat mujhe isane jagaayaa jaise koii sapanaa jaise koii saayaa koii nahiin lagataa hai koii mere saath hai niind nahiin aatii   threedots  dhakdhak kabhii se jiyaa dol rahaa hai ghuunghat abhii se meraa khol rahaa hai duur abhii to piyaa kii mulaaqaat hai niind nahiin aatii   threedots  jab jab dekhuun main ye chaand sitaare aisaa lagataa hai mujhe laaj ke maare jaise koii doli koii baaraat hai niind nahiin aatii   threedots ', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'jaane kyaa baat hai niind nahiin aatii badii lambii raat hai', 'year': '-1'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "annu malik", "r d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='r d burman' in top3=['laxmikantpyarelal', 'annu malik', 'r d burman']

### #48 — FAIL

- item: `{'lyrics': '  ki \tdilabar jaanii chalii havaa mastaanii \ta haan haan dilabar jaanii chalii havaa mastaanii \thansatekhelate guzare ye zindagaanii la \tdilabar jaanii chalii havaa threedots do \tdilabar jaanii chalii havaa threedots  la \tpyaar men din aise biite jaise biite pal 2 ki \tjaane kab shaam huii diip gae jal la \tsun mere pyaare ki \thuun la \tuuhuun huun aa haa haa \tsun mere pyaare ye hai terii meharabaanii \thansatekhelate guzare threedots  ki \tsaare soye tuu kyon jaage saathii kyaa baat hai 2 \to jangal ke raajaa aajaa sojaa ho gaii raat \tmiithemiithe sapane le aaii nindiyaa raanii \thansatekhelate guzare threedots do \tdilabar jaanii chalii havaa threedots ', 'correct_label': 'laxmikantpyarelal', 'label': 4, 'split': 'test', 'title': 'dilabar jaanii chalii havaa mastaanii', 'year': '1971'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "laxmikantpyarelal", "kalyanjianandji"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='r d burman' ref='laxmikantpyarelal'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='laxmikantpyarelal' in top3=['r d burman', 'laxmikantpyarelal', 'kalyanjianandji']

### #49 — PASS

- item: `{'lyrics': ' paagal kii tarah aavaaraa tere dil kaa sitaaraa kabhii yahaan kabhii vahaan bas tere pyaar kaa maaraa tere dil kaa sitaaraa dil dhuundhe tuu kahaan jaanejaan milane se darataa hai dil ikaraar ho naa jaae naa milo naa milo hamase jyaadaa kahiin pyaar ho naa jaae  ho betaabii kyaa hotii jaane naa dil kyaa bole kahanaa bhii maane naa dil dekho naa yuun hamako chaaho sanam chaahat kii raahon men hain dardogam kitane paas phir bhii duur hain donon ishq men kyuun majabuur hain ye nazaron kaa tiir dil ke kahiin paar ho naa jaae naa milo naa milo threedots  diivaanaa kar de naa diivaanaapan kahate hain ishq pe naa jor sanam jaaneman jaanejaan ye dillagii dekho naa ban jaae dil kii lagii to kaisaa dard hai kaisaa haal hai ab naa hosh hai ab naa khyaal hai ho kahiin jiinaa maranaa bhii dushvaar ho naa jaae naa milo naa milo threedots   ', 'correct_label': 'annu malik', 'label': 1, 'split': 'test', 'title': 'naa milo hamase jyaadaa kahiin pyaar ho naa jaae', 'year': '2000'}`
- output: `{"pred": "annu malik", "top3": ["annu malik", "a r rahman", "r d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='annu malik' ref='annu malik'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='annu malik' in top3=['annu malik', 'a r rahman', 'r d burman']

### #50 — FAIL

- item: `{'lyrics': ' ye saaye hain ye duniyaa hai parachhaaiyon kii ye saaye hain ye duniyaa hai bhari bhid men khali tanhaiyon ki ye saye hain  ye duniya hai   yahan koi sahil sahara nahin hai  kahin dubane ko kinara nahin hai  yahan koi sahil sahara nahin hai  yahan sari raunak ye rusavaiyon ki  ye saye hai ye duniya hai parachhaiyon ki  ye saye hai ye duniya hai threedots  kai chand uthakar jalae bujhae  bahut hamane chaha zara nind ae  kai chand uthakar jalae bujhae  yahan raat hoti hai bezariyon ki  ye saye hai ye duniya hai parachhaiyon ki  ye saye hai ye duniya hai threedots  yahan sare chehare hai mange hue se  nigahon men ansu bhi take hue se  yahan sare chehare hai mange hue se  badi nichi rahen hai unchaiyon ki  ye saye hai ye duniya hai parachhaiyon ki  ye saye hai ye duniya hai bhari bhid men khali tanhaiyon ki  ye saye hain ye duniya hai threedots', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'ye saaye hain ye duniyaa hai parachhaaiyon kii', 'year': '-1'}`
- output: `{"pred": "kalyanjianandji", "top3": ["kalyanjianandji", "laxmikantpyarelal", "madan mohan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='kalyanjianandji' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='r d burman' in top3=['kalyanjianandji', 'laxmikantpyarelal', 'madan mohan']

### #51 — FAIL

- item: `{'lyrics': '  gii \to lag gaiin ankhiyaan tum se morii \to mere baalam o mere sanam \tlag gaiin akhiyaan threedots  \tsharm kho gaii laaj kho gaii \thaay haay re raam haay raam haay haay haay raam \tmain to duniyaa se hii aaj kho gaii  ra \tahaa haa haa ye kahaanii naii sun lo gii \tsaarii duniyaa se hii main to kho gaii \to lag gaiin ankhiyaan threedots  \taaj merii nazar ko chamak mil gaii \tdil ko ik miithii miithii kasak mil gaii \to mere baalam \to lag gaiin ankhiyaan threedots  ra \tman ke taaron men laharaaii mastii kii dhun \tanaginat paayalen baj uthiin chhun chhunan chhun chhunan gii \to more baalam o mere saajan  \to sanam tujhase lag gaiin ankhiyaan \to lag gaiin ankhiyaan threedots ', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'o lag gaiin ankhiyaan tum se morii', 'year': '1953'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "naushad", "annu malik"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='shankarjaikishan' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='s d burman' in top3=['shankarjaikishan', 'naushad', 'annu malik']

### #52 — FAIL

- item: `{'lyrics': '  pahale sau baar idhar aur udhar dekhaa hai tab kahiin dar ke tumhen ek nazar dekhaa hai  ham pe hansatii hai jo duniyaan use dekhaa hii nahiin ham ne us shokh ko ae diidaaetar dekhaa hai  aaj is ek nazar par mujhe mar jaane do  us ne logon badii mushkil se idhar dekhaa hai  kyaa galat hai jo main diivaanaa huaa sach kahanaa mere mahabuub ko tum ne bhii agar dekhaa hai ', 'correct_label': 'laxmikantpyarelal', 'label': 4, 'split': 'test', 'title': 'pahale sau baar idhar aur udhar dekhaa hai', 'year': '1971'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "laxmikantpyarelal", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='r d burman' ref='laxmikantpyarelal'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='laxmikantpyarelal' in top3=['r d burman', 'laxmikantpyarelal', 'shankarjaikishan']

### #53 — FAIL

- item: `{'lyrics': ' na chhedo kal ke afasaane karo is raat kii baaten chhalakane do ye paimaane karo is raat kii baaten na chhedo kal ke afasaane  na phir ye raat aaegii na dil uchhalegaa siine men 2 na hogii rang pe mahafil na aisaa rang jiine men milenge kab ye diivaane karo is raat kii baaten na chhedo kal ke afasaane  har ek din kal kaa jhagadaa hai har ek din kal kaa hai ronaa 2 ye ghadiyaan raat kii tum bhii na auron kii tarah khonaa jo kal hogaa kudaa jaane karo is raat kii baaten na chhedo kal ke afasaane  karo vo baat jisase bojh dil kaa duur ho jaae 2 karo vo zikr jisase bekasii kaafuur ho jaae mile hain dil ko bahalaane karo is raat kii baaten na chhedo kal ke afasaane', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'na chhedo kal ke afasaane karo is raat kii baaten', 'year': '1967'}`
- output: `{"pred": "kalyanjianandji", "top3": ["kalyanjianandji", "r d burman", "s d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='kalyanjianandji' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='shankarjaikishan' in top3=['kalyanjianandji', 'r d burman', 's d burman']

### #54 — FAIL

- item: `{'lyrics': ' la \tudhar se tum chale aur ham idhar se 2 \tmuhabbat ho gaii \tmuhabbat ho gaii bas ek nazar se \tbas ek nazar se  ra \tmohabbat ban ke jo barasii hai dil par 2 \tna jaane wo ghataa aaii kidhar se 2 \tmuhabbat ho gaii do \tmuhabbat ho gaii bas ek nazar se 2 \tbas ek nazar se  la \tare dil kii kushii ke dene waale 2 \tbahut din ham terii ulafat ko tarase 2 \tmuhabbat ho gaii do \tmuhabbat ho gaii bas ek nazar se 2 \tbas ek nazar se  ra \to \tchhupaa rakhaa thaa siine men la \to \tchhupaa rakhaa thaa siine men do \ttumhaare pyaar ko duniyaa ke dar se 2 \tmuhabbat ho gaii \tmuhabbat ho gaii bas ek nazar se 2 \tbas ek nazar se ', 'correct_label': 'c ramchandra', 'label': 2, 'split': 'test', 'title': 'udhar se tum chale  muhabbat ho gaii bas ek nazar se', 'year': '1951'}`
- output: `{"pred": "naushad", "top3": ["naushad", "c ramchandra", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='naushad' ref='c ramchandra'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='c ramchandra' in top3=['naushad', 'c ramchandra', 'laxmikantpyarelal']

### #55 — PASS

- item: `{'lyrics': '  muhabbat hamaarii zamaanaa hamaaraa tuu gaae jaa ai dil taraanaa hamaaraa muhabbat hamaarii threedots  rahenge sadaa ham kushii ke chaman men 2 milegaa na gam ko thikaanaa hamaaraa 2 tuu gaae jaa ai dil threedots  hasiin hai muhabbat hamaare hii dam se 2 na bhuulegii duniyaa fasaanaa hamaaraa tuu gaae jaa ai dil threedots  ham is zindagii ko ujadane na denge 2  yahii zindagii hai  2 kazaanaa hamaaraa tuu gaae jaa ai dil threedots ', 'correct_label': 'naushad', 'label': 6, 'split': 'test', 'title': 'muhabbat hamaarii zamaanaa hamaaraa', 'year': '1949'}`
- output: `{"pred": "naushad", "top3": ["naushad", "shankarjaikishan", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='naushad' ref='naushad'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='naushad' in top3=['naushad', 'shankarjaikishan', 'laxmikantpyarelal']

### #56 — FAIL

- item: `{'lyrics': '  aaj kii raat piyaa aaj kii raat piyaa dil na todo man ki baat piya maan lo aaj ki raat piya  dil kii kahaanii apanii zubaanii tum ko sunaane aayii huun aankhon men leke sapane suhaane apanaa banaane aayii huun chodake saath piyaa muunh na modo man kii baat piyaa maan lo aaj kii raat piyaa  chandaa bhii dekhe taare bhii dekhe hamako gagan kii ot se ghaayal kiyaa hai dil tumane meraa meethi nazar kii chot se thaam ke haath piyaa yuun na chodo man kii baat piyaa maan lo aaj kii raat piyaa  ', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'aaj kii raat piyaa dil na todo', 'year': '1951'}`
- output: `{"pred": "naushad", "top3": ["naushad", "s d burman", "madan mohan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='naushad' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='s d burman' in top3=['naushad', 's d burman', 'madan mohan']

### #57 — PASS

- item: `{'lyrics': ' machal machal jaataa hai dil 2 soch kal kii baaten machal machal jaataa hai dil soch kal kii baaten ab to apane hii din honge hongii apanii raaten o raaten 2 machal machal jaataa hai dil  tuu kyaa jaane tere bin vo din kaise biite 2 ek terii aas thii varnaa ham nahiin jiite main huun raanii tu hai raajaa 2 taaron kii baaraaten ab to apane threedots  kahiin apanaa chhotaa saa ghar hogaa pyaaraa pyaaraa 2 baant lenge ham jiivan kaa dukh sukh saaraa hongii apane aangan men phir 2 pyaar kii saugaaten ab to apane threedots  ek pal judaa naa hon ham mil jaaen aise 2 do laharen ek duuje se mil jaaen jaise rah rah ke yaad aaengii 2 pahalii mulaaqaaten ab to apane threedots', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'machal machal jaataa hai dil soch kal kii baaten', 'year': '1985'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "kalyanjianandji", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='r d burman' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='r d burman' in top3=['r d burman', 'kalyanjianandji', 'laxmikantpyarelal']

### #58 — FAIL

- item: `{'lyrics': ' raat kalii ek khvaab men aaii aur gale kaa haar huii subah ko jab ham niind se jaage aankh tumhii se chaar huii raat kalii ek khvaab men aaii aur gale kaa haar huii  chaahe kaho ise merii mohabbat chaahe hansiin men udaa do ye kyaa huaa mujhe mujhako khabar nahiin ho sake tum hii bataa do tumane kadam jo rakhaa zamiin par siine men kyon jhankaar huii raat kalii threedots  aankhonmen kaajal aur latonmen kaalii ghataa kaa baseraa saanvalii suurat mohanii muurat saavan rut kaa saveraa jabase ye mukhadaa dil me khilaa hai duniyaa merii gulazaar huii raat kalii threedots  yuun to hasiinon ke mahajabiinon ke hote hain roz nazaare par unhen dekh ke dekhaa hai jab tumhen tum lage aur bhii pyaare baahon men le luun aisii tamannaa ek nahiin kaii baar huii raat kalii threedots', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'raat kalii ek khvaab men aaii aur gale kaa haar huii', 'year': '1971'}`
- output: `{"pred": "s d burman", "top3": ["s d burman", "r d burman", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='s d burman' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='r d burman' in top3=['s d burman', 'r d burman', 'shankarjaikishan']

### #59 — PASS

- item: `{'lyrics': ' dil jale to jale gam pale to pale kisii kii na sun gaaye jaa  o jiine vaale aag se aag bujhaa le jag kii na sun pyaar kii dhun jhuum ke gaa le dil jale to jale   threedots  o jiine vaale ye kaliyaan ye taare chup to hain magar takate idhar kahate hain saare dil jale to jale   threedots  o jiine vaale chhed hasiin taaren bichhade jo ab milanaa ho kab koii na jaane dil jale to jale   threedots ', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'dil jale to jale gam pale to pale', 'year': '1954'}`
- output: `{"pred": "s d burman", "top3": ["s d burman", "shankarjaikishan", "r d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='s d burman' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='s d burman' in top3=['s d burman', 'shankarjaikishan', 'r d burman']

### #60 — PASS

- item: `{'lyrics': ' hai isii men pyaar kii aabaruu vo zafaa karen main vafaa karuun jo vafaa bhii kaam na aa sake to vohii kahen ke main kyaa karuun hai isii threedots  mujhe gam bhii unakaa aziiz hai  ke unhiin kii dii huii chiiz hai   2 ke unhiin kii dii huii chiiz hai yahii gam hai ab merii zindagii ise kaise dil se judaa karuun hai isii threedots  jo na ban sake main vo baat huun  jo na khatm ho main vo raat huun   2 jo na khatm ho main vo raat huun ye likhaa hai mere nasiib men yuunhii shammaa banake jalaa karuun hai isii threedots  na kisii ke dil kii huun aarazuu  na kisii kii nazar kii huun justajuu   2 na kisii kii nazar kii huun justajuu main vo phuul huun jo udaas ho na bahaar aae to kyaa karuun hai isii threedots', 'correct_label': 'madan mohan', 'label': 5, 'split': 'test', 'title': 'hai isii men pyaar kii aabaruu vo jafaa karen main vafaa karuun', 'year': '0'}`
- output: `{"pred": "madan mohan", "top3": ["madan mohan", "c ramchandra", "annu malik"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='madan mohan' ref='madan mohan'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='madan mohan' in top3=['madan mohan', 'c ramchandra', 'annu malik']

### #61 — PASS

- item: `{'lyrics': ' laa laa laa laa laa laa o o o oho  vaadiyaan meraa daaman raaste merii baanhen jaao mere sivaa tum kahaan jaaoge vaadiyaan meraa daaman raaste merii baanhen jaao mere sivaa tum kahaan jaaoge vaadiyaan meraa daaman \t jab hansegii kalii rangavaalii koii 2 aur jhuk jaaegii tum pe dalii koii sar jhukaae hue tum mujhe paaoge vaadiyaan meraa daaman raaste merii baanhen jaao mere sivaa tum kahaan jaaoge vaadiyaan meraa daaman \t chal rahe ho jahaan is nazar se pare 2 vo dagar to guzaratii hai dil se mere dagamagaate hue tum yahiin aaoge vaadiyaan meraa daaman raaste merii baanhen jaao mere sivaa tum kahaan jaaoge  vaadiyaan meraa daaman raaste merii baanhen jaao mere sivaa tum kahaan jaaoge vaadiyaan meraa daaman', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'vaadiyaan meraa daaman', 'year': '1968'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "shankarjaikishan", "madan mohan"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='r d burman' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='r d burman' in top3=['r d burman', 'shankarjaikishan', 'madan mohan']

### #62 — FAIL

- item: `{'lyrics': '  bol siyaavar raamachandr kii jay pavanasut hanumaan kii jay har har mahaadev kii jay paarvatii ke pati bhagavatii paande kii jay  gangaaghaat kaa paanii piyaa hai ab sabako main paanii pilaa duungaa mujhako bhalaa samajhate ho kyaa tumhen haridvaar pahunchaa duungaa gangaaghaat kaa paanii threedots  pyaar kii baanii bolane vaalaa ban jaae ek tamaashaa is duniyaa men to chalatii hai bas laathii kii bhaashaa kaun hai tolaa kaun hai maashaa ye bhed abhii samajhaa duungaa gangaaghaat kaa paanii threedots  do shabdon men kah detaa huun is duniyaa kii kahaanii bholaa huun main nirbal nahiin din men bhii taare dikhaa duungaa gangaaghaat kaa paanii threedots  tumako sab kuchh nayaa mubaaraq hamako vahii puraanaa dekho gorii hai baalii umariyaa soch ke paanv badhaanaa vah to miit ek raat ke main to sangsang umar bitaa duungaa gangaaghaat kaa paanii threedots ', 'correct_label': 'laxmikantpyarelal', 'label': 4, 'split': 'test', 'title': 'bol siyaavar  gangaaghaat kaa paanii piyaa hai', 'year': '1975'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "madan mohan", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='shankarjaikishan' ref='laxmikantpyarelal'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='laxmikantpyarelal' in top3=['shankarjaikishan', 'madan mohan', 'laxmikantpyarelal']

### #63 — FAIL

- item: `{'lyrics': '     raat chupchaap dabe paanv chalii jaatii hai 2 raat kaamosh hai rotii nahiin hansatii bhii nahiin raat chupchaap dabe paanv chalii jaatii hai raat kaamosh hai rotii nahiin hansatii bhii nahiin raat chupchaap dabe paanv chalii jaatii hai  kaanch kaa niilaasaa gumbad hai udaa jaataa hai 2 paal khole koii bajaraasaa bahaa jaataa hai ek sailaab hai saahil pe bichhaa jaataa hai raat chupchaap dabe paanv chalii jaatii hai  chaand kii kiranon men vo rozsaa resham bhii nahiin 2 chaand kii chikanii dalii hai ki ghulii jaatii hai aur sannaaton kii ik dhuul udii jaatii hai raat chupchaap dabe paanv chalii jaatii hai  kaash ik baar kabhii niind se uth kar tum bhii 2 hijr kii raaton men ye dekho to kyaa hotaa hai ', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'raat chupchaap dabe paanv chalii jaatii hai', 'year': '1987'}`
- output: `{"pred": "madan mohan", "top3": ["madan mohan", "laxmikantpyarelal", "r d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='madan mohan' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='r d burman' in top3=['madan mohan', 'laxmikantpyarelal', 'r d burman']

### #64 — PASS

- item: `{'lyrics': ' dil kyon dhadakataa hai kyon pyaar hotaa hai siine men dard kyon baar baar hotaa hai dil kyon dhadakataa hai threedots  dil men agar apane hotii na ye dhadakan to zindagii bhar ham donon ajanabii rahate ye pyaar kii baaten ham jaanate kaise har saans ye kahatii tuu paas mere rahatii phir bhii mujhe teraa intazaar hotaa hai dil kyon dhadakataa hai threedots  ab to nahiin milatii apanii khabar mujhako tere khyaalon men ham is kadar khoye padhakar kitaabon ko raaten guzaariin hamane jab se muhabbat kii jii bhar nahiin soye is umr men sab kaa ye haal hotaa hai kyon pyaar hotaa hai threedots ', 'correct_label': 'annu malik', 'label': 1, 'split': 'test', 'title': 'dil kyon dhadakataa hai kyon pyaar hotaa hai', 'year': '1993'}`
- output: `{"pred": "annu malik", "top3": ["annu malik", "kalyanjianandji", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='annu malik' ref='annu malik'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='annu malik' in top3=['annu malik', 'kalyanjianandji', 'laxmikantpyarelal']

### #65 — FAIL

- item: `{'lyrics': ' kisi shaayar ki gazal dreamgirl kisi jhil ka kanval dreamgirl kabhi to milegi kahin to milegi aaj nahin to kal dreamgirl threedots  simati gulabon men lipati hijaabon men  2 saason men aati hai bhigi sharaabon men pas rahati hai vo pal do pal kaun  dreamgirl threedots  jab dekhati hai vo main puchh lunga to   2 shabanam ghata chaandani ban jaate hain doston rang rup hai vo leti badal he dreamgirl threedots', 'correct_label': 'laxmikantpyarelal', 'label': 4, 'split': 'test', 'title': 'dream girl', 'year': '1977'}`
- output: `{"pred": "madan mohan", "top3": ["madan mohan", "kalyanjianandji", "a r rahman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='madan mohan' ref='laxmikantpyarelal'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='laxmikantpyarelal' in top3=['madan mohan', 'kalyanjianandji', 'a r rahman']

### #66 — FAIL

- item: `{'lyrics': ' koii pyaar ke pankh pasaare aayaa hai paas tehaare sudhsudh apanii bisaraae pagalaa man tohe pukaare  zaraa man kii khevadiyaan khol sainyaa tore dvaare khade sainyaa tore sajanaa tore dvaare khade o sainyaa tore sajanaa tore dvaare khade  birahaa kii rainaa 2 terii galiyon ke phere 2 jogii kaa ruup liyaa priitam ne tere 2 gorii sun le balam ke bol sainyaa tore dvaare khade o sainyaa tore sajanaa tore dvaare khade  milanaa hai aaj tohe apane piaa se 2 jaane na bhed koii tere jiaa ke 2 manman men sajaniyaa dol sainyaa tore dvaare khade sainyaa tore dvaare khade o sainyaa tore sajanaa tore dvaare khade  bigade na baat kahiin dhiiraj na khonaa 2 jaage na bhaag ab kaahe kaa ronaa 2 teraa jiivan badaa anamol sainyaa tore dvaare khade sainyaa tore dvaare khade o sainyaa tore sajanaa tore dvaare khade  o man kii khevadiyaan khol sainyaa tore dvaare khade', 'correct_label': 'naushad', 'label': 6, 'split': 'test', 'title': 'zaraa man kii khevadiyaan khol sainyaa tore dvaare khade', 'year': '-1'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "naushad", "s d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='shankarjaikishan' ref='naushad'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='naushad' in top3=['shankarjaikishan', 'naushad', 's d burman']

### #67 — FAIL

- item: `{'lyrics': ' chale aaj tum jahaan se huii zindagii paraayii tumhen mil gayaa thikaanaa hamen maut bhii na aayii  o duur ke musaafir ham ko bhii saath le le re ham ko bhii saath le le ham rah gaye akele  tuune vo de diyaa gam bemaut mar gaye ham dil uth gayaa jahaan se le chal hamen yahaan se le chal hamen yahaan se kis kaam kii ye duniyaa jo zindagii se khele re ham ko bhii saath le le ham rah gaye akele  suunii hain dil kii raahen khaamosh hain nigaahen naakaam hasaraton kaa uthane ko hai janaazaa uthane ko hai janaazaa chaaron taraf lage hain barabaadiyon ke mele re ham ko bhii saath le le ham rah gaye akele  o duur ke musaafir ham ko bhii saath le le re ham ko bhii saath le le ham rah gaye akele ', 'correct_label': 'naushad', 'label': 6, 'split': 'test', 'title': 'o duur ke musaafir hamako bhii saath le le re', 'year': '1955'}`
- output: `{"pred": "c ramchandra", "top3": ["c ramchandra", "s d burman", "naushad"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='c ramchandra' ref='naushad'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='naushad' in top3=['c ramchandra', 's d burman', 'naushad']

### #68 — FAIL

- item: `{'lyrics': '     badhaaii ho badhaaii janamadin kii tumako janamadin tumhaaraa milenge ladduu hamako badhaaii ho badhaaii janamadin kii tumako  sadaa dil lagaa ke tuu mehanat se padhanaa mehanat se padhanaa padhaaii men aage se aage hii badhanaa aage hii badhanaa achchhaa jii bataao mainne aisaa kyuun kahaa jo tum paas hoge milenge ladduu hamako badhaaii ho badhaaii janamadin kii tumako  bade ho ke laanaa hamaarii tuu bhaabhii hamaarii tuu bhaabhii ke jisakii ho rangat gulaabiigulaabii gulaabiigulaabii achchhaa jii bataao mainne aisaa kyuun kahaa tumhaarii hogii shaadii milenge ladduu hamako badhaaii ho badhaaii janamadin kii tumako  budhaape men honge idhar baal pakke idhar baal pakke udhar honge ghar men jii bachchon ke bachche jii bachchon ke bachche achchhaa jii bataao mainne aisaa kyuun kahaa tumhaare hogaa potaa milenge ladduu hamako badhaaii ho badhaaii janamadin kii tumako ', 'correct_label': 'kalyanjianandji', 'label': 3, 'split': 'test', 'title': 'badhaaii ho badhaaii janamadin kii tumako', 'year': '1967'}`
- output: `{"pred": "annu malik", "top3": ["annu malik", "r d burman", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='annu malik' ref='kalyanjianandji'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='kalyanjianandji' in top3=['annu malik', 'r d burman', 'shankarjaikishan']

### #69 — FAIL

- item: `{'lyrics': ' kitanii javaan hai raat koii yaad aa gayaa badhane lagii hai baat koii yaad aa gayaa  phir aa gayii chaman men guzarii huii bahaar rahane lagaa kisii kaa phir dil ko intazaar ab hogii mulaaqaat koii yaad aa gayaa badhane lagii hai baat   threedots  phir yaad aa rahen hain guzare hue zamaane dil gunagunaa rahaa hai bhuule hue taraane tanhaaii aur ye raat koii yaad aa gayaa badhane lagii hai baat   threedots  aankhon se niind jaane ud kar kahaan gaii hai vo bhii vahiin pe honge nindiyaa jahaan gaii hai shaayad yahii hai baat koii yaad aa gayaa badhane lagii hai baat   threedots ', 'correct_label': 'c ramchandra', 'label': 2, 'split': 'test', 'title': 'kitanii javaan hai raat koii yaad aa gayaa', 'year': '1955'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "shankarjaikishan", "naushad"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='c ramchandra'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='c ramchandra' in top3=['laxmikantpyarelal', 'shankarjaikishan', 'naushad']

### #70 — PASS

- item: `{'lyrics': '  duniyaa vaalon raamsiitaa kii naii kahaanii sun lo vaalmiik se kuub sunii ab merii zubaanii sun lo  galiigalii siitaa roe aaj mere desh men siitaa dekhii raam dekhaa aaj nae bhesh men  tumane naam sunaa siitaa kaa main use dekh aayaa huun o dharm ke thekedaaron main ek naii raamaayan laayaa huun vo siitaa thii raamaayan kii jiitii jaagatii ruuthe raam se jo khoyaa pyaar maangatii galiigalii siitaa roe threedots  raam kii liilaa dekh chuke koii usakii liilaa jaane naa raam yahaan siitaa yahaan par koii pahachaane naa aage badh ke dekh diivaane tuu hii inakaa raam hai isake dil ko chiir ke dekh liyaa teraa naam hai galiigalii siitaa roe threedots  dharatii phatii siitaa chhupii kahiin nazar aaye naa ye vo siitaa hai ki jise dharatii bhii chhupaaye naa ye bhii siitaa vo bhii siitaa fark dekho bhaag men vo aag se laut aaii ye hai abhii aag men galiigalii siitaa roe threedots  bahan jis bhaaii kii hai vo bhii kafaa ho gayaa maan ye kisii laal kii hai vo bhii judaa ho gayaa janak siitaa chhod de to kahaan jaae jaanakii maan ise pahachaan ke bhii phir nahiin pahachaanatii galiigalii siitaa roe threedots  kyon bharosaa nahiin isape kyaa ye pyaar jhuuthaa hai bolobolo aansuon kaa kyaa ye haar jhuuthaa hai isakii kathaa jhuuthii hai to jhuuthaa bhagavaan hai jhuuthii hai raamaayan saarii aur jhuuthaa raam hai dharm jhuuthaa prem jhuuthaa jhuuthaa hindustaan hai deviyon pe dosh lage aaj mere desh men siitaa to hai raam nahiin aaj mere desh men galiigalii siitaa roe threedots ', 'correct_label': 'kalyanjianandji', 'label': 3, 'split': 'test', 'title': 'duniyaa vaalon raamsiitaa kii  galiigalii siitaa roe', 'year': '1960'}`
- output: `{"pred": "kalyanjianandji", "top3": ["kalyanjianandji", "laxmikantpyarelal", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='kalyanjianandji' ref='kalyanjianandji'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='kalyanjianandji' in top3=['kalyanjianandji', 'laxmikantpyarelal', 'shankarjaikishan']

### #71 — FAIL

- item: `{'lyrics': '  lagan tose laagii balamaa 2  dhare dil pe haath taaron ke saath saarii rain jaagii balamaa lagan tose laagii balamaa 2   chamakchamak kar duube taare ikik kar ke saare  2 ghatateghatate ghat gaii baatii phiike pade ujiyaare chalatechalate thak gayaa chandaa thake na pyaar ke maare lagan tose laagii balamaa 2   niind kii maa thii  duniyaa saarii sapanon men thii khoii  2 rukiirukii thiin mast hawaayen laharlahar thii soii main nindiyaa se duur rahii kyuun ye na jaane koii lagan tose laagii balamaa 2   chaand ne kitanaa mujhase puuchhaa baat koii to hogii  2 kisake kaaran jog liyaa hai kaun hai teraa jogii main bas munh se itanaa bolii priit kii huun main rogii lagan tose laagii balamaa 4  dhare dil pe haath taaron ke saath saarii rain jaagii balamaa lagan tose laagii balamaa 2 ', 'correct_label': 'madan mohan', 'label': 5, 'split': 'test', 'title': 'lagan tose laagii balamaa', 'year': '1957'}`
- output: `{"pred": "naushad", "top3": ["naushad", "madan mohan", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='naushad' ref='madan mohan'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='madan mohan' in top3=['naushad', 'madan mohan', 'shankarjaikishan']

### #72 — FAIL

- item: `{'lyrics': ' la apanii kaho kuchh merii suno     kyaa dil kaa lagaanaa bhuul gae kyaa bhuul gae ta rone kii aadat aisii padii     hansane kaa taraanaa bhuul gae haan bhuul gae  la kaalii raaten biit gaiin     phir chaandanii raaten aaii hain\t  2 ta dil men nahiin ujiyaalaa mere     gam kii ghataaen chhaaii hain       2 la priit ke vaade yaad karo     kyaa priit nibhaanaa bhuul gae kyaa bhuul gae  ta bhuulaa huaa hai raah musaafir     bichhadaa huaa hai manzil se\t  2 la khoe hue raste kaa pataa     tum puuchh lo kud apane dil se\t  2 ta chalate chalate aise thake     manzil kaa thikaanaa bhuul gae haan bhuul gae  la nazdiik aao nazdeek aa threedots     yah mausam nahiin phir aane kaa\t  2 ta nazdiik shamaa ke jaane se     kyaa haal huaa parvaane kaa\t\t  2 la mitane kaa fasaanaa yaad rahaa     jalane kaa fasaanaa bhuul gae kyaa bhuul gae     apanii kaho kuchh merii suno     kyaa dil kaa lagaanaa bhuul gae kyaa bhuul gae ', 'correct_label': 'c ramchandra', 'label': 2, 'split': 'test', 'title': 'apanii kaho kuchh merii suno kyaa dil kaa lagaanaa bhuul gae', 'year': '1952'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "madan mohan", "kalyanjianandji"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='shankarjaikishan' ref='c ramchandra'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='c ramchandra' in top3=['shankarjaikishan', 'madan mohan', 'kalyanjianandji']

### #73 — PASS

- item: `{'lyrics': '  ho sar pe mukut saje mukh pe ujaalaa haath men dhanush gale men pushp maalaa ham daas inake ye svaamii sabake anjaan ham ye antarayaamii shiish jhukaao raamgun gaao bolo jay vishnu ke avataarii  raam jii kii nikalii savaarii raam jii kii liilaa hai nyaarii ko \traam jii kii nikalii threedots ek taraf laxman ek taraf siitaa biich men jagat ke paalanahaarii ko \traam jii kii nikalii threedots  dhiire chalaa rath o rath vaale tohe kabar kyaa o bholebhaale ko \ttohe kabar kyaa o bholebhaale ik baar dekho jii naa bharegaa sau baar dekho phir jii karegaa vyaakul pade hain kabase khade hain ko \tvyaakul pade hain kabase khade hain darshan ke pyaase sab narnaarii raam jii kii nikalii threedots ko \traam jii kii nikalii threedots  chaudah baras kaa vanavaas paayaa maataapitaa kaa vachan nibhaayaa ko \tmaataapitaa kaa vachan nibhaayaa dhokhe se har lii raavan ne siitaa raavan ko maaraa lankaa ko jiitaa ko \traavan ko maaraa lankaa ko jiitaa tabtab ye aae 2 ko \ttabtab ye aae 2 jabjab duniyaa inako pukaarii raam jii kii nikalii threedots ek taraf laxman threedots ko \traam jii kii nikalii threedots ', 'correct_label': 'laxmikantpyarelal', 'label': 4, 'split': 'test', 'title': 'ho sar pe mukut saje  raam jii kii nikalii savaarii', 'year': '1979'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "kalyanjianandji", "naushad"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='laxmikantpyarelal' ref='laxmikantpyarelal'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='laxmikantpyarelal' in top3=['laxmikantpyarelal', 'kalyanjianandji', 'naushad']

### #74 — PASS

- item: `{'lyrics': '  ku \taankhon ne tumhaarii miithii baaton ne 2 \tmerii niind udaaii meraa chain churaayaa \tsapanaa sajaayaa apanaa banaayaa \tapanaa banaake sapanaa sajaake \tchupake se sikhaayaa pyaar \tdhiiredhiire is dil kaa chhiinaa hai qaraar 2 a \taankhon ne tumhaarii miithii threedots chhiinaa hai qaraar  ku \tdiivaanaa ishq kaa main to hone lagaa \tzulfon kii ot men jaanaan khone lagaa a \tmeraa kahanaa naa maane merii pyaas naa jaane \tdhakdhak dhadake dil meraa tadape \trangiin safar men aisii umar men \tdard uthaa pahalii baar ku \tdhiiredhiire is dil kaa chhiinaa hai qaraar a \tdhiiredhiire is dil kaa chhiinaa hai qaraar  \tyaadon men aajkal kaatuun main raatdin \tjhuuthaa saaraa jahaan lagataa hai tere bin ku \tkyaa haal jiyaa kaa main tujhase bataauun \tek pal kahiin main tujhe bhuul naa paauun \tshaamsavere dil ko mere rahataa hai kyon intazaar a \tdhiiredhiire is dil kaa chhiinaa hai qaraar ku \tdhiiredhiire is dil kaa chhiinaa hai qaraar ku \taankhon ne tumhaarii miithii baaton ne a \taankhon ne tumhaarii miithii baaton ne ku \tmerii niind udaaii a \tmeraa chain churaayaa ku \tsapanaa sajaayaa a \tapanaa banaayaa ku \tapanaa banaake a \tsapanaa sajaake ku \tchupake se a \tsikhaayaa pyaar ku \tdhiiredhiire is dil kaa chhiinaa hai qaraar a \tdhiiredhiire is dil kaa chhiinaa hai qaraar ', 'correct_label': 'annu malik', 'label': 1, 'split': 'test', 'title': 'aankhon ne tumhaarii miithii baaton ne', 'year': '2003'}`
- output: `{"pred": "annu malik", "top3": ["annu malik", "c ramchandra", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='annu malik' ref='annu malik'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='annu malik' in top3=['annu malik', 'c ramchandra', 'shankarjaikishan']

### #75 — FAIL

- item: `{'lyrics': ' sakhii rii birahaa ke dukhade sah sah kar jab raadhe besudh ho lii to ik din apane manamohan se jaa kar yuun bolii  aaj sajan mohe ang lagaalo  janam safal ho jaaye  hriday kii piidaa deh kii agni  sab shiital ho jaaye   karuun laakh jatan more man kii tapan  more tan kii jalan nahiin jaaye  kaisii laagii ye lagan kaisii jaagii ye agan  jiyaa dhiir dharan nahiin paaye  prem sudhaa threedots more saanvariyaa  prem sudhaa itani barasaa do jag jal thal ho jaaye  aaj sajan threedots  mohe apanaa banaalo meri baanh pakad  main huun janam janam kii daasii  meri pyaas bujhaa do manahar giridhar pyaas bujhaa do  main huun antarghat tak pyasi  prem sudhaa threedots more saanvariyaa  prem sudhaa itani barasaa do jag jal thal ho jaaye  aaj sajan threedots  kaii jug se hain jaage more nain abhaage 2 kahiin jiyaa nahiin laage bin tore sukh dekhe nahiin aage 2 duhkh piichhe piichhe bhaage jag suunaa suunaa laage bin tore prem sudhaa more saanvariyaa saanvariyaa prem sudhaa itanii barasaa do jag jal thal ho jaaye aaj sajan threedots ', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'aaj sajan mohe ang lagaalo janam safal ho jaaye', 'year': '-1'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "naushad", "s d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='s d burman' in top3=['laxmikantpyarelal', 'naushad', 's d burman']

### #76 — PASS

- item: `{'lyrics': ' rote hue aate hain sab hansataa huaa jo jaaegaa vo muqaddar kaa sikandar jaaneman kahalaaegaa  vo sikandar kyaa thaa zisane zulm se jiitaa zahaan pyaar se jiite dilon ko vo jhukaa de aasamaan jo sitaaron par kahaanii pyaar kii likh jaaegaa vo muqaddar kaa sikandarthreedots  zindagii to bevafaa hai ek din thukaraaegii maut mahabuubaa hai apane saath lekar jaaegii mar ke jiine kii adaa jo duniyaa ko sikhalaaegaa vo muqaddar kaa sikandarthreedots  hamane maanaa ye zamaanaa dard kii jaagiir hai har kadam pe aansuon kii ik nai zanjiir hai aae din par jo khushii ke giit gaataa jaaegaa vo muqaddar kaa sikandarthreedots  rote hue aate hain sab hansataa huaa jo jaaegaa vo muqaddar kaa sikandar jaaneman kahalaaegaa', 'correct_label': 'kalyanjianandji', 'label': 3, 'split': 'test', 'title': 'rote hue aate hain sab hansataa huaa jo jaaegaa', 'year': '1978'}`
- output: `{"pred": "kalyanjianandji", "top3": ["kalyanjianandji", "shankarjaikishan", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='kalyanjianandji' ref='kalyanjianandji'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='kalyanjianandji' in top3=['kalyanjianandji', 'shankarjaikishan', 'laxmikantpyarelal']

### #77 — PASS

- item: `{'lyrics': ' karo baaten mulaaqaaten aisii raaten jaagii jaagii soye soye khoye khoye main aur tuu karo baaten mulaaqaaten aisii raaten jaagii jaagii soye soye khoye khoye main aur tuu  aankhon se karanaa tum baaten chup rahanaa tumane jo kat men likkhaa thaa mat kahanaa haan haan logon se kah duun main dil kaa afasaanaa tumane samajhaa hai kyaa mujhako diiwaanaa laakh chhupaao chhup nahiin sakate pyaar aur kushabuu  dekho raazedil ye duniyaa naa jaane koii dekhe to ban jaanaa begaane hen hen dil ko lene do laharaake angadaaii mahafil men dhuundho thodii sii tanahaaii aankhon hii aankhon men chalane do pyaar kaa jaaduu  karo baaten mulaaqaaten aisii raaten jaagii jaagii soye soye khoye khoye main aur tuu ', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'karo baaten mulaaqaaten aisii raaten', 'year': '1976'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "c ramchandra", "s d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='r d burman' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='r d burman' in top3=['r d burman', 'c ramchandra', 's d burman']

### #78 — FAIL

- item: `{'lyrics': ' naa naa naa naa naa naa na na naa asalaa vallaa vallaa main lailaa vallaa vallaa oelaa oelaa aa aa fiinak yaa habiibii fiinak yaa habiibii fiinak dil ko churaa ke mere apanaa banaa le mujhe dil meraa le ke jaae mehabuubaa asalaa vallaa vallaa threedots  yak ba yak teraa saamane aanaa yak ba yak teraa dil ko dhadakaanaa yak ba yak nazaren milaanaa yak ba yak nazaren churaanaa yak ba yak muskuraanaa yaa allaa allaa vallaa yak ba yak teraa saamane aanaa fiinak yaa habiibii fiinak ye aankhen terii  dil ko churaa ke mere threedots  chaand taare tere badan men jade hain aage piichhe aashiq hazaaron khade hain tere mere do nainaa jab se lade hain terii baahon men aa ke ham to mare hain fiinak yaa habiibii fiinak ye aankhen terii  dil ko churaa ke mere threedots  ruup teraa sone men dhal ke banaa hai jaan merii tujh men nashaa hii nashaa hai  uf kyaa nigaahen kyaa adaa hai aaj ye diivaanaa to tujh pe fidaa hai ', 'correct_label': 'annu malik', 'label': 1, 'split': 'test', 'title': 'asalaa vallaa vallaa  fiinak yaa habiibii  dil ko churaa ke mere', 'year': '2002'}`
- output: `{"pred": "madan mohan", "top3": ["madan mohan", "annu malik", "kalyanjianandji"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='madan mohan' ref='annu malik'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='annu malik' in top3=['madan mohan', 'annu malik', 'kalyanjianandji']

### #79 — PASS

- item: `{'lyrics': ' banjar hai sab banjar hai banjar hai sab banjar hai ham dhuundhane jab firadaus chale  huun terii khoj talaash men dekh piyaa ham kitane kaale kos chale  banjar hai sab banjar hai  mainnaa yaar milaa de saaiiyaan ek baar milaa de saaiiyaan ek baar milaa de saaiiyaan 2  mainne fotaafotaa falaq chaandaa maine totetote taare chune 2  maindaa yaar milaan de saaiiyaan ek baar milaa de saaiiyaan ek baar milaa de saaiiyaan 2  taaron kii chamak ye subaho talaq  lagatii hii nahin par baraf talaq  saaiiyaan saaiiyaan saaiiyaan  mainne fotaafotaa falaq chaandaa maine totetote taare chune 2  sirf ik terii aahat ke liye kankad patthar but saare sune  muda de da de rusvaaiyaan  mainnaa yaar milaa de saaiiyaan ek baar milaa de saaiiyaan ek baar milaa de saaiiyaan 2  aa aa aa mainnaa yaar milaa de saaiiyaan ek baar milaa de saaiiyaan ek baar milaa de saaiiyaan 2  banjar hai sab banjar hai 3 banjar hai sab banjar hai ham dhuundhane jab firadaus chale huun terii khoj talaash men dekh piyaa ham kitane kaale kos chale banjar hai sab banjar hai yaar milaa de saaiiyaan  aa dekh merii peshaanii ko taqadiir ke harfe likkhe hain  pairon ke nishaan jab dekhe jahaan sau baar jhukaayaa sar ko vahaan  yaar milaa de saaiiyaan aa dekh merii peshaanii ko taqadiir ke harfe likkhe hain main kitanii baar pukaaruun tujhe tere naam ke saffe likkhe hain  teraa saayaa kabhii to bolegaa teraa saayaa kabhii to bolegaa main chunataa rahaa parchhaaiyaan  mainnaa yaar milaa de saaiiyaan saaiiyaan saaiiyaan ', 'correct_label': 'a r rahman', 'label': 0, 'split': 'test', 'title': 'banjar hai sab banjar hai  meraa yaar milaa de saaiiyaan', 'year': '2002'}`
- output: `{"pred": "a r rahman", "top3": ["a r rahman", "madan mohan", "s d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='a r rahman' ref='a r rahman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='a r rahman' in top3=['a r rahman', 'madan mohan', 's d burman']

### #80 — PASS

- item: `{'lyrics': ' aashaa   takaraa gaye do baadal ambar pe                 to barasane lage buunden bikhar ke                 takaraa gaye do  vinod speaking                 maushumii kitanaa pyaaraa naam hai ye                 is naam kaa saath to har mausam se hai                 chaahe wo sardii kaa ho yaa garmii kaa                 patajhad kaa yaa saawan kaa  aashaa   aahaa chhodo jaao bade wo ho tum                 naam meraa jod diyaa mausam se sanam                 mausam phir bhii mausam hai sanam                 naam mera jodaa na bataa kud se kyon balam                 mujhase milaao ye nain to                 aise na jalaao mere man ko                 takaraa gaye do  vinod speaking                 ye saawan kaa mausam to kuubasuurat hai hii                 lekin tumhaarii is kuubasuurat umar ne                 ise aur bhii kuubasuurat banaa diyaa hai  aashaa   jaane aaii kaisii ye umar                 ban ke kalii khilane lagii                 suunii raah par                 tan men man men uthii ye lahar                 tujhase sajan takaraae man jaauun main bikhar                 aag lage re saawan ko chhoo gayaa mere daaman ko                 takaraa gaye do baadal ambar pe                 to barasane lage buunden bikhar ke                 takaraa gaye do', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'takaraa gaye do baadal ambar pe', 'year': '1975'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "shankarjaikishan", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='r d burman' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='r d burman' in top3=['r d burman', 'shankarjaikishan', 'laxmikantpyarelal']

### #81 — FAIL

- item: `{'lyrics': '  tasaviir banaataa huun terii kuunejigar se kuunejigar se dekhaa hai tujhe main ne muhabbat kii nazar se are muhabbat kii nazar se  jitane bhii mile rang vo sabhii bhar diye tujh men haay bhar diye tujh men ik rangevafaa aur hai laauun vo kidhar se are laauun vo kidhar se tasaviir banaataa huun terii threedots  saavan terii zulfon se ghataa maang ke laayaa haay maang ke laayaa bijalii ne churaaii hai tadap terii nazar se are tadap terii nazar se tasaviir banaataa huun terii threedots  main dil men bithaa kar tujhe ruksat na karuungaa haay ruksat na karuungaa mushkil hai teraa laut ke jaanaa mere ghar se are jaanaa mere ghar se tasaviir banaataa huun terii threedots ', 'correct_label': 'naushad', 'label': 6, 'split': 'test', 'title': 'tasaviir banaataa huun terii khuunejigar se', 'year': '1952'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "c ramchandra", "madan mohan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='shankarjaikishan' ref='naushad'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='naushad' in top3=['shankarjaikishan', 'c ramchandra', 'madan mohan']

### #82 — FAIL

- item: `{'lyrics': '  ko \taa  duniyaa ne hamen do din rahane na diyaa mil ke dene ko sazaa de dii 2 sahane na diyaa mil ke 2  duniyaa ne hamen do din rahane na diyaa mil ke  ko \taa  qisamat ke ishaare pe ik roz mile donon aramaan liye dil men ik saath khile donon par pyaar kii laharon men 2 bahane na diyaa mil ke sahane na diyaa mil ke  duniyaa ne hamen do din rahane na diyaa mil ke  ko \taa  bedard hai duniyaa bedard hai duniyaa badii bedard hai duniyaa qaanuun bhii maanaa hai kahiin ro ke manaane se insaaf bhii sunataa hai kahiin shor machaane se ab kaun sune dukhade 2 is dard bhare dil ke 2  duniyaa ne hamen do din rahane na diyaa mil ke dene ko sazaa de dii sahane na diyaa mil ke ', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'duniyaa ne hamen do din rahane na diyaa mil ke', 'year': '1946'}`
- output: `{"pred": "c ramchandra", "top3": ["c ramchandra", "naushad", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='c ramchandra' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='s d burman' in top3=['c ramchandra', 'naushad', 'shankarjaikishan']

### #83 — FAIL

- item: `{'lyrics': '  kar de zaraa ishaaraa tere naam kaa sahaaraa 2  chhaaii huii siyaahii bhatakaa huaa hai raahi sar par khadii tabaahii 2 terii razaa se chamake duubaa huaa sitaaraa tere naam kaa sahaaraa threedots  anjaam zindagii kaa dil ko daraa rahaa hai tuufaan aa rahaa hai 2 tuu hii use bachaa le duniyaa ne jis ko maaraa tere naam kaa sahaaraa threedots  kar de zaraa ishaaraa tere naam kaa sahaaraa ', 'correct_label': 'c ramchandra', 'label': 2, 'split': 'test', 'title': 'kar de zaraa ishaaraa', 'year': '0'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "naushad", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='c ramchandra'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='c ramchandra' in top3=['laxmikantpyarelal', 'naushad', 'shankarjaikishan']

### #84 — FAIL

- item: `{'lyrics': '  tere binaa jiyaa jaae naa  2 bin tere tere bin saajanaa saans men saans aae naa tere binaa threedots  jab bhii kayaalon men tuu aae mere badan se kushbuu aae mahake badan men rahaa na jaae rahaa jaae naa tere binaa threedots  reshamii raaten roz na hongii ye saugaaten roz na hongii zindagii tujh bin raas na aae raas aae naa tere binaa threedots ', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'tere binaa jiyaa jaae naa', 'year': '-1'}`
- output: `{"pred": "kalyanjianandji", "top3": ["kalyanjianandji", "r d burman", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='kalyanjianandji' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='r d burman' in top3=['kalyanjianandji', 'r d burman', 'shankarjaikishan']

### #85 — PASS

- item: `{'lyrics': ' rahman marahabaa marahabaa marahabaa marahabaa marahabaa ungalii jaisii dubalii ko nahiin chaahiye pharmacy  jiit kaa mantra hai take it easy policy chaar dinakii chaandanii yah javaanii fantasy  mahadevan jaanatii ho hindii men pyaar ke kitane akshar bol do merii khaatir pyaar ke do hii akshar  mahadevanjames jiit kaa mantra hai take it easy policy chaar dinakii chaandanii yah javaanii fantasy  rahman chitrahaar men bijalii ud gaii mahadevanjames rahman padhane par bhii fel ho gaye mahadevanjames rahman baap ne bolaa ammaa kaa dushhman mahadevanjames rahman paap kare aur gangaa nahaae mahadevanjames rahman  mahadevan jaanatii ho itanaa to badan men laakhon nadii bataa do mujhako itanaa kahaan main pyaar kii nadii  mahadevanjames jiit kaa mantra hai take it easy policy chaar dinakii chaandanii yah javaanii fantasy  nazar ke mil jaane se hii shiil to bhang  nahiin hotaa billiyaan na shaakaahaarii har koii raan nahiin hotaa bhalaaii kabhii auraton kii kraantii ke binaa nahiin hogii zamaanaa badal gayaa pyaare puraanii baat nahiin hogii  rahman filam dekhane vo nahiin aaii mahadevanjames rahman bagal siit par budhhdhii ho to mahadevanjames rahman mahadevanjames pyaar kare aur not bhii maange  rahman ungalii jaisii dubalii ko nahiin chaahiye faarmasii  jiit kaa mantra hai take it easy policy chaar dinakii chaandanii yah javaanii fantasy  mahadevanjames agar ladakii ko andhere men aankh maarii to hogaa kyaa agar aazaadii na ho to svarg milane se hogaa kyaa biis kii umr kaa jo hai khel saath men khelake hogaa kyaa', 'correct_label': 'a r rahman', 'label': 0, 'split': 'test', 'title': 'urvashi urvashi take it easy urvashi', 'year': '-1'}`
- output: `{"pred": "a r rahman", "top3": ["a r rahman", "madan mohan", "kalyanjianandji"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='a r rahman' ref='a r rahman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='a r rahman' in top3=['a r rahman', 'madan mohan', 'kalyanjianandji']

### #86 — FAIL

- item: `{'lyrics': '  ki chuudii nahiin ye meraa       chuudii nahiin ye meraa dil hai dekho dekho tuute naa       chuudii nahiin ye meraa    ki niiliipiilii rangbirangii pyaar kii ye saugaat       na na na na aise nahiin dhiiredhiire chupakechupake daalo inmen haath      kaanch hai kachchaa lekin inse ho sachchaa singaar       sonaa nahiin chaandii nahiin hiiraa nahiin motii nahiin qiimat inkii pyaar      phuulonsii naazuk hai dekho dekho dekho dekho tuute naa       chuudii nahiin ye meraa  la giggles achchhaa sach ki chuudii nahiin ye meraa   ki meraa pyaar hai chuudii jaisaa isakaa or na chhor      yahaan nahiin vahaan nahiin dekho kabhii tuute nahiin jiivan kii ye dor      inkii khankhan dil kii dhadakan hai meraa sangiit      suno zaraa socho zaraa nagamaa ye pyaar bharaa o mere man miit      laajavaab haan bemisaal dekho dekho tuute naa       chuudii nahiin ye meraa   la aa haa haa  2       terii chaahat terii ulafat hai merii manzil      ghere mujhe baanhen terii baandhe tujhe chaahen merii dil meraa teraa dil      koii bhii ho meraa hai tuu ai mere hamadam      gam mile khushii mile kahiin rahen kaise rahen bichhadenge na ham  ki phir bhii  la huun huun   ki jaaneman la huun huun ki  dekho dekho dekho tuute naa       chuudii nahiin ye meraa   ki chuudii nahiin ye  la teraa dil hai ki  dekho dekho tuute naa       chuudii nahiin ye meraa haan la giggles', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'chuudii nahiin ye meraa', 'year': '1971'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "kalyanjianandji", "annu malik"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='r d burman' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='s d burman' in top3=['r d burman', 'kalyanjianandji', 'annu malik']

### #87 — FAIL

- item: `{'lyrics': ' la  umr huii tumase mile phir bhii jaane kyon      aise lage jaise pahalii baar mile hain he  umr huii baag saje phir bhii jaane kyon      aise lage phool pahalii baar khile hain  la  ruup jagaa yuun bin sanvaare saajanaa main sanvar gaii 2      aaj lagaa yuun aaj lagaa yuun      motiyon se merii maang bhar gaii      kajaraa chhalake acharaa dhalake      aise lage jaise pahalii baar mile hain  he  sang tumhaaraa merii zindagii ko raas aa gayaa 2      paa ke sahaaraa paa ke sahaaraa      duur thhaa main apane paas aa gayaa      duniyaa saarii laage nyaarii      aise lage jaise pahalii baar mile hain  la  jhuum uthaa tan man men ek aisii baat aa gaii 2      jisakii thii lagan jisakii thii lagan      aaj vo milan kii raat aa gaii      alake lahake akhiyaan bakahe      aise lage jaise pahalii baar mile hain ', 'correct_label': 'c ramchandra', 'label': 2, 'split': 'test', 'title': 'umr huii tumase mile phir bhii jaane kyon', 'year': '1963'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "r d burman", "madan mohan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='c ramchandra'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='c ramchandra' in top3=['laxmikantpyarelal', 'r d burman', 'madan mohan']

### #88 — FAIL

- item: `{'lyrics': ' ye galiyaan ye chaubaaraa yahaan aanaa na dobaaraa ab ham to bhae paradesii ke teraa yahaan koii nahiin le jaa rangbirangii yaaden hansane rone kii buniyaaden mere haathon men bhariibharii chuudiyaan mujhe bhaa gaii harii harii chuudiyaan dekh milatii hain terimerii chuudiyaan tuune piisii vah mehandii rang laii morii gorii  havelii rach aaii terii aankh kyon laado bhar aaii tere baar  bhii bajegii shahanaaii saavan men baadal se kahanaa parades men terii bahanaa aa maan  milane  chale ham pardesh tere aangan men apanaa bachapan chhod chale kal bhii suuraj nikalegaa kal bhii panchhii gaaenge sab tujhako dikhaaii denge par ham na nazar aaenge aanchal men sajaa lenaa ham ko sapanon men bulaa lenaa ham ko dekh tuu na hamen bhulaanaa maano duur hamen hai jaanaa merii alhad sii anakhaliyaan  sadaa palakon men basaanaa jab bajane lagen baaje gaaje lagane lagen khaaliikhaalii us din tuu samajhanaa merii dolii uthii hai phuulon vaalii thode din ye naate the kabhii ham hansate gaate the', 'correct_label': 'laxmikantpyarelal', 'label': 4, 'split': 'test', 'title': 'ye galiyaan ye chaubaaraa yahaan aanaa na dobaaraa', 'year': '-1'}`
- output: `{"pred": "s d burman", "top3": ["s d burman", "c ramchandra", "madan mohan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='s d burman' ref='laxmikantpyarelal'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='laxmikantpyarelal' in top3=['s d burman', 'c ramchandra', 'madan mohan']

### #89 — FAIL

- item: `{'lyrics': '  ki \tjaaduugar 3 \tjaaduugar jaaduu kar jaaegaa kisii ko samajh nahiin aaegaa \to marajiinaa naach hasiinaa mushkil kar de sabakaa jiinaa 2 \tnahiin to nahiin to \tjaaduugar jaaduu kar threedots  \tnaachegii terii javaanii dekhegii duniyaa diivaanii 2 \thar chiiz hai mere bas men kyaa aag hai kyaa hai paanii 2 \tare chhuu mantar chhuu dekh idhar tuu \tpahan le inako le ye ghungharuu \tvaranaa gazab ho jaaegaa \te jaaduugar jaaduu kar threedots  aa \tmaanaa tujhe maine maanaa ho tuu jaaduugar hai diivaanaa 2 \tbebas mujhe kar diyaa yuun hairaan hai saaraa zamaanaa 2 \tbas had kar dii o bedardii batalaa kyaa hai terii marazii \tkab tak mujhe tadapaaegaa ki \tjaaduugar jaaduu kar jaaegaa aa  kisii ko samajh nahiin aaegaa  aa \tqismat kaa chamakaa sitaaraa tuune mujhe jab pukaaraa ki \tchupchaap tuu naachatii jaa jab tak karuun main ishaaraa 2 aa \to tere qadamon men sar hai tuu hai to phir kisakaa dar hai \tjo hogaa dekhaa jaaegaa ki \te jaaduugar jaaduu kar jaaegaa do \tkisii ko samajh nahiin aaegaa ki \to marajiinaa naach hasiinaa threedots ', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'jaaduugar jaaduu kar jaaegaa', 'year': '1980'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "annu malik", "r d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='r d burman' in top3=['laxmikantpyarelal', 'annu malik', 'r d burman']

### #90 — FAIL

- item: `{'lyrics': '  mere mahabuub qayaamat hogii aaj rusavaa terii galiyon men muhabbat hogii naam nikalegaa teraa hii lab se jaan jab is dilenaadaan se rukhasat hogii mere mahabuub   mere sanam ke dar se agar baadesabaa ho teraa guzar kahanaa sitamagar kuchh hai khabar teraa naam liyaa jab tak bhii jiyaa ai shamaa teraa paravaanaa jisase ab tak tujhe nafarat hogii aaj rusavaa     mere mahabuub qayaamat hogii aaj rusavaa terii galiyon men muhabbat hogii merii nazaren to gilaa karatii hain tere dil ko bhii sanam tujhase shikaayat hogii  terii galii main aataa sanam nagamaa vafaa kaa gaataa sanam tujhase sunaa na jaataa sanam phir aaj idhar aayaa huun magar ye kahane main diivaanaa khatm bas aaj ye vahashat hogii aaj rusavaa   merii tarah tuu aahen bhare tuu bhii kisii se pyaar kare aur rahe vo tujhase pare tuune o sanam dhaaye hain sitam to ye tuu bhuul na jaanaa ki na tujhape bhii inaayat hogii aaj rusavaa ', 'correct_label': 'laxmikantpyarelal', 'label': 4, 'split': 'test', 'title': 'mere mahabuub qayaamat hogii', 'year': '1964'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "naushad", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='r d burman' ref='laxmikantpyarelal'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='laxmikantpyarelal' in top3=['r d burman', 'naushad', 'laxmikantpyarelal']

### #91 — FAIL

- item: `{'lyrics': '  lallaa lallaa lorii duudh kii katorii duudh men bataashaa munnii kare tamaashaa  chhotiichhotii pyaarii sundar pariyon jaisii hai kisii kii nazar naa lage merii munnii aisii hai shahad se bhii miithii duudh se bhii gorii chupakechupake choriichorii chorii lallaa lallaa lorii threedots  kaarii rainaa ke maathe pe chamake chaand sii bindiyaa munnii ke chhotechhote nainon men khele nindiyaa sapanon kaa palanaa aashaaon kii dorii chupakechupake choriichorii chorii lallaa lallaa lorii threedots lallaa lallaa lorii duudh kii katorii duudh men bataashaa jiivan khel tamaashaa ', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'lallaa lallaa lorii duudh kii katorii', 'year': '1977'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "s d burman", "r d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='r d burman' in top3=['laxmikantpyarelal', 's d burman', 'r d burman']

### #92 — FAIL

- item: `{'lyrics': ' kaaryeshudaasii karneshumantrii bhojeshumaataa shayaneshurambhaa patnii pati ke lie de de apanii jaan aurat se badhake na koii yahaan sukh men bhii saath de dukh men bhii saath de ye bane sevikaa premikaa patnii pati ke lie threedots  tyaag aur samarpan hai patnii kaa naam ye pati kii sevaa kare subahoshaam vrat rakhe duaa de pujaaran bane sirf prem dhaage se jiivan bandhe mamataa kii chaandanii ye aisii roshanii jo har andheraa mitaa de ye nayaa ruup hai devii kaa patnii pati ke lie threedots  jo nahiin hai patnii to kyaa hai pati isakii mannaton kaa silaa hai pati jo kabhii bhii patnii se dhokhaa kare vo na zindagii men kabhii khush rahe jisane bhii hai kahii ye baat hai sahii samajho ise isako jaano ye to hai sundar mallikaa patnii pati ke lie threedots ', 'correct_label': 'annu malik', 'label': 1, 'split': 'test', 'title': 'patnii pati ke lie de de apanii jaan', 'year': '1999'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "madan mohan", "annu malik"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='annu malik'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='annu malik' in top3=['laxmikantpyarelal', 'madan mohan', 'annu malik']

### #93 — FAIL

- item: `{'lyrics': '       dol rahii hai dol rahii hai dol rahii hai naiyaa dol rahii hai naiyaa merii dol rahii hai naiyaa aa ho ho ho ho ho ho 3   aaj puunam kaa chaand khilaa hans rahii hai raat aaj chamakiilii laharon kaa chanchal hai gaat  2 main akelaa huun kisase kahuun apane man kii baat  ho kahaan jaauun kahaan jaauun kahaan jaauun re  2  merii raadhaa hai kaun main huun kisakaa kanhaiyaa merii raadhaa merii raadhaa hai kaun main huun kisakaa kanhaiyaa  dol rahii hai naiyaa merii dol rahii hai naiyaa dol rahii hai dol rahii hai dol rahii hai naiyaa dol rahii hai naiyaa merii dol rahii hai naiyaa ho \t', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'dol rahii hai naiyaa merii', 'year': '1946'}`
- output: `{"pred": "c ramchandra", "top3": ["c ramchandra", "shankarjaikishan", "s d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='c ramchandra' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='s d burman' in top3=['c ramchandra', 'shankarjaikishan', 's d burman']

### #94 — FAIL

- item: `{'lyrics': ' ku \to taak dhinaa dhin taa taa thaiyaa ko \ttaak dhinaa dhin 2 ku \to taak dhinaa dhin taa taa thaiyaa \tsun mere bandhuu sun mere bhaiyaa \tnaach nachaae rupaiyaa 2 \tkyon jii sach kahaa yaa jhuuth kahaa 2 ko \ttuune sach kahaa haan jii sach kahaa 2 ku \to taak dhinaa dhin threedots  \tladakii gariib kii ghar jo aae \tsaasuu jii naak chadhaae \toe maal kazaanaa saath jo laae \tsasurii sir pe bithaae \tkyuun naarii hai ek khilaunaa \tmaatii mol bike kyon sonaa \tek jagah tum dekh lo yaaron 2 \tkaisii dhuup aur chhaiyaa ko \tnaach nachaae rupaiyaa 2  ku \troz dahez ke hoven jhagade \tjalate hain naarii ke kapade \trapat karo darogaa akade \tmujarim ko kaun pakade \tbaat pate kii kahe diivaanaa \taaj nahiin hai vo zamaanaa \tik palade men naarii baithe 2 \taur duuje men rupaiyaa ko \tnaach nachaae rupaiyaa 2 ', 'correct_label': 'annu malik', 'label': 1, 'split': 'test', 'title': 'o taak dhinaa dhin  sun mere bandhuu  naach nachaae rupaiyaa', 'year': '1991'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "annu malik", "kalyanjianandji"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='r d burman' ref='annu malik'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='annu malik' in top3=['r d burman', 'annu malik', 'kalyanjianandji']

### #95 — FAIL

- item: `{'lyrics': ' tuu kahaan  ye bataa  is nashiilii raat men maane naa meraa dil diivaanaa haay re threedots maane naa meraa dil diivaanaa  he threedots badaa natakhat hai samaa    2 har nazaaraa hai javaan chhaa gayaa chaaron taraf  merii aahon kaa dhuaan dil meraa merii jaan naa jaanaa threedots tuu kahaan threedots  o o threedots aaii jab thandii havaa    2 maine puuchhaa jo pataa vo bhii kataraake gai aur bechain kiyaa pyaar se tuu mujhe de sadaa threedots tuu kahaan threedots  he threedots chaand taaron ne sunaa    2 in bahaaron ne sunaa dard kaa raag meraa  rahaguzaaron ne sunaa tuu bhii sun jaaneman aa bhii jaa  threedots tuu kahaan threedots  o o threedots pyaar kaa dekho asar    2 aae tum thaame jigar mil gai aaj mujhe  merii manachaahii dagar kyuun chhupaa ek jhalak phir dikhaa  threedots tuu kahaan threedots', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'tuu kahaan ye bataa is nashiilii raat men jaane naa meraa dil diivaanaa', 'year': '-1'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "annu malik", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='shankarjaikishan' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='s d burman' in top3=['shankarjaikishan', 'annu malik', 'laxmikantpyarelal']

### #96 — FAIL

- item: `{'lyrics': ' is intezaareshauk ko janamon kii pyaas hai ik shamaa jal rahii hai to vo bhii udaas hai  muhabbat aisii dhadakan hai jo samajhaaii nahiin jaatii \t 2 zubaan par dil kii bechainii kabhii laaii nahiin jaatii \t 2 muhabbat aisii dhadakan hai  chale aao chale aao taqaazaa hai nigaahon kaa\t 2 taqaazaa hai nigaahon kaa kisii kii aarzuu aise to thukaraaii nahiin jaatii\t 2 muhabbat aisii dhadakan hai jo samajhaaii nahiin jaatii \t 2 muhabbat aisii dhadakan hai  mere dil ne bichhaae hain sajade aaj raahon men\t 2 sajade aaj raahon men jo haalat aashiqii kii hai vo batalaaii nahiin jaatii\t 2 muhabbat aisii dhadakan hai jo samajhaaii nahiin jaatii     2 muhabbat aisii dhadakan hai ', 'correct_label': 'c ramchandra', 'label': 2, 'split': 'test', 'title': 'muhabbat aisii dhadakan hai', 'year': '1953'}`
- output: `{"pred": "annu malik", "top3": ["annu malik", "c ramchandra", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='annu malik' ref='c ramchandra'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='c ramchandra' in top3=['annu malik', 'c ramchandra', 'laxmikantpyarelal']

### #97 — FAIL

- item: `{'lyrics': '  chhiin sake to chhiin le khushiyaan mere nasiib kii 2 laayegii rang ek din aah kisii gariib kii  merii bahaar luut ke apanaa chaman basaaye jaa 2 gam pe mere nazar na kar shauq se muskuraaye jaa 2 aag lagaake phuunk de duniyaa kisii gariib kii 2 chhiin sake to chhiin le  threedots  dard jo mere diil kaa hai tere liiye davaa sahii 2 mere liye jo maut hai us men teraa bhalaa sahii 2 ye terii khushansiibiyaan hain kisii badanasiib kii 2 chhiin sake to chhiin le  threedots ', 'correct_label': 'c ramchandra', 'label': 2, 'split': 'test', 'title': 'chhiin sake to chhiin le', 'year': '1953'}`
- output: `{"pred": "naushad", "top3": ["naushad", "laxmikantpyarelal", "c ramchandra"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='naushad' ref='c ramchandra'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='c ramchandra' in top3=['naushad', 'laxmikantpyarelal', 'c ramchandra']

### #98 — FAIL

- item: `{'lyrics': '  gii \to o hoy  ko \tho ho ho ho \the he he he  gii \thoy \tzor lagaa ke  ko \thai yaa gii \tpair jamaa ke ko \thai yaa gii \tjaan ladaa ke ko \thai yaa  gii \tzor lagaa ke  \tpair jamaa ke \tjaan ladaa ke  ko  hai yaa hai \thai yaa hai \thai yaa hai \thai yaa hai  gii \to \taangan men baithii hai machheran terii aas lagaaye ko \thaay terii aas lagaaye gii \taramaanon aur aashaaon ke laakhon diip jalaaye ko \tlaakhon diip jalaaye  gii \taangan men baithii hai machheran terii aas lagaaye \taramaanon aur aashaaon ke laakhon diip jalaaye \tbholaa bachapan rastaa dekhe mamataa kair manaaye \tzor lagaa ke phenk machhere dhiil naa aane paaye  ko \thai yaa hai yaa \tzor lagaa ke  \thai yaa \tpair jamaa ke \thai yaa \tjaan ladaa ke \thai yaa  gii \tzor lagaa ke  \tpair jamaa ke \tjaan ladaa ke  ko \thai yaa hai \thai yaa hai \thai yaa hai \thai yaa hai \thai yaa hai  gii \to \tjanamjanam se apane sar par tuufaanon ke saaye ko \ttuufaanon ke saaye gii \tlaharen apanii hamajolii hain aur baadal hamasaaye ko \taur baadal hamasaaye  gii \tjanamjanam se apane sar par tuufaanon ke saaye \tlaharen apanii hamajolii hain aur baadal hamasaaye \tpriit kaa jaam hai jiivan apanaa kyaa sardii kyaa garmii \tapanii himmat kabhi naa tuute rut aaye rut jaaye  ko \thai yaa hai yaa \tzor lagaa ke  \thai yaa \tpair jamaa ke \thai yaa \tjaan ladaa ke \thai yaa  gii \tare \tzor lagaa ke  \tpair jamaa ke \tjaan ladaa ke  ko \thai yaa hai \thai yaa hai \thai yaa hai \thai yaa hai \thai yaa hai  gii \to ', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'zor lagaa ke hai yaa pair jamaa ke', 'year': '1952'}`
- output: `{"pred": "c ramchandra", "top3": ["c ramchandra", "a r rahman", "s d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='c ramchandra' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='s d burman' in top3=['c ramchandra', 'a r rahman', 's d burman']

### #99 — FAIL

- item: `{'lyrics': ' diivaanaa mujhako log kahe main samajhuun jag hai diivaanaa ho main samajhuun jag hai diivaanaa diivaanaa mujhako log kahe  hansataa hai koi suurat pe merii hansataa hai koi haalat pe merii hai kaun buraa maalik jaane anjaam se begaanaa  main yaar kii khaatir lut jaaun main yaar kii khaatir mit jaaun chhotaa hii sahii par dil hai badaa har haal pe begaanaa  diivaanaa mujhako log kahe main samajhuun jag hai diivaanaa ho main samajhuun jag hai diivaanaa divaanaa mujhako log kahe', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'diivaanaa mujhako log kahe main samajhuun jag hai diivaanaa', 'year': '1967'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "laxmikantpyarelal", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='r d burman' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='shankarjaikishan' in top3=['r d burman', 'laxmikantpyarelal', 'shankarjaikishan']

### #100 — FAIL

- item: `{'lyrics': ' jinake sar ho ishq kii chhaanv paanv ke niiche jannat hogii jinake sar ho ishq kii chhaanv  chal chainyyaa chainyyaa chainyyaa chainyyaa  sare ishq kii chhaanv chal chainyyaa chainyyaa paanv chalat chale chal chainyyaa chainyyaa paanv chalat chale chal chainyyaa chainyyaa  chal chainyyaa chainyyaa chainyyaa chainyyaa  vo yaar hai jo khushabuu kii tarah hai jisakii zubaan udruu kii tarah merii shaam raat merii qaayanaat vo yaar meraa sainyyaa sainyyaa  chal chainyyaa chainyyaa chainyyaa chainyyaa  gul posh kabhii itaraaye kahiin mahake to nazar aa jaaye kahiin taviiz banaake pahanuun use aayat kii tarah mil jaaye kahiin vo yaar hai jo iimaan kii tarah meraa nagamaa vahii meraa kalamaa vahii meraa nagamaa nagamaa meraa kalamaa kalamaa  yaar misaaleos chale paanv kii tale firadaus chale kabhii daal daal kabhii paat paat main havaa pe dhuundhuun usake nishaan  sare ishq kii chhaanv chal chainyyaa chainyyaa paanv chalat chale chal chainyyaa chainyyaa paanv chalat chale chal chainyyaa  chal chainyyaa chainyyaa chainyyaa chainyyaa   threedots  main usake ruup kaa saudaaii vo dhuup chhaanv saa harjaai vo shokh nazar badalataa hai main rang ruup kaa saudaaii  jinake sar ho ishq kii chhaanv paanv ke niiche jannat hogii jinake sar ho ishq kii chhaanv  chal chainyyaa chainyyaa chainyyaa chainyyaa  sare ishq kii chhaanv chal chainyyaa chainyyaa paanv chalat chale chal chainyyaa chainyyaa paanv chalat chale chal chainyyaa  chal chainyyaa chainyyaa chainyyaa chainyyaa ', 'correct_label': 'a r rahman', 'label': 0, 'split': 'test', 'title': 'chainyyaa chainyyaa', 'year': '0'}`
- output: `{"pred": "madan mohan", "top3": ["madan mohan", "s d burman", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='madan mohan' ref='a r rahman'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='a r rahman' in top3=['madan mohan', 's d burman', 'laxmikantpyarelal']

### #101 — FAIL

- item: `{'lyrics': '  akele hii akele chalaa hai kahaan kahegaa kyaa kahegaa ye mausam javaan naa jaa naa jaa ho aajaa aajaa o raahii alabele hamasafar bhii koii saath lele  duur parvat pe kyuun ek badalii jhukii kyuun pavan chalatechalate chaman men rukii ek tanahaa kalii se ye kyuun kah gaii akele hii akele threedots  thandiithandii havaaon kii baat maan le kyuun nazaare tujhe roke ye raaz jaan le kaun detaa aavaaz pahachaan le akele hii akele threedots ', 'correct_label': 'kalyanjianandji', 'label': 3, 'split': 'test', 'title': 'akele hii akele chalaa hai kahaan', 'year': '1970'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "shankarjaikishan", "annu malik"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='kalyanjianandji'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='kalyanjianandji' in top3=['laxmikantpyarelal', 'shankarjaikishan', 'annu malik']

### #102 — FAIL

- item: `{'lyrics': '  ki \tek thaa abdul rahamaan la \tsachchii ki \thaan \tek thaa abdul rahamaan ek thii abdul rahamaniyaa \tab main huun ik manamaujii tuu ban jaa manamaujaniyaan ho ho ho ho la \tsunsun mere manamaujii main huun terii sajaniyaan \ttuu kar de ek ishaaraa main chhoduun saarii duniyaa ho ho ho  ki \tmain diivaanaa aavaaraa mujhako log kahen naakaaraa \tzaraa soch le \tbesahaare ko banaayaa tuune apanaa sahaaraa \tzaraa soch le la \tho  maine taajamahal kab maangaa  2 \ttuune pyaar diyaa jab maangaa 2 \tsun shaahajahaan mere dil ke \tmain huun dil se terii shaahajahaniyaan 3 ki \tek thaa abdul rahamaan threedots la \tab tuu hai ik manamaujii main terii manamaujaniyaan do \tho ho ho ho  la \traajaa mujhe kaanch kii tuu chuudii laa de 2 \tsone ke naa chaandii ke main maanguun vaade \tdukh sukh teremere aadheaadhe \traajaa mujhe kaanch kii tuu chuudii laa de ki \tgariibon kii mohabbat zamaane se niraalii \tiraade badebade aur jeben khaaliikhaalii 2 la \ttuu jo pyaar se mujhe dede \tmujhe pyaarii hai terii doaniyaan \tterii doaniyaan ho terii doaniyaan ki \tik thaa abdul rahamaan threedots la \tab tuu hai ik threedots  ki \tteraa ek nazaaraa kaafii hai mere lie 2 \tzulfon kaa sahaaraa kaafii hai mere lie \taankhon kaa ishaaraa kaafii hai mere lie ho ho \tteraa ek nazaaraa kaafii hai mere lie la \tho raajaa dekh liyaa tujhe jab se 2 \tmaine chaand naa dekhaa tab se 2 \ttuune duniyaa hii dil kii badal dii do \tai mohabbat terii meharabaaniyaan 3 ki \tik thaa abdul rahamaan threedots la \tsunsun mere manamaujii threedots ', 'correct_label': 'madan mohan', 'label': 5, 'split': 'test', 'title': 'ek thaa abdul rahamaan ek thii abdul rahamaniyaa', 'year': '1962'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "kalyanjianandji", "r d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='madan mohan'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='madan mohan' in top3=['laxmikantpyarelal', 'kalyanjianandji', 'r d burman']

### #103 — PASS

- item: `{'lyrics': '  tumhaare pyaar men ham beqaraar ho ke chale shikaar karane ko aae shikaar ho ke chale shikaar karane ko threedots  tumhen qariib se dekhaa to dil ko haar diyaa tumhaarii shok adaa ne hamen to maar diyaa har ek baat pe ham to nisaar ho ke chale shikaar karane ko threedots  tumhaarii aankh mohabbat kii baat kahatii hai tumhen bhii kisii kii talaash rahatii hai ye raaz jaan gae raazadaar ho ke chale shikaar karane ko threedots  na apanaa hosh na apanii kabar kahaan hain ham isii kaa naam mohabbat hai ai mere hamadam tumhaare kuuche se diivaanaavaar ho ke chale shikaar karane ko threedots ', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'tumhaare pyaar men ham  shikaar karane ko aae', 'year': '1968'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "kalyanjianandji", "madan mohan"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='shankarjaikishan' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='shankarjaikishan' in top3=['shankarjaikishan', 'kalyanjianandji', 'madan mohan']

### #104 — FAIL

- item: `{'lyrics': ' merii bhiigiibhiigii sii palakon pe rah gae jaise mere sapane bikhar ke jale man teraa bhii kisii ke milan ko anaamikaa tuu bhii tarase merii bhiigii threedots  tujhe bin jaane bin pahachaane mainne hriday se lagaayaa par mere pyaar ke badale men tuune mujhako ye din dikhalaayaa jaise birahaa kii ritu mainne kaatii tadapake aanhen bharbhar ke jale man teraa threedots  aag se naataa naarii se rishtaa kaahe man samajh na paayaa mujhe kyaa huaa thaa ik bevafaa se haay mujhe kyon pyaar aayaa terii bevafaaii pe hanse jag saaraa galiigalii guzare jidhar se jale man teraa threedots', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'merii bhiigiibhiigii sii palakon pe rah gaye', 'year': '1973'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "kalyanjianandji", "s d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='shankarjaikishan' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='r d burman' in top3=['shankarjaikishan', 'kalyanjianandji', 's d burman']

### #105 — FAIL

- item: `{'lyrics': ' ra\tjhilamil sitaaron kaa aangan hogaa \trimajhim barasataa saavan hogaa \taisaa sundar sapanaa apanaa jiivan hogaa la\tjhilamil sitaaron kaa aangan hogaa   ra\tprem kii galii men ek chhotaasaa ghar banaaenge \tkaliyaan naa mile naa sahii kaanton se sajaaenge \tbagiyaa se sundar vo ban hogaa \trimajhim barasataa saavan hogaa la\tjhilamil sitaaron kaa aangan hogaa  ra\trimajhim barasataa saavan hogaa  la\tterii aankhon se saaraa sansaar main dekhuungii \tdekhuungii is paar yaa us paar main dekhuungii \tnainon ko teraa hii darshan hogaa \trimajhim barasataa saavan hogaa ra\tjhilamil sitaaron kaa aangan hogaa  la\trimajhim barasataa saavan hogaa  ra\tphir to mast havaaon ke ham jhonke ban jaaenge la\tnainaa sundar sapanon ke jharokhe ban jaaenge \tman aashaaon kaa darpan hogaa do\trimajhim barasataa saavan hogaa \taisaa sundar sapanaa apanaa jiivan hogaa      jhilamil sitaaron kaa aangan hogaa rimajhim barasataa saavan hogaa aisaa sundar sapanaa apanaa jiivan hogaa jhilamil sitaaron kaa aangan hogaa   terii aankhon se saaraa sansaar main dekhuungii dekhuungii is paar yaa us paar main dekhuungii nainon ko teraa hii darshan hogaa rimajhim barasataa saavan hogaa jhilamil sitaaron kaa aangan hogaa   roengii ye aankhen phir bhii main to muskuraauungii dukh ke tuufaanon se bhii main na ghabaraauungii jab saath mere meraa saajan hogaa rimajhim barasataa saavan hogaa jhilamil sitaaron kaa aangan hogaa ', 'correct_label': 'laxmikantpyarelal', 'label': 4, 'split': 'test', 'title': 'jhilamil sitaaron kaa aangan hogaa', 'year': '1970'}`
- output: `{"pred": "kalyanjianandji", "top3": ["kalyanjianandji", "r d burman", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='kalyanjianandji' ref='laxmikantpyarelal'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='laxmikantpyarelal' in top3=['kalyanjianandji', 'r d burman', 'laxmikantpyarelal']

### #106 — PASS

- item: `{'lyrics': ' aaj mausam badaa beiimaan hai badaa beiimaan hai aaj mausam aane vaalaa koii tuufaan hai koii tuufaan hai aaj mausam  kyaa huaa hai huaa kuchh nahiin hai baat kyaa hai pataa kuchh nahiin hai mujhase koii kataa ho gaii to is men merii kataa kuchh nahiin hai kuubasuurat hai tuu rut javaan hai aaj mausam badaa beiimaan hai  kaaliikaalii ghataa dar rahii hai thandii aahen havaa bhar rahii hai sabako kyaakyaa gumaan ho rahe hain har kalii ham pe shak kar rahii hai phuulon kaa dil bhii kuchh badagumaan hai  ai mere yaar ai husn vaale dil kiyaa mainne tere havaale terii marzii pe ab baat thaharii jiine de chaahe tuu maar daale tere haathon men ab merii jaan hai', 'correct_label': 'laxmikantpyarelal', 'label': 4, 'split': 'test', 'title': 'aaj mausam badaa beiimaan hai aaj mausam', 'year': '-1'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "c ramchandra", "s d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='laxmikantpyarelal' ref='laxmikantpyarelal'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='laxmikantpyarelal' in top3=['laxmikantpyarelal', 'c ramchandra', 's d burman']

### #107 — FAIL

- item: `{'lyrics': '  har dil men nafarat bharii hai koii dil saaf nahiin hai maalik terii saarii duniyaa men kahiin insaaf nahiin hai  tuu mile to puuchhuun tujhase kyaa ye hai nyaay teraa duniyaa ko die ujaale aur mujhako diyaa andheraa tuu mile to puuchhuun threedots  nekii karane vaalon ko to milatii yahaan buraaii hai kudagarzii ke tuufaanon men duub gaii sachchaaii hai kisii kii nagarii bas gaii dekho kisii kaa lut gayaa deraa tuu mile to puuchhuun threedots  kitanii umangen laae the ham dil men sametakar le jaa le aa rahe hain hasaraten qafan men lapetakar ab kisape karen bharosaa jab tuune hii munh pheraa duniyaa ko die ujaale threedots  terii jhuuthii duniyaa kii ham sab diivaaren tod chale tujhe mubaarak terii duniyaa ham to duniyaa chhod chale mar kar bhii na bhuul sakenge ham ehasaan ye teraa tuu mile to puuchhuun threedots ', 'correct_label': 'laxmikantpyarelal', 'label': 4, 'split': 'test', 'title': 'har dil men nafarat bharii hai  tuu mile to puuchhuun', 'year': '1976'}`
- output: `{"pred": "naushad", "top3": ["naushad", "laxmikantpyarelal", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='naushad' ref='laxmikantpyarelal'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='laxmikantpyarelal' in top3=['naushad', 'laxmikantpyarelal', 'shankarjaikishan']

### #108 — FAIL

- item: `{'lyrics': '  le jaa merii duaaen le jaa parades jaane vaale le jaa merii duaaen jaakar bhulaa na denaa dil se merii wafaaen le jaa merii duaaen 2 le jaa merii duaaen le jaa parades jaane vaale le jaa merii duaaen  tuu hii suhaag meraa tuu hii singaar meraa kar luungii zindagii bhar main intazaar teraa ummiid ke sitaare dekho na duub jaaen le jaa merii duaaen le jaa merii duaaen le jaa parades jaane vaale le jaa merii duaaen  sunate hain ye sitamagar duniyaa nahiin kisii kii jisane bhii kii muhabbat dushaman huii usii kii aisaa na ho ke saajan ham tumase mil na paaen le jaa merii duaaen le jaa merii duaaen le jaa parades jaane vaale le jaa merii duaaen ', 'correct_label': 'naushad', 'label': 6, 'split': 'test', 'title': 'le jaa merii duaaen le jaa parades jaane vaale', 'year': '1951'}`
- output: `{"pred": "c ramchandra", "top3": ["c ramchandra", "naushad", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='c ramchandra' ref='naushad'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='naushad' in top3=['c ramchandra', 'naushad', 'shankarjaikishan']

### #109 — FAIL

- item: `{'lyrics': ' kaise kahuun kaise ho tum koii nahiin jaise ho tum jaan bhii tum aur dil bhii tum sab kuchh ho aise ho tum raahon men baahon men aahon men tum hii tum  tum ho jahaan main huun vahiin tum bin sanam main kuchh nahiin tum ho hasiin tum mahazabiin tum naazaniin tum dilanashiin mere dil men tum ho tum kaise kahuun kaise ho threedots  saagar bhii saahil bhii tum sab kuchh ho aise ho tum  kaliyon men phuulon men taaron men tum hii tum tum jab mile main kho gaii tum par fidaa main ho gaii tum zindagii tum taazagii tum roshanii tum chaandanii mere dil men tum ho tum hii tum kaise kahuun kaise ho threedots  giiton men raagon men saazon men tum hii tum kaise kahuun kaise ho threedots ', 'correct_label': 'annu malik', 'label': 1, 'split': 'test', 'title': 'kaise kahuun kaise ho tum  tum hii tum', 'year': '1997'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "madan mohan", "annu malik"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='r d burman' ref='annu malik'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='annu malik' in top3=['r d burman', 'madan mohan', 'annu malik']

### #110 — FAIL

- item: `{'lyrics': ' o manachalii kahaan chalii  2 dekh dekh dekh dekh mujh se na sharamaa ek ek ek main huun bhanvaraa aur tuu kalii o manachalii threedots  hothon pe leke teraa naam aai hai rang bharii shaam phuulon se chhalake hain jaam bhanvaron ne dil liye thaam aise men he he ho e he ho aise men tod ke prem kii dorii o gorii  chakorii  tuu kahaan chalii threedots  duniyaa se nahiin darenge ham tum mulaaqaate karenge aajaa do baate karenge rangiin barasaaten karenge ye sach hai e he o o e he o o ye sach hai main huun ek diivaanaa na jaanaa  na maanaa  tuu kahaan chalii threedots  rut aisii aai hui hai badalii sii chhaai hui hai tuu kyon sharamaai hui hai mujhase ghabaraai hui hai pyaar men e he o o e he o o pyaar men yaar se aankh churaake chhupaake  bachaake  tuu kahaan chalii threedots', 'correct_label': 'laxmikantpyarelal', 'label': 4, 'split': 'test', 'title': 'o manachalii kahaan chalii', 'year': '-1'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "s d burman", "annu malik"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='r d burman' ref='laxmikantpyarelal'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='laxmikantpyarelal' in top3=['r d burman', 's d burman', 'annu malik']

### #111 — PASS

- item: `{'lyrics': ' unakii zulfen unake chehare se hataa sakataa nahiin dil kii betaabii kisii suurat chhupaa sakataa nahiin kitanii dilakash hain muhabbat kii javaan majabuuriyaan saamane manzil hai aur paanv badhaa sakataa nahiin  merii zindagii men aate  to kuchh aur baat hotii  2 ye nasiib jagamagaate  to kuchh aur baat hotii  2  kaii baar mil chukii hain ye hasiinhasiin nigaahen 2 vo hii beqaraariyaan hain na milii kushii kii raahen mere dil se dil milaate  to kuchh aur baat hotii  2 merii zindagii men threedots  mujhe kyaa garaz kisii se hanse phuul yaa sitaare 2 hain merii nazar men phiike ye javaanjavaan nazaare agar aap muskaraate  to kuchh aur baat hotii  2 merii zindagii men threedots  ye kushii rahe salaamat yuun hii jashn ho suhaanaa 2 jise sun rahii hai duniyaa mere dil kaa hai taraanaa mere saath tum bhii gaate  to kuchh aur baat hotii  2 merii zindagii men threedots ', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'unakii zulfen unake chehare se  merii zindagii men aate', 'year': '1968'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "madan mohan", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='shankarjaikishan' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='shankarjaikishan' in top3=['shankarjaikishan', 'madan mohan', 'laxmikantpyarelal']

### #112 — PASS

- item: `{'lyrics': '  jaaiye hamase kafaa ho jaaiye dushmanon kaa aasaraa ho jaaiye  chaand se lipatii huii hai chaandanii mahakaa mahakaa hai yah mausam shabanamii aapakii mahasuus hotii hai kamii aaj to mere kudaa ho jaaiye nahiin to jaaiye hamase kafaa ho jaaiye  aazama liijiye hamaaraa hausalaa kar liyaa hai hamane bhii ye faisalaa ham na chhodenge vafaa kaa silasilaa aap chaahe bevafaa ho jaaiye jaaiye hamase kafaa ho jaaiye  aap kii fitarat kaa hai saaraa qusuur aap kii aadat men shaamil hai guruur aap ye yakiin kar len huzuur aap jaane kyaa se kyaa ho jaaiye  dushmanon kaa aasaraa ho jaaiye jaaiye hamase kafaa ho jaaiye ', 'correct_label': 'madan mohan', 'label': 5, 'split': 'test', 'title': 'jaaiye hamase kafaa ho jaaiye', 'year': '1980'}`
- output: `{"pred": "madan mohan", "top3": ["madan mohan", "r d burman", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='madan mohan' ref='madan mohan'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='madan mohan' in top3=['madan mohan', 'r d burman', 'laxmikantpyarelal']

### #113 — FAIL

- item: `{'lyrics': ' dil kaa haal sune dilavaalaa siidhii sii baat na mirch masaalaa kahake rahegaa kahanevaalaa dil kaa haal sune dilavaalaa  chhote se ghar men gariib kaa betaa main bhii huun maan ke nasiib kaa betaa 2 ranjogam bachapan ke saathii aandhiyon men jalii jiivan baatii bhuukh ne hain bade pyaar se paalaa dil kaa haal sune dilavaalaa  haay karuun kyaa suurat aisii gaanthake puure chor ke jaisii  2 chalataa phirataa jaanake ek din binaa dekhe pahachaan ke ek din baandhake le gayaa pulisavaalaa dil kaa haal sune dilavaalaa  buudhe daarogaa ne chashme se dekhaa     2 aage se dekhaa piichhe se dekhaa uupar se dekhaa niiche se dekhaa bolaa ye kyaa kar baithe ghotaalaa haay ye kyaa kar baithe ghotaalaa ye to hai thaanedaar kaa saalaa   dil kaa haal sune dilavaalaa  gam se abhii aazaad nahiin main kush magar aabaad nahiin main  2 manzil mere paas khadii hai paanv men lekin bedii padii hai taanga detaa hai daulatavaalaa   dil kaa haal sune dilavaalaa  sun lo magar ye kisii se na kahanaa tinake kaa leke sahaaraa na bahanaa 2 bin mausammal haar na gaanaa aadhii raat ko machchil laanaa varanaa pakad legaa pulisavaalaa dil kaa haal sune dilavaalaa', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'dil kaa haal sune dilavaalaa siidhii sii baat na mirch masaalaa', 'year': '1955'}`
- output: `{"pred": "madan mohan", "top3": ["madan mohan", "laxmikantpyarelal", "kalyanjianandji"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='madan mohan' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='shankarjaikishan' in top3=['madan mohan', 'laxmikantpyarelal', 'kalyanjianandji']

### #114 — FAIL

- item: `{'lyrics': ' aae tum yaad mujhe gaane lagii har dhadakan kushabuu laai pavan mahakaa chandan aae tum yaad mujhe threedots  jis pal nainon men sapanaa teraa aae us pal mausam pe menhandii rach jaae   2 aur tuu ban jaaye jaise dulhan aae tum yaad mujhe threedots  jab main raaton men taare ginataa huun aur tere kadamon kii aahat sunataa huun  2 lage mujhe har taaraa teraa darapan aae tum yaad mujhe threedots  har pal man meraa mujhase kahataa hai jisakii dhun men tuu khoyaa rahataa hai   2 bhar de phuulon se usakaa daaman aae tum yaad mujhe threedots', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'aaye tum yaad mujhe gaane lagii har dhadakan', 'year': '1975'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "shankarjaikishan", "annu malik"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='s d burman' in top3=['laxmikantpyarelal', 'shankarjaikishan', 'annu malik']

### #115 — PASS

- item: `{'lyrics': ' la  jaanaa hai hamen to jahaan qaraar mile ki  luutenge raahon men jahaan bahaar mile la ki  jaanaa hai  la  jab tak chaluun chalatii rahuun main        baahon ke saaye men tere ki  jaanaa hamen kahaan yah bhii nahiin sochen       niind sii aankhon men bhare la  manzil hamen mile na mile       teraa pyaar mile la  jaanaa hai hamen to threedots  ki  mujhe duniyaa men jiine kaa sahaaraa       kaafii hai dil kii lagii la  kuchh bhii naa chaahuun rahe mere liye       yah tere honthon kii hansii ki  saarii duniyaa se lenaa hamen kyaa       hamako yaar mile la  jaanaa hai hamen to threedots  la  tere sang piyaa padate hain mere       niilagagan pe qadam ki  tum ho mere to dharatii ghataa pe       raaj hamaaraa hai sanam la  ho aaj nazaare sar jhukaake       sau sau baar mile la  jaanaa hai hamen to threedots', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'jaanaa hai hamen to jahaan qaraar mile', 'year': '1973'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "laxmikantpyarelal", "kalyanjianandji"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='r d burman' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='r d burman' in top3=['r d burman', 'laxmikantpyarelal', 'kalyanjianandji']

### #116 — FAIL

- item: `{'lyrics': '  ko  mahalaa mahalaa mahaa lambolaa 2 la  rainaa soyii soyii nainaa jaagii jaagii       jaane kyaa ho aage dam dam damru bolaa2      mahalaa mahalaa mahaa lambolaa 2  raa rastaa ghere raat khadii hai      rastaa ghere raat khadii hai      paayal bedii ban gaii hai      rastaa ghere raat khadii hai      paayal bedii ban gaii hai      ho tan dolaa man dolaa dambolaa       rainaa soyii soyii threedots       tushimaa aise chal rahii hai       tushimaa aise chal rahii hai       nadiyaa jaise jal rahii hai       tushimaa aise chal rahii hai       nadiyaa jaise jal rahii hai      o taaj banii re sholaa dambolaa      rainaa soyii soyii threedots      mahalaa mahalaa mahaa lambolaa 2  sa  royegaa jiivan maut hansegii       royegaa jiivan maut hansegii       kisii ko naagan aaj dasegii raa royegaa jiivan maut hansegii       kisii ko naagan aaj dasegii      o bairan ne muunh kholaa dambolaa ', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'rainaa soyii soyii nainaa jaagii jaagii', 'year': '197'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "s d burman", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='r d burman' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='s d burman' in top3=['r d burman', 's d burman', 'laxmikantpyarelal']

### #117 — FAIL

- item: `{'lyrics': '      ho merii sonii merii tamannaa jhuuth nahiin hai meraa pyaar diiwaane se ho gaii galatii jaane do yaar i love you i love you  merii sonii merii tamannaa jhuuth nahiin hai meraa pyaar diiwaane se ho gaii galatii jaane do yaar i love you i love you  aake merii aankhon men tum dekho in men har ik ada tumhaarii hai kahane ko ye dil hai meraa lekin dhadakan men sadaa tumhaarii hai tum se hai chain meraa tum se hai meraa qaraar  laa laa laa i love you i love you  mere sonaa merii tamannaa jhuuth nahiin hai meraa pyaar diiwaanii se ho gaii galatii jaane do yaar i love you i love you  tadapatii huun bahut naa tadapaao achchhaa baabaa chalo ham hii haare tum ne agar dil se mujhe chaahaa tum bhii to ho sanam mujhe pyaare mere qariib aao zaraa sun bhii lo dil kii pukaar  laa laa laa i love you i love you  merii sonii merii tamannaa jhuuth nahiin hai meraa pyaar diiwaane se ho gaii galatii jaane do yaar i love you laa laa laa i love you laa laa laa i love you ', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'merii sonii merii tamannaa', 'year': '1973'}`
- output: `{"pred": "annu malik", "top3": ["annu malik", "r d burman", "a r rahman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='annu malik' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='r d burman' in top3=['annu malik', 'r d burman', 'a r rahman']

### #118 — FAIL

- item: `{'lyrics': ' mere piyaa chhede jiyaa dhiire se aa ke thandii hawaa mere piyaa   dil se gaii gam kii ghadii jhuum rahii hai zindagii  2 phuule khile dil bhii mile jab se dayaa tuune  apanii kataa  mere piyaa   sone chalen jaane kahaan taaron se jhilamil kaaravaan  2 lagane lagiin aankhen zaraa bigadii zamaane ne lautaa diyaa   mere piyaa chhede jiyaa dhiire se aa ke thandii hawaa mere piyaa', 'correct_label': 'madan mohan', 'label': 5, 'split': 'test', 'title': 'mere piyaa chhede jiyaa dhiire se aa ke', 'year': '1953'}`
- output: `{"pred": "naushad", "top3": ["naushad", "s d burman", "c ramchandra"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='naushad' ref='madan mohan'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='madan mohan' in top3=['naushad', 's d burman', 'c ramchandra']

### #119 — PASS

- item: `{'lyrics': '  chaahaa thaa banuun pyaar kii raahon kaa devataa mujhako banaa diyaa hai gunaahon kaa devataa  ye zindagii to kvaab hai jiinaa bhii hai nashaa do ghuunt maine pii lie to kyaa buraa kiyaa rahane do jaam saamane sab kuchh yahii to hai har gamazadaa ke aansuon kaa devataa mujhako banaa diyaa threedots  qismat to chal rahii hai hamase chaal har qadam ek chaal ham bhii chal die to ho gayaa sitam ab to chalenge chaal ham qismat ke saath bhii aisaa banaa sansaar kii raahon kaa devataa mujhako banaa diyaa threedots  hogaa jahaan bhii ruup to puujaa hii jaaegaa chaahe jahaan bhii phuul ho man ko lubhaaegaa hokar rahegaa zindagii men pyaar ek baar bas kar rahegaa dil men nigaahon kaa devataa mujhako banaa diyaa threedots ', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'chaahaa thaa banuun pyaar kii raahon kaa devataa', 'year': '1967'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "madan mohan", "r d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='shankarjaikishan' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='shankarjaikishan' in top3=['shankarjaikishan', 'madan mohan', 'r d burman']

### #120 — FAIL

- item: `{'lyrics': ' paradesii re jaatejaate jiyaa moraa liye jaa jaa re paradesii re  dil par gam kii ghataa jab chhaae jii bhar aae dil kii baat honthon par aae niind naa aae niind liye jaa yaa diye jaa paradesii rethreedots  kar ke ishaaraa pyaaraapyaaraa diyaa sahaaraa ban kar ke gamon se pyaaraa kiyaa kinaaraa jaa ke aane kaa vaadaa kiye jaa paradesii rethreedots', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'paradesii re jaatejaate jiyaa moraa liye jaa', 'year': '1950'}`
- output: `{"pred": "naushad", "top3": ["naushad", "laxmikantpyarelal", "c ramchandra"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='naushad' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='s d burman' in top3=['naushad', 'laxmikantpyarelal', 'c ramchandra']

### #121 — FAIL

- item: `{'lyrics': ' ummiid bharaa panchhiithaa khoj rahaa sajanii kahataa thaa yahii panchhiihaay dekho re gaii sajanii haay dekho re gaii sajanii2  taaron bharii rajaniiaanchal ko fasaa re 2 puuch rahii hansaketuu kisako pukaare tuu kisako pukaare nainan men niir bharedard sambhaale ummiid bharaa panchhii threedots  rajaniimohe na sataadil na jalaaitanaa bataa kahaan gaii sajaniio kahaan gaii sajanii2 aansuu hain mere nainon kenaa ho sakii  buunde 2 dil men lagii aag lagaaman men milan ke ho man men milan ke haalat meretujhe taras na aaye ummiid bharaa panchhii threedots', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'ummiid bharaa panchhii thaa khoj rahaa sajanii', 'year': '1946'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "s d burman", "naushad"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='shankarjaikishan' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='s d burman' in top3=['shankarjaikishan', 's d burman', 'naushad']

### #122 — FAIL

- item: `{'lyrics': ' bachanaa ai hasiinon lo main aa gayaa  hay bachanaa ai hasiinon lo main aa gayaa  husn ka aashiq husn ka dushman  apanii ada hai yaaron se judaa  koras  hai ho  hai bachanaa threedots   hai duniya men nahiin hai aaj meraa saa divaanaa  pyaar vaalon kii jubaan pe hai meraa hii taraanaa  sabakii rang bharii aankhon pe aaj chamak rahaa hai meraa hii nashaa  koras  hai ho  hai bachana threedots   jaam milaten hain adab se shaam detii hai salamii  giit jhukate hai labon pe saaz karate hain gulaamii  ho koi paradaa ya badashaah aaj to sab hain mujhape fidaa  koras  hai ho  hai bachanaa threedots  ek hangaamaa uthaa duun main to jaaun jidhar se  jiit leta huun dilon ko ek halkii si najar se  mahabuubon kii mahafil men aaj chhaayii hai chhaayii hai meri hii ada  koras  hai ho   hai bacahanaa threedots', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'bachanaa ai hasiinon lo main aa gayaa', 'year': '-1'}`
- output: `{"pred": "naushad", "top3": ["naushad", "laxmikantpyarelal", "r d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='naushad' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='r d burman' in top3=['naushad', 'laxmikantpyarelal', 'r d burman']

### #123 — FAIL

- item: `{'lyrics': ' tuu hii re tuu hii re tere binaa main kaise jiyuun aajaa re aajaa re yuun hii tadapaa naa tuu mujhako jaan re jaan re in saanson men bas jaa tuu chaand re chaand re aajaa dil kii zamiin pe tuu  chaahat hai agar aake mujhase mil jaa tuu yaa phir aisaa kar dharatii se milaa de mujhako tu hii re tuu hii re tere binaa main kaise jiyuun aajaa re aajaa re yuun hii tadapaa naa tuu mujhako  in saanson kaa dekho tum paagalapan ke aaye nahiin inhen chain mujhase ye bolii main raahon men terii  apane bichhaa duun ye nain in uunche pahaadon se jaan de duungaa main  gar tuum naa aaii kahiin tum udhar jaan ummiid merii jo todo idhar ye jahaan chhoduu main maut aur jindagii tere haathon men de diyaa re  aaii re aaii re le main aaii huun tere liye todaa re todaa re har bandhan ko pyaar ke liye jaan re jaan re aajaa tujhamen samaa jaauun main dil re dil re teri saanson men bas jaauun main  chaahat hai agar aake mujhase mil jaa tuu yaa phir aisaa kar dharatii se milaa de mujhako tu hii re tuu hii re tere binaa main kaise jiyuun aajaa re aajaa re yuun hii tadapaa naa tuu mujhako  aa threedots  sau baar bulaae main sau baar aauun  ik baar jo dil diyaa ik aankh roye to dujii bolo  soyegii kaise bhalaa in pyaar kii raahon men patthar hain kitane  un sab ko hii paar kiyaa ik nadii huun main chaahat bharii aaj milane  saagar ko aaii yahaan sajanaa sajanaa aaj aansuu bhii mithe lage  tu hii re tuu hii re tere binaa main kaise jiyuun aajaa re aajaa re yuun hii tadapaa naa tuu mujhako jaan re jaan re in saason men bas jaa tuu chaand re chaand re aajaa dil kii zamiin pe tuu  pal pal pal pal vakt to bitaa jaaye re zaraa bol zaraa bol vaqt se ke vo tham jaaye re aaii re aaii re le main aaii huun tere liye jaan re jaan re aajaa tujhamen samaa jaauun main', 'correct_label': 'a r rahman', 'label': 0, 'split': 'test', 'title': 'tuu hii re tuu hii re tere binaa main kaise jiyuun', 'year': '-1'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "a r rahman", "annu malik"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='r d burman' ref='a r rahman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='a r rahman' in top3=['r d burman', 'a r rahman', 'annu malik']

### #124 — FAIL

- item: `{'lyrics': ' panchhii nadiyaa pavan ke jhonke koii sarahad naa inhen roke sarahaden insaanon ke lie hain socho tumane aur maine kyaa paayaa insaan ho ke panchhii nadiyaa threedots  jo ham donon panchhii hote tairate ham is niil gagan men pankh pasaare saarii dharatii apanii hotii apane hote saare nazaare khulii fizaaon men udate apane dil men ham saaraa pyaar samo ke panchhii nadiyaa threedots  jo main hotii nadiyaa aur tum pavan ke jhonke to kyaa hotaa pavan ke jhonke nadii ke tan ko jab chhuute hain laharen hii laharen banatii hain ham donon jo milate to kuchh aisaa hotaa sab kahate ye lahar lahar jahaan bhii jaae isako naa koii toke panchhii nadiyaa threedots ', 'correct_label': 'annu malik', 'label': 1, 'split': 'test', 'title': 'panchhii nadiyaa pavan ke jhonke', 'year': '2000'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "r d burman", "kalyanjianandji"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='annu malik'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='annu malik' in top3=['laxmikantpyarelal', 'r d burman', 'kalyanjianandji']

### #125 — PASS

- item: `{'lyrics': ' chaand chhupaa aur taare duube raat gazab kii aaii husn chalaa hai ishq se milane zulm kii badalii chhaaii  tuut padii hai aandhii gam kii aaj pavan hai paagal kaanp rahii hai dharatii saarii chiikh rahe hain baadal duniyaa ke tuufaan hazaaron husn kii ik tanahaaii  maut kii naagan aaj khadii hai raah men phan phailaaye jangaljangal naach rahe hain shaitaanon ke saae aaj kudaa khaamosh hai jaise bhuul gayaa ho kudaaii  ghor andheraa mushkil raahen kadamkadam pe dhokhe aaj mohabbat ruk na sakegii chaahe kudaa bhii roke raahevafaa men piichhe hatanaa pyaar kii hai rusvaaii  paar nadii ke yaar kaa deraa aaj milan hai teraa odh le tuu leharon kii chunarii baandh le mauj kaa seharaa dole men manjhadhaar ke hogii aaj terii vidaaii  duub ke in uunchii leharon men naiyyaa paar lagaa le ulfat ke tuufaan men zindaa rahate hain marane vaale jiitejii sansaar men kisane pyaar kii manzil paayii  tere dil ke khuun se hogaa laal chenaab kaa paanii duniyaa kii taariikh men likhii jaayegii yeh qurbaanii sohanii aur mahivaal ne apanii ishq men jaan ganvaayii       hamaare pyaar ke kisse sunaaye jaayenge yeh giit saare zamaane men gaaye jaayenge ham na honge fasaana hogaa 2 aane vaale ko aanaa hogaa jaane vaale ko jaanaa hogaa  ', 'correct_label': 'naushad', 'label': 6, 'split': 'test', 'title': 'chaand chhupaa aur taare duube raat gazab kii aaii', 'year': '-1'}`
- output: `{"pred": "naushad", "top3": ["naushad", "shankarjaikishan", "madan mohan"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='naushad' ref='naushad'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='naushad' in top3=['naushad', 'shankarjaikishan', 'madan mohan']

### #126 — FAIL

- item: `{'lyrics': ' dukhiyaare nainaa dhuundhen piyaa ko  nisadina karen pukaar 2 dukhiyaare nainaa  phir kyaa aaengiin vo raaten 2 laut gaiin hain jo baaraaten 2 biite din aur bichhadaa saathii 2 bahatii nadii kii dhaar dukhiyaare nainaa threedots  raah men nainaa diyaa jalaaen 2 aap jalen aur jiyaa jalaaen 2 jis se jiivan bhii jal jaae 2 vo kaisii jaladhaar dukhiyaare nainaa threedots', 'correct_label': 'madan mohan', 'label': 5, 'split': 'test', 'title': 'dukhiyaare nainaa dhuundhen piyaa ko', 'year': '1952'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "shankarjaikishan", "kalyanjianandji"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='madan mohan'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='madan mohan' in top3=['laxmikantpyarelal', 'shankarjaikishan', 'kalyanjianandji']

### #127 — FAIL

- item: `{'lyrics': '  aa palakon men aa sapane sajaaaa  behosh raaton kii nindiyaa churaa aa palakon men aa threedots  jis raaginii ko bhiigii huii chaandanii gaa rahii hai mere dhadakate dil se usii kii sadaa aa rahii hai aa palakon men aa threedots  yah pyaas kaisii hai aakar ye jalate sitaaron se puuchh le bechainiyaan har pal machalatii bahaaron se puuchh le aa palakon men aa threedots ', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'aa palakon men aa', 'year': '1955'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "madan mohan", "c ramchandra"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='shankarjaikishan' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='s d burman' in top3=['shankarjaikishan', 'madan mohan', 'c ramchandra']

### #128 — FAIL

- item: `{'lyrics': ' tere sadake balam na kar koii gam ye samaa ye jahaan phir kahaan ho tere sadake balam na kar koii gam  din hain suhaane phir kaun jaane aae na aae bahaar tuu gam ko piile dam bhar ko jiile duniyaa kaa kyaa aaitabaar ho jii piyaa duniyaa kaa kyaa aitabaar tere sadake balamthreedots  kaanton men daaman ulajhe na saajan phuulon men hansake guzaar thodii hansii hai thodii khushii hai dukh zindagii men hazaar ho jii piyaa dukh zindagii men hazaar tere sadake balamthreedots  naiyaa milan kii maujen pavan kii kahatii hain mujhako pukaar gaataa chalaa chal hansataa chalaa chal jiivan kii nadiyaa ke paar ho jii piyaa jiivar kii nadiyaa ke paar tere sadake balam na kar koii gam ye samaa ye jahaan phir kahaan ', 'correct_label': 'naushad', 'label': 6, 'split': 'test', 'title': 'tere sadake balam na kar koii gam', 'year': '-1'}`
- output: `{"pred": "madan mohan", "top3": ["madan mohan", "s d burman", "naushad"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='madan mohan' ref='naushad'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='naushad' in top3=['madan mohan', 's d burman', 'naushad']

### #129 — FAIL

- item: `{'lyrics': ' dil kyaa chaahe kaise boluun baat ye dil kii aake labon pe  kyon ruk jaae main kyaa jaanuun 2 dil kyaa chaahe kaise boluun  maange dil duaa jisakii vo kushii tuu hai main to jism huun merii zindagii tuu hai 2 tuu mujhase bichhade to saans merii tham jaae 2 baat ye dil kii threedots  tujhako kyaa pataa tere ishq men kyaa hai kyaa junuun hai ye kyaa nashaa kyaa mazaa hai 2 tuu dekhe hansake to dard davaa ban jaae 2 baat ye dil kii threedots  chhodake teraa dar yahaan kahaan jaauun dil kii bebasii kaise tujhako samajhaauun 2 tujhako naa dekhuun to chain kahiin naa aae 2 baat ye dil kii threedots', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'dil kyaa chaahe kaise boluun', 'year': '1985'}`
- output: `{"pred": "annu malik", "top3": ["annu malik", "laxmikantpyarelal", "s d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='annu malik' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='r d burman' in top3=['annu malik', 'laxmikantpyarelal', 's d burman']

### #130 — FAIL

- item: `{'lyrics': '  aaj shiishe men baarbaar unhen dil kii suurat dikhaaii detii hai apanii suurat nazar nahiin aatii merii suurat dikhaaii detii hai  dil men ek jaanetamannaa ne jagah paaii hai aaj gulashan men nahiin ghar men bahaar aaii hai  aa gayaa aa gayaa mere tasavvur men koii paradaanashiin 2 aaj har chiiz nazar aatii hai mujhako hasiin kyaa karuun main badii dilakash merii tanhaaii hai aaj gulashan men nahiin threedots  bahakiibahakii nashaaehusn men khoiikhoii jaise kyaalon kii rangiin rubaaii koii dil ke shiishe men parii ban ke utar aaii hai aaj gulashan men nahiin threedots  husn ke saamane izahaarevafaa hai mushkil 2 kaash chhup kar hii vo sun le meraa naalaaedil jisane pyaar kii manzil mujhe dikhalaaii hai aaj gulashan men nahiin threedots ', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'aaj shiishe men baarbaar  dil men ek jaanetamannaa', 'year': '1964'}`
- output: `{"pred": "naushad", "top3": ["naushad", "shankarjaikishan", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='naushad' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='s d burman' in top3=['naushad', 'shankarjaikishan', 'laxmikantpyarelal']

### #131 — PASS

- item: `{'lyrics': '  anahonii ko honii kar den honii ko anahonii 2 ek jagah jab jamaa hon tiinon amar akabar enthonii anahonii ko honii threedots  ek ek se bhale do do se bhale tiiin duulhaa dulhan saath nahiin baajaa hai baaraat nahiin are kuchh darane kii baat nahiin ye milan kii rainaa hai koii gam kii raat nahiin yaaron hanso banaa rakhii hai kyuun ye suurat ronii 2 ek jagah jab jamaa threedots  ek ek se bhale do do se bhale tiiin shammaa ke paravaanon ko is ghar ke mehamaanon ko 2 pahachaano anjaanon ko kaise baat matalab kii samajhaauun diivaanon ko sapan salone le ke aaii hai ye raat salonii 2 ek jagah jab jamaa threedots ', 'correct_label': 'laxmikantpyarelal', 'label': 4, 'split': 'test', 'title': 'anahonii ko honii kar den  amar akabar enthonii', 'year': '1977'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "r d burman", "kalyanjianandji"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='laxmikantpyarelal' ref='laxmikantpyarelal'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='laxmikantpyarelal' in top3=['laxmikantpyarelal', 'r d burman', 'kalyanjianandji']

### #132 — FAIL

- item: `{'lyrics': ' o mere dil ke chain  chain aae mere dil ko duaa kiijiye  apanaa hii saayaa dekh ke tum jaane jahaan sharamaa gae abhii to ye pahalii manzil hai tum to abhii se ghabaraa gae meraa kyaa hogaa socho to jaraa haay aise naa aanhen bharaa kiijiye o mere dil ke chain threedots  aapakaa aramaan aapakaa naam meraa taraanaa aur nahiin in jhukatii palako ke sivaa dil kaa thikaanaa aur nahiin janchataa hii nahiin aankho men koi dil tumako hii chaahe to kyaa kiijiye o mere dil ke chain threedots  yuun to akelaa hii aqasar gir ke sambhal sakataa huun main tum jo pakad lo haath meraa duniyaa badal sakataa huun main maangaa hai tumhen duniyaa ke liye ab kud hii sanam faisalaa kiijiye o mere dil ke chain threedots', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'o mere dil ke chain chain aaye mere dil ko duaa kiijiye', 'year': '-1'}`
- output: `{"pred": "s d burman", "top3": ["s d burman", "shankarjaikishan", "annu malik"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='s d burman' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='r d burman' in top3=['s d burman', 'shankarjaikishan', 'annu malik']

### #133 — PASS

- item: `{'lyrics': ' jab chaahaa yaaraa tumane aankhon se maaraa tumane honthon se zindaa kar diyaa are tumhaarii marzii pe chal rahen hain kataa hamaarii kyaa ho jab chaahaa yaaraa tumane threedots  chalo jii ham bure sahii chalo jii ham jhuuthe hain  magar inahiin nigaahon se hazaaron dil tuute hain 2 are kasam se kahanaa hamaarii suurat nahiin hai pyaarii kyaa hothreedots jab chaahaa yaaraa tumanethreedots  samajh sako to hamasafar hamen tum apanaa jaano  are udhar nahiin idhar chalo kabhii to kahanaa maano 2 are lipat aake puuchhen ke aage marzii ab hai hamaarii kyaa hothreedots jab chaahaa yaaraa tumanethreedots', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'jab chaahaa yaaraa tumane aankhon se maaraa tumane', 'year': '-1'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "laxmikantpyarelal", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='r d burman' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='r d burman' in top3=['r d burman', 'laxmikantpyarelal', 'shankarjaikishan']

### #134 — FAIL

- item: `{'lyrics': '  le le dard paraayaa threedots aa aa aa  le le dard paraayaa kar de duur gam kaa saayaa terii khushii tujhako mil hii jaayegii  2  khushii aur ko deke tuu le le gam terii haar bhii jiit se kuchh na kam 2 jo kisiike kaam aayaa jis ne roton ko hansaayaa usakii tat bhii kinaare lag hii jaayegii le le threedots  kiyaa apanii khaatir to vo kyaa kiyaa kiyaa kud ko khushahaal to vo kyaa kiyaa 2 tuu bahaar ban jaa saarii duniyaan pe chhaa murjhaaii kalii bhii khil hii jaayegii le le threedots   tuu duniyaan men apanaa nishaan chhod jaa rahe yaad vo daastaan chhod jaa 2 jo ho zindagii se haaraa ban jaa us kaa sahaaraa terii manzil bhii tujhe mil hii jaayegii le le threedots ', 'correct_label': 'madan mohan', 'label': 5, 'split': 'test', 'title': 'le le dard paraayaa', 'year': '1957'}`
- output: `{"pred": "s d burman", "top3": ["s d burman", "naushad", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='s d burman' ref='madan mohan'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='madan mohan' in top3=['s d burman', 'naushad', 'shankarjaikishan']

### #135 — FAIL

- item: `{'lyrics': ' ai kaash chalate mil ke ye tiin raahii dil ke chaand aur main aur tuu uu uu  chalaa chalaa saa raat kaa jaaduu koii na ho har suu udatii ho khushabuu tum ho ham hon kam se kam ho faasale dil ke ai kaash chalate mil ke threedots  nazar pe ho na dil pe ho qaabuu koii na ho har suu udatii ho khushabuu chalate chalate jaa nikalate paas manzil ke ai kaash chalate mil ke threedots ', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'ai kaash chalate mil ke', 'year': '1960'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "shankarjaikishan", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='r d burman' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='s d burman' in top3=['r d burman', 'shankarjaikishan', 'laxmikantpyarelal']

### #136 — FAIL

- item: `{'lyrics': ' ham matavale naujavaan manzilon ke ujaale log kare badanami kaise ye duniyaa vaale  kare bhalai ham bure banen har dam is jahan ki rit nirali  pyar ko samajhe hay re hay sitam ham matavale naujavaan threedots  ham dhul men lipate sitare ham zarre nahin hain angare nadan hai jahan samajhega kahan ham naujavan ke ishare  jab jab jhum ke nikale ham jaan ke pad jayen lale log karen badanami kaise ye duniyaa vale ham matavale naujavaan threedots  ham rote dilon ko hansa den dukh dadr ki aag bujhaa den bechain nazar betaab jigar ham sabako ko gale se laga len ham man mauji shahazade dukhiyon ke rakhavale log karen badanami kaise ye duniyaa vaale karen bhalai ham bure bane har dam is jahan ki rit nirali  pyar ko samajhe hay re hay sitam  ham matavale naujavaan manzilon ke ujale log karen badanami kaise ye duniyaa vale', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'ham matavaale naujavaan manzilon ke ujaale', 'year': '1959'}`
- output: `{"pred": "s d burman", "top3": ["s d burman", "kalyanjianandji", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='s d burman' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='shankarjaikishan' in top3=['s d burman', 'kalyanjianandji', 'laxmikantpyarelal']

### #137 — PASS

- item: `{'lyrics': '  ruutheruuthe piyaa manaauun kaise 2 aaj na jaane baat huii kyaa kyon ruuthe mujhase jab tak vo na bolen mujhase main samajhuun kaise ruutheruuthe piyaa threedots  vo baithe hain kuchh aise shaadii men dulhan jaise kyaa ban ke dulhaa main jaauun aur unakii maang sajaauun lambii dulhan thiganaa duulhaa 2 jodii jamen kaise ruutheruuthe piyaa threedots  kyaa mujhase hasiin hain qitaaben piyaa jinako pyaar se thaame main nain milaanaa chaahuun par nain milaa naa paauun sautan chashmaa biich men aae 2 nain milen kaise ruutheruuthe piyaa threedots ', 'correct_label': 'kalyanjianandji', 'label': 3, 'split': 'test', 'title': 'ruutheruuthe piyaa manaauun kaise', 'year': '1974'}`
- output: `{"pred": "kalyanjianandji", "top3": ["kalyanjianandji", "madan mohan", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='kalyanjianandji' ref='kalyanjianandji'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='kalyanjianandji' in top3=['kalyanjianandji', 'madan mohan', 'laxmikantpyarelal']

### #138 — PASS

- item: `{'lyrics': ' bhanvare kii gunjan hai meraa dil  kabase sanbhaale rakhaa hai dil  tere liye tere liye\t2\t   \t\t2  mujhe kabase thii pyaar kii justajuu  merii zindagaanii men hai tuu hii tuu\t2 main aayaa huun duniyaa men tere liye mere dil men jhuume terii aarzuu  bhanvare kii gunjan hai meraa dil threedots  gagan se bhii uunchaa meraa pyaar hai  tujhii par mituungaa ye iqaraar hai\t\t2 tuu itanaa samajh le mere hamasafar tere pyaar se meraa sansaar hai bhanvare kii gunjan hai meraa dil threedots  ', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'bhanvare kii gunjan hai meraa dil', 'year': '1971'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "s d burman", "madan mohan"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='shankarjaikishan' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='shankarjaikishan' in top3=['shankarjaikishan', 's d burman', 'madan mohan']

### #139 — FAIL

- item: `{'lyrics': '     premnagar men basane waalo apanii jiit pe hansane waalo priit hansaaye priit rulaaye priit milaaye priit hii saath chhudaaye   hansmukh phuulo ye mat bhuulo 2 o ', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'premnagar men basane waalo', 'year': '1949'}`
- output: `{"pred": "s d burman", "top3": ["s d burman", "madan mohan", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='s d burman' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='shankarjaikishan' in top3=['s d burman', 'madan mohan', 'shankarjaikishan']

### #140 — FAIL

- item: `{'lyrics': ' baadal jo barase to bhiige tum bhiige ham  3 tapatip tapatip guunj rahii hai buundon kii saragam ho baadal jo barase to bhiige tum bhiige ham   phuul kaliyaan bhiigebhiige raste galiyaan bhiigebhiige   2 baarish ne dho daale hain duniyaa ke saare gam ahaa haa  baadal jo barase to   thandiithandii giiliigiilii ye havaaen hain nashiilii  2 aag lagaa de jo paanii men aisaa hai mausam haay baadal jo barase to ', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'baadal jo barase to bhiige tum bhiige ham', 'year': '1993'}`
- output: `{"pred": "a r rahman", "top3": ["a r rahman", "shankarjaikishan", "r d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='a r rahman' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='r d burman' in top3=['a r rahman', 'shankarjaikishan', 'r d burman']

### #141 — FAIL

- item: `{'lyrics': ' gir gayaa jhumakaa girane do kho gaii mundarii khone do ud gaii chunarii udane do kaahe ka dar hai baalii umar hai chhodo bahaanaa naa naa  gir gayaa jhumakaa girane do kho gaii mundarii khone do ud gaii chunarii udane do kaahe ka dar hai baalii umar hai are chhodo bahaanaa naa naa  gir gayaa jhumakaa girane do  aajaa naa naa aajaa aajaa aajaa naa naa haan haan naa naa naa naa  poochhen ye sab mujhe aaii kahaan se tuu hasiinaa rang bhare honthon kaa rang bhalaa kisane chhiinaa kahanaa chaman se phuulon ne meraa ruup churaake rakh liyaa uii kyaa huaa chubh gayaa kaantaa chubhane do khul gaya gajaraa khulane do mit gayaa kajaraa mitane do kaahe kaa dar hai baalii umar hai are chhodo bahaanaa uunhuun   gir gayaa jhumakaa  sharabatii aankhon se do ghuunth piine do mujhako reshamii zulfon ke saaye men jiine do mujhako main maan jaatii lekin dhadakate dil ne manaa kar diyaa haay haay kyaa huaa ho gaii mushkil hone do khil gaiin kaliyaan khilane do aa gaye bhanware aane do kaahe kaa dar hai baalii umar hai are chhodo bahaanaa naa naa  gir gayaa jhumakaa  aahistaa aahistaa chhedo dilon kii kahaanii kyaa karuun maane naa merii jawaanii diiwaanii aise diiwaane tum nahiin the ye tumako kya ho gayaa gayaa kyaa huaa chal gayaa jaaduu chalane do are sudhabudha khoii khone do aa gayaa koii aane do kaahe kaa dar hai baalii umar hai chhodo bahaanaa naa naa naa ', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'gir gayaa jhumakaa girane do', 'year': '1973'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "a r rahman", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='r d burman' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='s d burman' in top3=['r d burman', 'a r rahman', 'laxmikantpyarelal']

### #142 — FAIL

- item: `{'lyrics': '  so \tai duubaa re duubaa aankhon men terii dil meraa duubaa re 2 \tduubaa re duubaa aankhon men terii dil meraa duubaa re \ttujhako hasiinaa  ko \the he \tmaine banaayaa ko \tho ho \ttujhako hasiinaa maine banaayaa merii mahabuubaa re a \tai duubaa re duubaa aankhon men merii dil teraa duubaa re \tduubaa re duubaa aankhon men merii dil teraa duubaa re \tnaa romeo hai ko \the he \tnaa to hai majanuun ko \tho ho \tnaa romeo hai naa to hai majanuun tuu hai ajuubaa re so \tai duubaa re duubaa aankhon men merii dil teraa duubaa re 2 a \tai duubaa re duubaa aankhon men merii dil teraa duubaa re 2  ko \tho  so \tterii sahelii ko \toy taubaa so \tlagatii pahelii ko \toy taubaa so \tkyon hai akelii \toy taubaa \tpuuchho to zaraa  a \tladakaa ye ladakaa ko \toy taubaa a \tvillain kaa jhadakaa ko \toy taubaa a \tkyon aise tadapaa \tpuuchho to zaraa so \tsaarii umar main ko \the he so \tkarataa rahuungaa ko \tho ho so \tsaarii umar main karataa rahuungaa bas terii puujaa re \tai duubaa re duubaa aankhon men terii dil meraa duubaa re a \tai duubaa re duubaa aankhon men merii dil teraa duubaa re  a \tteriimerii jodii ko \tvaah re vaah a \tye love story ko \tvaah re vaah a \thogii naa puurii \tjaa maan jaa  so \ttuu hai kanvaarii ko \tvaah re vaah so \tmain huun kunvaaraa ko \tvaah re vaah so \tdil tujhape haaraa \tvaah re vaah \taa paas aa  a \ttuu naa milaa to ko \the he a \tmain dhuundh luungii ko \tho ho a \ttuu naa milaa to main dhuundh luungii mahabuub duujaa re so \thoy he duubaa re duubaa aankhon men terii dil meraa duubaa re 2 a \tduubaa re duubaa aankhon men merii dil teraa duubaa re so \ttujhako hasiinaa ko \the he so \tmaine banaayaa ko \tho ho a \tnaa romeo hai naa to hai majanuun tuu hai ajuubaa re so \tduubaa duubaa duubaa \tduubaa re duubaa aankhon men terii dil meraa duubaa re \tduubaa duubaa a \tai duubaa re duubaa aankhon men merii dil teraa duubaa re so \tare re \tai duubaa re duubaa aankhon men terii dil meraa duubaa re a \tai duubaa re duubaa aankhon men merii dil teraa duubaa re so \tare duubaaduubaa re ', 'correct_label': 'annu malik', 'label': 1, 'split': 'test', 'title': 'ai duubaa re duubaa aankhon men terii dil meraa duubaa re', 'year': '2003'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "r d burman", "annu malik"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='annu malik'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='annu malik' in top3=['laxmikantpyarelal', 'r d burman', 'annu malik']

### #143 — FAIL

- item: `{'lyrics': '  ra nanhe munne bachche terii mutthii men kyaa hai  2 aa mutthii men hai taqadiir hamaarii ko mutthii men hai taqadiir hamaarii aa ham ne qismat ko bas men kiyaa hai ko ham ne qismat ko bas men kiyaa hai ra bholii bhalii matavaalii aankhon men kyaa hai 2 aa aankhon men jhuume ummiidon kii divaalii ko aankhon men jhuumen ummiidon kii divaalii aa aanevaalii duniyaa kaa sapanaa sajaa hai ko aanevaalii duniyaa kaa sapanaa sajaa hai threedots  ra bhiikh men jo motii mile loge yaa na loge zindagii ke aansuuon kaa bolo kyaa karoge 2 aa bhiikh men jo motii mile to bhii ham naa lenge ko bhiikh men jo motii mile to bhii ham naa lenge aa zindagii ke aansuuon kii maalaa pahanenge ko zindagii ke aansuuon kii maalaa pahanenge aa mushkilon se ladate bhidate jiine men mazaa hai ko mushkilon se ladate bhidate jiine men mazaa hai  ra ham se na chhupaao bachcho hamen bhii bataao aanevaale duniyaa kaisii hogii samajhaao 2 aa aanevaale duniyaa men sab ke sar pe taaj hogaa ko aanevaale duniyaa men sab ke sar pe taaj hogaa aa na bhuukhon kii bhiid hogii na dukhon kaa raaj hogaa ko na bhuukhon kii bhiid hogii na dukkon kaa raaj hogaa aa badalegaa zamanaa ye sitaaron pe likhaa hai ko badalegaa zamanaa ye sitaaron pe likhaa hai threedots ', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'nanhe munne bachche terii mutthii men kyaa hai', 'year': '1954'}`
- output: `{"pred": "naushad", "top3": ["naushad", "c ramchandra", "madan mohan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='naushad' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='shankarjaikishan' in top3=['naushad', 'c ramchandra', 'madan mohan']

### #144 — FAIL

- item: `{'lyrics': '  duniyaa men dilawaale honge hazaaron phir bhii hamaarii wafaa dilarubaa yaad karoge   2 hamane bhii apanaa mohabbat bharaa dil jaao tumhen de diyaa tum bhii kyaa yaad karoge   pyaar men aakir hamaare  kaam aa gayiin wo dard bharii aahen dard bharii aahen   2 aapake qadamon ke niiche jalatii thiin raahen jalatii thiin raahen is dhuup men tumako zulafon kaa saayaa jaise ki hamane diyaa saajanaa yaad karoge  duniyaa men dilawaale honge hazaaron phir bhii hamaarii wafaa dilarubaa yaad karoge   beqaraar main bhii huun lekin lab tharatharaaye aankh jhuk jaaye aankh jhuk jaaye   2 tum rahe aanchal samete tan ko churaaye phir bhii udaa laayaa baahon men tumako jhonkaa mere pyaar kaa ye hawaa yaad karoge  hamane bhii apanaa mohabbat bharaa dil jaao tumhen de diyaa tum bhii kyaa yaad karoge   ham mile to raah kyaa hai chalatii hai manzil sang hamen leke sang hamen leke   2 dekhanaa chhuute na bainyaan milake gale se milake gale se pal men andheraa hai pal men ujaalaa ye bekudii kii ghataa baalamaa yaad karoge  duniyaa men dilawaale honge hazaaron phir bhii hamaarii wafaa dilarubaa yaad karoge tum bhii kyaa yaad karoge', 'correct_label': 'laxmikantpyarelal', 'label': 4, 'split': 'test', 'title': 'duniyaa men dilawaale honge hazaaron', 'year': '1969'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "s d burman", "r d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='shankarjaikishan' ref='laxmikantpyarelal'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='laxmikantpyarelal' in top3=['shankarjaikishan', 's d burman', 'r d burman']

### #145 — FAIL

- item: `{'lyrics': ' prem kaa pinjaraa hogayaa suunaaman kaa panchhii chuut gayaa aajao bichhade saathii aajaakaahe hamse ruuth gayaa prem kaa pinjaraa hogayaa suunaaman kaa panchhii chuut gayaa  chain hamaaraa le gayaa koiiaansuu hamako de gayaa le gayaa koii sukh kii duniyaaniind hamaarii le gayaa  bhii hai aakaash bhii haitaqadiir kaa taara tuut gayaa prem kaa pinjaraa threedots  tuut gaiituut gaiituut gaii merii phulavaarii dans gaiidans gaiidans gaii haay yaad tumhaarii tuut gaii merii phulavaarii raha gaii aahenraha gaye aansuu sab kuchh koii luut gayaa prem kaa pinjaraa threedots  ham tume itanaa yaad karenkabhii tum bhii to hamako yaad karo is duniyaa ko tumane ujaadaaaake use aabaad karo ab main huun  duubatii naiyyaakisaka sahaaraa tuut gayaa prem kaa pinjaraa threedots', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'prem kaa pinjaraa ho gaaya suunaa', 'year': '-1'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "naushad", "madan mohan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='s d burman' in top3=['laxmikantpyarelal', 'naushad', 'madan mohan']

### #146 — FAIL

- item: `{'lyrics': '  aa \t botal se ik baat chalii hai \tkaag udaa ke raat chalii hai  2 \tho \ttu du du tu tu du du tu tu du tu tu 2 ra \tho \tbotal se ik baat chalii hai aa \ttu du du ra \tkaag udaa ke raat chalii hai  aa \taaj kii may bahut miithii hai \taaj to aankh milaa ke piinaa ra \tchaand kii misarii ghul jaayegii \tchaand se honth lagaa ke piinaa  aa \tho \ttu du du tu tu du du tu tu du tu tu 2 ra \tho \tbotal se ik baat chalii hai \tkaag udaa ke raat chalii hai aa \tho \tbotal se ik baat chalii hai \tkaag udaa ke raat chalii hai  ra \tvaadon waalii raat aayii hai \taaj kii raat inakaar naa karanaa aa \tapane din aur raat naa puuchho \ttumase jiinaa tumape maranaa  \ttu du du tu tu du du tu tu du tu tu 2 ra \tho \tbotal se ik baat chalii hai aa \ttu du du ra \tkaag udaa ke raat chalii hai aa \tbotal se ik baat chalii hai \tkaag udaa ke raat chalii hai do \tla la la la la ', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'botal se ek baat chalii hai', 'year': '1978'}`
- output: `{"pred": "madan mohan", "top3": ["madan mohan", "c ramchandra", "a r rahman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='madan mohan' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='r d burman' in top3=['madan mohan', 'c ramchandra', 'a r rahman']

### #147 — PASS

- item: `{'lyrics': ' dil use do jo jaan de de jaan use do jo dil de de  1 ye pyaar ke nazaare hain dekh lo jidhar ab naachatii hai duniyaa khushii kaa hai asar lo khatm huaa hai ye aaj kaa safar ab hogii suhaanii vo kal kii sahar dil use threedots  2 jo sochate rahoge to kuchh na milegaa jo chupake rahoge to kaam na banegaa jo dil men jaloge to aramaan rahegaa jo badhate chaloge to raastaa milegaa dil use threedots  3 vo gunchaa nahiin hai jo khilanaa na jaane vo baadesabaa kyaa jo chalanaa na jaane vo bijalii nahiin jo chamakanaa na jaane vo insaan nahiin jo tadapanaa na jaane dil use threedots', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'dil use do jo jaan de de jaan use do jo dil de de', 'year': '-1'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "madan mohan", "annu malik"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='shankarjaikishan' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='shankarjaikishan' in top3=['shankarjaikishan', 'madan mohan', 'annu malik']

### #148 — PASS

- item: `{'lyrics': ' dil de de dil le le dil le le dil de de mujhe pyaar lagataa hai pyaaraa main huun adaaon kaa maaraa kisii ne aankh churaaii kisii ne dil men utaaraa hasiin hai samaan muhabbaten javaan kariib aa ke kah rahiin mujhase javaaniyaan  saarii umar main rahuun atharaa saal kaa dil de de threedots  yuu mat mariinaa ma ma ma ma re dyuu natii natiinaa na na na na re jaanam ye umr to aatii hai ek baar isamen hain shokhiyaan isamen hotaa hai pyaar rok luun vaqt ko ye umar naa dhale zindagii bhar sanam silasilaa ye chale milatii rahen hasiinon se hasiin nishaaniyaan saarii umar main threedots  chandaa kii chaandanii rab kii jaaduugarii hogii hogii kahiin sapanon kii vo parii kyaa use hai pataa kyaa use hai khabar dhuundhatii hai use har jagah ye nazar kabhii kahiin mile vo to banen kahaaniyaan saarii umar main threedots ', 'correct_label': 'annu malik', 'label': 1, 'split': 'test', 'title': 'dil de de dil le le  saarii umar main rahuun atharaa saal kaa', 'year': '2002'}`
- output: `{"pred": "annu malik", "top3": ["annu malik", "laxmikantpyarelal", "kalyanjianandji"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='annu malik' ref='annu malik'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='annu malik' in top3=['annu malik', 'laxmikantpyarelal', 'kalyanjianandji']

### #149 — FAIL

- item: `{'lyrics': ' main teri nazar ka suruur huun tujhe yaad ho ke na yaad ho  tere paas rahake bhi dur huun  tujhe yaad ho ke na yaad ho  main teri nazar ka suruur huun   mujhe aankh se to giraa diyaa  kaho dil se bhi kya bhulaa diyaa   2 teri aashiqii ka guruur huun  tujhe yaad ho ke na yaad ho  main teri nazar ka threedots  teri zulf hai mere haath men  ke tu aaj bhi mere saath hai   2 tere dil men bhi main zaruur huun  tujhe yaad ho ke na yaad ho  main teri nazar ka threedots', 'correct_label': 'madan mohan', 'label': 5, 'split': 'test', 'title': 'main terii nazar kaa suruur huun', 'year': '1964'}`
- output: `{"pred": "naushad", "top3": ["naushad", "madan mohan", "c ramchandra"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='naushad' ref='madan mohan'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='madan mohan' in top3=['naushad', 'madan mohan', 'c ramchandra']

### #150 — FAIL

- item: `{'lyrics': ' rafii resham kii dorii hoy resham kii dorii kahaan jaiiho nindiyaa churaake choriichorii resham kii dorii hoy resham kii dorii hoa o kahaan jaiiho nindiyaa churaake choriichorii lataa ki resham kii dorii haay resham kii dorii kahaan jaauungii main tuu hai chandaa main chakorii piipal kii chhainyaa hoa piipal kii chhainyaa ho o o teriimerii ek jindadii o mere sainyaa piipal kii chhainyaa hoa piipal kii chhainyaa rafii o o o o chhoduun main zamaanaa main naa chhoduun terii bainyaa piipal kii chhainyaa haay piipal kii chhainyaa  lataa imalii ke buute hoa imalii ke buute kal kyuun na aae main na boluun jaao jhuuthe   2 rafii badaa mazaa aae main manaauun aur tuu ruuthe aur tuu ruuthe kothe pe aa rii haay kothe pe aa rii tere naam kar duun jiyaa le aa patavaarii lataa kaisaa patavaarii hoa kaisaa patavaarii e tuu meraa main teriiye to jaane duniyaa saarii kaisaa patavaarii hoa kaisaa patavaarii  lataa parbat pe jharanaa hoa parbat pe jharanaa koii sun legaa chupakechupake baaten karanaa  2 rafii pyaar kiyaa to badanaamii se kyaa daranaa kyaa daranaa lataa kurtaa malamal kaa hoa kurtaa malamal kaa aaj to jaatii huun main lele vaadaa kal kaa kurtaa malamal kaa haay kurtaa malamal kaa rafii o o o o kal kaa bharosaa kyaa bharosaa nahiin pal kaa kurtaa malamal kaa haay kurtaa malamal kaa  rafii ambar pe taare haay ambar pe taare jiine nahiin denge tere nainaa kajaraare  2 lataa jiinaa ho jise vo aae kyuun priitam ke dvaare priitam ke dvaare rafii misarii kii daliyaan haay misarii kii daliyaan pyaar men kaante hain ziyaadaa thodii kaliyaan lataa misarii kii daliyaan hoa misarii kii daliyaan o o o o kaante ho yaa kaliyaan pii kii galiyaan pii kii galiyaana rafii gunagunaanaa lataa gunagunaanaa donon gunagunaanaa', 'correct_label': 'laxmikantpyarelal', 'label': 4, 'split': 'test', 'title': 'resham kii dorii', 'year': '1969'}`
- output: `{"pred": "s d burman", "top3": ["s d burman", "shankarjaikishan", "r d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='s d burman' ref='laxmikantpyarelal'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='laxmikantpyarelal' in top3=['s d burman', 'shankarjaikishan', 'r d burman']

### #151 — FAIL

- item: `{'lyrics': ' milo na tum to ham ghabaraaye milo to aankh churaaye hamen kyaa ho gayaa hai tumhiin ko dil kaa raaz bataayen tumhiin se raaz chhupaayen hamen kyaa ho gayaa hai   threedots  o bhole saathiyaa dekhe jo shokhii tere pyaar kii oy hoy o bhole saathiyaa  dekhe jo shokhii tere pyaar kii aanchal men bhar lii hamane saarii baharen sansaar kii nayii adaa se ham ithalaayen paayii khushii lutaayen hamen kyaa ho gayaa hai   threedots  ruuthe kabhii kabhii maan gaye baaten tumhaarii ham jaan gaye aa aisii adaayen qurabaan gaye tumhen manaaye dil bahalaayen kyaa kyaa naaz uthaayen hamen kyaa ho gayaa hai   threedots  o sohane jogiyaa rang le hamen bhii isii rang men oy hoy o sohane jogiyaa  rang le hamen bhii isii rang men phir se sunaa de bansii kaliyaan khilaa de gore ang men vahii jo taanen aag lagaaye unhiin se aag bujhaaen hamen kyaa ho gayaa hai   threedots ', 'correct_label': 'madan mohan', 'label': 5, 'split': 'test', 'title': 'milo na tum to ham ghabaraaye', 'year': '1970'}`
- output: `{"pred": "s d burman", "top3": ["s d burman", "kalyanjianandji", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='s d burman' ref='madan mohan'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='madan mohan' in top3=['s d burman', 'kalyanjianandji', 'laxmikantpyarelal']

### #152 — PASS

- item: `{'lyrics': ' na som ko na mangal ko na budh ko na jummeraaat ko aanaa aaadhii raat ko aanaa aaadhii raat ko jumme ke jumme ghar aayaa karo us din akele rahate hain ghar aake tum chummaa de jaayaa karo hoe hoe  jumme ke jumme bulaayaa karo us din ham mood men rahate hain ghar bulaake tum chummaa le jaayaa karo hoe hoe  jumme ko aake tum kyaa karoge bolo jii bolo tum kyaa karoge tum ham pe ham pe maranaa ham tum pe tum pe marenge dil dil dil dil ye dhak dhak dhak karataa hai kuchh karane ko dil chaahe karane se dil darataa hai jumme ke din yuun zid naa karo vaadaa karake kabhii to nibhaayaa karo jumme ke jumme threedots  main mummy se boluungaa tuu ban jaa saas hamaarii terii baaten number one hain tuu hii hai meraa raajaa par aaj to sunday hai mujhe maaf kar de baabaa jumme kaa din hai yuun zid naa karo jumme ke jumme threedots ', 'correct_label': 'annu malik', 'label': 1, 'split': 'test', 'title': 'jumme ke jumme ghar aayaa karo  chummaa de jaayaa karo', 'year': '1997'}`
- output: `{"pred": "annu malik", "top3": ["annu malik", "naushad", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='annu malik' ref='annu malik'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='annu malik' in top3=['annu malik', 'naushad', 'laxmikantpyarelal']

### #153 — FAIL

- item: `{'lyrics': ' akhiyaan milaake jiyaa bharamaa ke chale nahin jana ho chale nahin jana  2   2  jao to jane na dungi main rasta rok lungi  2 ho sainya ke painyyaa pad jaungi roke kahungi  2 akhiyan mila ke threedots  ahon ke badale ahen lena ji daga nahiin dena  2 han nain bhare na roe roe dil ye kahe na  2 akhiyan mila ke threedots  jane ka nam na lo raja ji dil baitha jae  2 han dekho ji dekho dukhi dil ki pare na hay  2 akhiyan mila ke threedots', 'correct_label': 'naushad', 'label': 6, 'split': 'test', 'title': 'akhiyaan milaake jiyaa bharamaa ke', 'year': '1944'}`
- output: `{"pred": "madan mohan", "top3": ["madan mohan", "kalyanjianandji", "s d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='madan mohan' ref='naushad'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='naushad' in top3=['madan mohan', 'kalyanjianandji', 's d burman']

### #154 — FAIL

- item: `{'lyrics': ' mujh pe tuufaan uthaaye logon ne 2 muft baithebithaaye logon ne 2 kar diyaa apane aanejaane ke 2 tazakire jaayejaaye logon ne  mujh pe tuufaan uthaaye logon ne muft baithebithaaye logon ne  vasl kii baaten kab ban aaii thiin dil se dafatar banaaye logon ne baat apanii vahaan na jamane diye apane naqsh jamaaye logon ne  mujh pe tuufaan uthaaye logon ne muft baithebithaaye logon ne 2  sun ke udatii sii apanii chaahat kii 2 donon ke hosh udaaye logon ne bin kahe raaz haay bin haan ne 2 use kyuun kar sunaaye logon ne  mujh pe tuufaan uthaaye logon ne  kya tamaashaa hai jo naa dekhe the 2 wo tamaashe dikhaaye logon ne kar diyaa momin us sanam ko kudaa kyaa kiyaa haayhaay logon ne 2  mujh pe tuufaan uthaaye logon ne muft baithebithaaye logon ne mujh pe tuufaan uthaaye logon ne  mujh pe tufaan uthaaye logon ne 2 ', 'correct_label': 'a r rahman', 'label': 0, 'split': 'test', 'title': 'mujh pe tuufaan uthaaye logon ne', 'year': '2003'}`
- output: `{"pred": "naushad", "top3": ["naushad", "s d burman", "c ramchandra"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='naushad' ref='a r rahman'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='a r rahman' in top3=['naushad', 's d burman', 'c ramchandra']

### #155 — FAIL

- item: `{'lyrics': ' pyaar kii nishaaniyaan sunaayen ye kahaaniyaan tuu pyaar kar ye zindagii hai pyaar ke liye pyaar kii nishaaniyaanthreedots  wo dil hii kyaa jise kisii kii aarazuu na ho wo aankh kyaa jise kisii ki justajuu na ho aarazuu na ho justajoo na ho to dil bane wo phuul jisamen  rangobuu na ho pyaar kii kahaaniyaanthreedots  ye pyaar do dilon kii dhadakanon kaa naam hai hai jis men chaahaton kaa rang ye wo jaam hai ye jaam pii bhii le diiwaanagii bhii le is jaam hii men zindagii kii subaha shaam hai pyaar kii kahaaniyaanthreedots  safar kaa kyaa mazaa jo koii hamasafar na ho tujhako kisii kii terii kisii ko khabar na ho kisii ko saath le kisii kaa saath de jiinaa hai kyaa zaruurii muhabbat agar na ho pyaar kii nishaaniyaanthreedots', 'correct_label': 'madan mohan', 'label': 5, 'split': 'test', 'title': 'pyaar kii nishaaniyaan sunaayen ye kahaaniyaan', 'year': '1958'}`
- output: `{"pred": "c ramchandra", "top3": ["c ramchandra", "kalyanjianandji", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='c ramchandra' ref='madan mohan'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='madan mohan' in top3=['c ramchandra', 'kalyanjianandji', 'laxmikantpyarelal']

### #156 — FAIL

- item: `{'lyrics': ' mere mahabuub tujhe merii muhabbat kii qasam phir mujhe naragisii aankhon kaa sahaaraa de de meraa khoyaa huaa rangiin nazaaraa de de mere mahabuub tujhe threedots  bhuul sakatii nahiin aankhen vo suhaanaa manzar jab teraa husn mere ishq se takaraayaa thaa aur phir raah men bikhare the hazaaron nagamen main vo nagamen terii aavaaz ko de aayaa thaa saazedil ko unhiin giiton kaa sahaaraa de de meraa khoyaa threedots  yaad hai mujhako merii umr kii pahalii vo ghadii terii aankhon se koii jaam piyaa thaa maine mere rag rag men koii barq sii laharaaii thii jab tere maramarii haathon ko chhuaa thaa maine aa mujhe phir unhiin haathon kaa sahaaraa de de meraa khoyaa threedots  maine ik baar terii ek jhalak dekhii hai merii hasarat hai ke main phir teraa diidaar karuun tere saae ko samajh kar main hansiin taajamahal chaandanii raat men nazaron se tujhe pyaar karuun apanii mahakii huii zulfon kaa sahaaraa de de meraa khoyaa threedots  dhuundhataa huun tujhe har raah men har mahafil men thak gaye hain merii majabuur tamannaa ke kadam aaj kaa din merii ummiid kaa hai aakhirii din kal na jaane main kahaan aur kahaan tuu ho sanam do ghadii apanii nigaahon kaa sahaaraa de de meraa khoyaa threedots  saamane aa ke zaraa pardaa uthaa de ruk se ik yahii meraa ilaajegametanhaaii hai terii furaqat ne pareshaan kiyaa hai mujhako ab mil jaa ke merii jaan bhii ban aaii hai dil ko bhuulii huii yaadon kaa sahaaraa de de meraa khoyaa threedots ', 'correct_label': 'naushad', 'label': 6, 'split': 'test', 'title': 'mere mahabuub tujhe merii muhabbat kii qasam', 'year': '1963'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "naushad", "madan mohan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='naushad'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='naushad' in top3=['laxmikantpyarelal', 'naushad', 'madan mohan']

### #157 — FAIL

- item: `{'lyrics': ' thukaraake mujhe jaanevaale ik thokar aur lagaataa jaa sinduur to maang se chhiin liyaa ab phuulon ko thukaraataa jaa  o jaanevaale jaanevaale tuune aramaanon kii duniyaa luut lii muskuraane bhii na paaii thii tamannaa luut lii haaye duniyaa luut lii  o jaanevaale threedots  chhiin kar khushiyaan merii rone ko aansuu de diye  2 raat din maangii mere dil ne duaa jisake liye 2 kyaa qayaamat hai kyaa qayaamat hai usii ne dil kii duniyaa luut lii muskuraane bhii na paaii thii tamannaa luut lii haaye duniyaa luut lii  o jaanevaale threedots   kar diyaa beghar mujhe mere hii ghar ke saamane 2 aa gayii jab pyaar kii manzil nazar ke saamane      2 luutanevaale ne luutanevaale ne manzil kii tamannaa luut lii muskuraane bhii na paaii thii tamannaa luut lii haaye duniyaa luut lii  o jaanevaale tuune aramaanon kii duniyaa luut lii muskuraane bhii na paaii thii tamannaa luut lii haaye duniyaa luut lii  o jaanevaale threedots', 'correct_label': 'c ramchandra', 'label': 2, 'split': 'test', 'title': 'thukaraake mujhe jaanevaale  o jaanevaale tuu ne', 'year': '1949'}`
- output: `{"pred": "naushad", "top3": ["naushad", "laxmikantpyarelal", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='naushad' ref='c ramchandra'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='c ramchandra' in top3=['naushad', 'laxmikantpyarelal', 'shankarjaikishan']

### #158 — FAIL

- item: `{'lyrics': ' sun lo sunaataa huun tumako kahaanii ruutho naa hamase o gudiyon kii raanii re mammaa re mammaa re re mammaa re mammaa re  1 ham to gae baazaar men lene ko aaluu aaluu vaaluu kuchh na milaa piichhe padaa bhaaluu re mammaa threedots  2 ham to gae baazaar men lene ko lattuu lattuu vattuu kuchh na milaa piichhe padaa tattuu re mammaa threedots  3 ham to gae baazaar men lene ko rotii rotii votii kuchh na milii piichhe padii motii re mammaa threedots', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'sun lo sunaataa huun tumako kahaanii ruutho naa re mammaa re mammaa re', 'year': '1971'}`
- output: `{"pred": "kalyanjianandji", "top3": ["kalyanjianandji", "annu malik", "s d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='kalyanjianandji' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='shankarjaikishan' in top3=['kalyanjianandji', 'annu malik', 's d burman']

### #159 — PASS

- item: `{'lyrics': ' la dar naa mohabbat kar le 2   ulfat se jholii bhar le   duniyaa hai chaar din kii   jii le chaahe mar le   ho o do dar naa mohabbat kar le 2  la duniyaa faanii tuu bhii faanii   letaa jaa ulfat kii nishaanii sh do lafazon kii ek kahaanii   ek mohabbat ek javaanii   yaad ise tuu kar le 2 do dar naa mohabbat kar le 2 la ulfat se jholii bhar le threedots   ho o do dar naa mohabbat kar le 2  sh duniyaa to kaanton kaa ek van hai   aur ulfat phuulon kaa chaman hai la kar le vahii jo dil kii lagan hai   soch naa manzil dil kii kathin hai   ho dil kii kathin hai   is manzil se guzar le 2   dar naa mohabbat kar le 2 sh ulfat se jholii bhar lethreedots   ho o do dar naa mohabbat kar le 2  la kahanaa jo tumane meraa na maanaa   piichhe padegaa phir pachhataanaa sh dekh le apanaa   kar le thikaanaa   ye hai mohabbat   vo hai zamaanaa 2 do hans le yaa aahen bhar le 2   dar naa mohabbat kar le 2 ', 'correct_label': 'naushad', 'label': 6, 'split': 'test', 'title': 'dar naa mohabbat kar le', 'year': '1949'}`
- output: `{"pred": "naushad", "top3": ["naushad", "c ramchandra", "s d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='naushad' ref='naushad'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='naushad' in top3=['naushad', 'c ramchandra', 's d burman']

### #160 — FAIL

- item: `{'lyrics': ' bindiyaa tarase kajaraa barase aaye naa saajanaa dhal gaii rainaa bujh gaii baatii main khadii aanganaa 2  main pyaasii piyaa aavan kii koyal sii bin saavan kii 2 bhatakuun re saathii binaa bindiyaa threedots  yaad karuun jab suuratiyaa aur jalen bhiigii ankhiyaan 2 kuch mohe suujhe naa bindiyaa threedots  dhuundha thakii sab dvaar galii raat yuun hii phir biit chalii 2 aae piyaa ajahun naa bindiyaa threedots  bindiyaa threedots  main khadii aanganaa 4', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'bindiyaa tarase kajaraa barase aaye naa saajanaa', 'year': '0'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "r d burman", "kalyanjianandji"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='r d burman' in top3=['laxmikantpyarelal', 'r d burman', 'kalyanjianandji']

### #161 — PASS

- item: `{'lyrics': '      shai mere dil se ye nain mile rahane do jaaneman ke do ghadii bahal jaataa hai dil diiwaanaa  aa ke do ghadii bahal jaataa hai dil diiwaanaa  shai inake binaa yahaan vahaan aise phiruun uljhan kaa maaraa pairon tale jaise koii rakhataa chale jalataa angaaraa ho dukh meraa ye jaane yaa jaane meraa haal ye viiraanaa  aa ho mere dil se ye nain threedots  tum bhii mujhe dekho yuun hii hotii rahe dil kii do baaten tum hii se mile mujhe jiivan ke din jiivan kii raaten ho ye raat din ruk jaaen phir bhii na ruk paae ye afasaanaa  ho mere dil se ye nain threedots ', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'mere dil se ye nain mile rahane do jaaneman', 'year': '1974'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "kalyanjianandji", "s d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='r d burman' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='r d burman' in top3=['r d burman', 'kalyanjianandji', 's d burman']

### #162 — FAIL

- item: `{'lyrics': '  mujhako agar ijaazat ho to main ik giit sunaauun mahafil men shaamil ho kar aapakaa dil bahalaauun  aapake qadam uthe yuun merii aavaaz se aa gae kuchh sher yaad husn ke andaaz se mujhako agar ijaazat ho to aage baat badhaauun mahafil men shaamil ho threedots  is maze kii raat men chaandanii kaa naam luun aapasaa koii nahiin main kisakaa naam luun mujhako agar ijaazat ho to naam koii le jaauun mahafil men shaamil ho threedots ', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'mujhako agar ijaazat ho to main ik giit sunaauun', 'year': '1974'}`
- output: `{"pred": "naushad", "top3": ["naushad", "r d burman", "madan mohan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='naushad' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='r d burman' in top3=['naushad', 'r d burman', 'madan mohan']

### #163 — FAIL

- item: `{'lyrics': ' zamiin chal rahii aasamaan chal rahaa hai  ye kisake ishaare jahaan chal rahaa hai  zamiin chal rahii threedots   chalii jaa rahii hai zamaane kii naiyaa  nazar se na dekhaa kisiine khevaiyaa  na jaane ye chakkar kahaan chal rahaa hai  ye kisake ishaare threedots   ye hansanaa ye ronaa ye aashaa niraashaa  samajh men na aaye ye kyaa hai tamaashaa  ye kyon raat din kaaravaan chal rahaa hai  ye kisake ishaare threedots   ajab hai ye mahafil ajab daastaan hai  na manzil hai koii na koii nishaan hai  to phir kis liye kaaravaan chal rahaa hai  ye kisake ishaare threedots   bhatakate to dekhe hazaaron sayaane magar raaz qudarat kaa koii na jaane  ye sab silasilaa benishaan chal rahaa hai  ye kisake ishaare threedots  ', 'correct_label': 'c ramchandra', 'label': 2, 'split': 'test', 'title': 'zamiin chal rahii aasamaan chal rahaa hai', 'year': '1954'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "madan mohan", "s d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='shankarjaikishan' ref='c ramchandra'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='c ramchandra' in top3=['shankarjaikishan', 'madan mohan', 's d burman']

### #164 — PASS

- item: `{'lyrics': ' rafii dekho ruuthaa naa karo  baat nazaron kii suno lataa ham na bolenge kabhii tum sataayaa naa karo   2 rafii dekho ruuthaa naa karo  rafii cheharaa to laal huaa kyaa kyaa haal huaa is adaa par terii main to paagal huaa tum bigadane jo lago  aur bhii hansiin lago lataa ham na bolenge kabhii tum sataayaa naa karo rafii dekho ruuthaa naa karo  lataa jaan par merii banii aapakii thaharii hansii haay main jaan gaii pyaar kii fitanaagarii dil jalaane ke liye thandii aahen na bharo rafii dekho ruuthaa naa karo  baat nazaron kii suno lataa ham na bolenge kabhii  rafii terii khushabuu ne mere hosh bhii chhiin liye hain khushii aaj hame tere pahaluu men gire dil kii dhadakan pe zaraa phuul saa haath rakho lataa ham na bolenge kabhii tum sataayaa naa karo rafii dekho ruuthaa naa karo  lataa kyaa kahegaa ye samaa in raahon kaa dhunaa laaj aae mujhe mujhako laae ho kahaan ham tumhe maan gae  tum bade vo ho hato rafii dekho ruuthaa naa karo  baat nazaron kii suno lataa ham na bolenge kabhii tum sataayaa naa karo rafii dekho ruuthaa naa karo', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'dekho ruuthaa naa karo baat nazaron kii suno', 'year': '0'}`
- output: `{"pred": "s d burman", "top3": ["s d burman", "r d burman", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='s d burman' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='s d burman' in top3=['s d burman', 'r d burman', 'shankarjaikishan']

### #165 — FAIL

- item: `{'lyrics': ' chhod ke naa jaanaa naa naa jaanaan phir mujhe tum chhod ke naa jaanaa phir na meraa dil dukhaanaa phir na tadapaanaa ho chhod ke naa jaanaa  kaisii dhun men kho gaii hai ye to paagal ho gaii hai isako ye kyaa ho gayaa hai jaagate men so gaii hai chhod ke naa jaanaa threedots  das rahaa hai tan ko tanhaaii kaa naag merii nas nas men hai jaane kaisii aag main huun jaise baansurii aur saans tuu guunjataa hai tuu badan men ban ke raag sun rahii hain ye fizaaen apanaa afasaanaa naa naa naa naa naa chhod ke naa jaanaa threedots  tuu jo chhuu le to bahak jaatii huun main garm haathon se dahak jaatii huun main jism lagataa hai mujhe ik phuul saa tere paas aake mahak jaatii huun main hai tere bin kaise mumakin chain paa jaanaa naa naa naa naa naa chhod ke naa jaanaa threedots  aarajuuen dil ko pighalaane lagiin haay kyuun angadaaiiyaan aane lagiin kaanpatii huun tharatharaatii huun main kyuun  kyuun main aakhir tumase sharamaane lagii ye mujhe kyaa ho rahaa hai tum hii samajhaanaa naa naa naa naa naa chhod ke naa jaanaa threedots ', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'chhod ke naa jaanaa', 'year': '1999'}`
- output: `{"pred": "annu malik", "top3": ["annu malik", "a r rahman", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='annu malik' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='r d burman' in top3=['annu malik', 'a r rahman', 'laxmikantpyarelal']

### #166 — FAIL

- item: `{'lyrics': '  he nadiyaa kinaare he raaii aaii kanganaa aise ulajh gae anaadii sajanaa nadiyaa kinaare   threedots  kaahe panaghat uupar gaii thii chalake akelii maare hans hans taanaa saarii sakhiyaan sahelii  gorii aur jaao na maano kahanaa nadiyaa kinaare   threedots  ab khadii khadii sochuun dekhii hai saas nanandiiyaa sab kaa karii hai bahaanaa ab to suunii kalaaii lai ke chorii chorii jaanaa bhaarii padaa re piyaa se milanaa nadiyaa kinaare   threedots  ', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'he nadiyaa kinaare he raaii aaii kanganaa', 'year': '1973'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "s d burman", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='r d burman' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='s d burman' in top3=['r d burman', 's d burman', 'laxmikantpyarelal']

### #167 — PASS

- item: `{'lyrics': ' suuraj ke jaisii golaaii\tgolaaii chandaa ki thandak bhii paaii\tshshshshthreedots haa thanake to pyaare duhaaii laii laii laii laii  terii dhuum har kahiin tujh saa yaar koii nahiin ham ko to pyaare tuu sab se pyaaraa laii laii laii laii terii dhuum threedots   duniyaa kii gaadii kaa pahiyaa tuu chor tuu hii sipahiyaa raajon kaa raajaa rupaiyaa\t2 laii laii laii laii terii dhuum threedots   buudhon kii tuu hii javaanii\tcough cough bachapan kii dilakash kahaanii tere binaa duudh paanii\t\t2 laii laii laii laii terii dhuum threedots   daulat kaa mazahab chalaake\tom dhanaaya namah ham ek mandir banaake\t\thare dhan hare dhan puujenge tujhako bithaake\t2 jay jay jay jay  terii dhuum threedots ', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'terii dhuum har kahiin tujh saa yaar koii nahiin', 'year': '-1'}`
- output: `{"pred": "s d burman", "top3": ["s d burman", "c ramchandra", "kalyanjianandji"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='s d burman' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='s d burman' in top3=['s d burman', 'c ramchandra', 'kalyanjianandji']

### #168 — FAIL

- item: `{'lyrics': '  na jaane dil vich kii aayaa ek prem pyaalaa pii aayaa main jii aayaa main jii aayaa main prem pyaalaa pii aayaa oy ramataa jogii hoy hoy   threedots  main prem daa pyaalaa pii aayaa ek pal men sadiyaan jii aayaa oy ramataa jogii hoy hoy  main prem daa pyaalaa pii aayaa ek pal men sadiyaan jii aayaa saarii madhushaalaa pii aayaa main pii aayaa main pii aayaa main pii aayaa jaa pii aayaa main jii aayaa oy ramataa jogii hoy hoy tuu ramataa jogii hoy hoy   threedots  tuu prem daa pyaalaa pii aayaa ai tere dil vich kii aayaa saarii madhushaalaa pii aayaa ek pa men sadiyaan jii aayaa main pii aayaa main pii aayaa main pii aayaa jaa pii aayaa main jii aayaa tuu ramataa jogii hoy hoy oy ramataa jogii hoy hoy   threedots  ye jog liyaa kis kaaran ye rog liyaa kis kaaran ho ik jogan dekhii bastii men ek mauj uthii to mastii men dil bhii aayaa main pii aayaa main prem pyaalaa pii aayaa main pii aayaa main pii aayaa main prem pyaalaa pii aayaa main jii aayaa tuu ramataa jogii tuu ramataa jogii jogii jogii jogii ho man men lagan ye jaagii jag chhuutaa hoy hoy jag chhuutaa jiyaa main raagii ye baat vahaan tak na pahunchii ye chot jiyaa tak na laagii ho ye dard zubaan tak na aayaa ye tere dil vich kii aayaa  saarii madhushaalaa pii aayaa ek pal men sadiyaan jii aayaa main pii aayaa main pii aayaa main pii aayaa jaa pii aayaa main pii aayaa oy ramataa jogii hoy hoy   threedots ', 'correct_label': 'a r rahman', 'label': 0, 'split': 'test', 'title': 'na jaane dil vich kii aayaa  ramataa jogii', 'year': '1999'}`
- output: `{"pred": "s d burman", "top3": ["s d burman", "c ramchandra", "annu malik"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='s d burman' ref='a r rahman'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='a r rahman' in top3=['s d burman', 'c ramchandra', 'annu malik']

### #169 — FAIL

- item: `{'lyrics': '  mu \tkahiin saavan men bhii ye dil na tarase la \tghataa chhaaii to hai barase na barase  \tbhiigiibhiigii havaa hai kaaliikaalii ghataa hai \tghataa pe to shaq ho sakataa hai tum pe nahiin ho mu \tbhiigiibhiigii havaa hai threedots  la \tdil diivaane diivaaron ko tod ke mil jaate hain \tjab phuulon ko khilanaa ho to patajhad men khil jaate hain \taise aksar huaa hai aisaa ho ye duaa hai \tduaa pe to shaq ho sakataa hai tum pe nahiin ho  mu \tis duniyaa se dar ke kisane yaar kaa daaman chhod diyaa \tvo harajaaii kahalaayaa hai jisane vaadaa tod diyaa \taashiq se sunaa hai chaahat men vafaa hai \tvafaa pe to shaq ho sakataa hai tum pe nahiin ho  la \tvaqt pe din dhalataa hai vaqt pe chaand nikalataa hai mu \tkoii to hai is parade men kaun ishaaraa karataa hai la \tkoii jaaduu hai kyaa mu \tkahate hain kudaa hai do \tkudaa pe to shaq ho sakataa hai tum pe nahiin ho la \ttum pe nahiin mu \ttum pe nahiin ', 'correct_label': 'naushad', 'label': 6, 'split': 'test', 'title': 'kahiin saavan men bhii  bhiigiibhiigii havaa hai', 'year': '1975'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "kalyanjianandji", "annu malik"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='naushad'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='naushad' in top3=['laxmikantpyarelal', 'kalyanjianandji', 'annu malik']

### #170 — PASS

- item: `{'lyrics': '  ra \ttum laakh chhupaanaa chaahoge par pyaar chhupaa naa paaoge \tkachche dhaage se bandhe sarakaar chale aaoge 2 la \ttum laakh jataanaa chaahoge par pyaar jataa naa paaoge \tdil ko thaame haathon se kaamosh chale aaoge  ra \ttumhaare chehare kii rangat to ye bataatii hai \tkisii kii yaad tumhen har ghadii sataatii hai \tyah ulajheulajhe baal muhabbat kaa raaz kahate hain \tkamal se nain kyaalon men duube rahate hain \ttumhaarii chaal men shokii hai aur sharaarat hai \tzaruur tumako kisii na kisii se ulfat hai \tlo raaz khul gayaa ab kis lie chhupaate ho \tzamaanaa jaan gayaa hamako kyon banaate ho \ttum laakh chhupaanaa threedots  la \ttumhaare honthon pe har baat kaanp jaaegii \tlagii ye dil kii zubaan par kabhii na aaegii \tbataao kaise jataaoge pyaar phir apanaa \tna hogaa puuraa kabhii aarazuu kaa ye sapanaa \ttumhen yah pyaar kii hasarat bahut sataaegii \tkabhii rulaaegii tumako kabhii hansaaegii \thamaare kuuche men aashiq hazaar aate hain \tmagar jo aate hain vo hosh bhuul jaate hain \ttum laakh chhupaanaa threedots  ra \thamaare hizr men tumako na niind aaegii \takelaa paa ke judaaii tumhen sataaegii \tham apanii aah se patthar ko mom karate hain \tham apane pyaar se gulashan men rang bharate hain \thamaaraa jazbaaemohabbat ye rang laaegaa \ttumhaare dar se tumhen badh ke khiinch laaegaa \tgulon kii qaid men kushbuu to ruk nahiin sakatii \tisii tarah qaid muhabbat chhup nahiin sakatii \ttum laakh chhupaanaa threedots ', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'tum laakh chhupaanaa chaahoge par pyaar chhupaa naa paaoge', 'year': '1960'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "kalyanjianandji", "madan mohan"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='shankarjaikishan' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='shankarjaikishan' in top3=['shankarjaikishan', 'kalyanjianandji', 'madan mohan']

### #171 — FAIL

- item: `{'lyrics': '  jaago sone vaalon suno merii kahaanii 2 kyaa amiirii kyaa gariibii bhuulo baaten puraanii jaago sone vaalon threedots  tuutaa jo aaj dil kaa vo saaz rone lagaa ek badanasiib hansane lage duniyaa ke log koii huaa barbaad jaago sone vaalon threedots  ye uunch niich duniyaa ke biich aakir ye kyon bolo koii jo hai bhalaa vo kyon buraa ham to na samajhe ye raaz jaago sone vaalon threedots  aapas men gam baanten jo ham phir na rahen aise sitam kahane ko insaan hain vo insaaniyat kahaan hai jaago sone vaalon threedots ', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'jaago sone vaalon suno merii kahaanii', 'year': '1965'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "kalyanjianandji", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='r d burman' in top3=['laxmikantpyarelal', 'kalyanjianandji', 'shankarjaikishan']

### #172 — PASS

- item: `{'lyrics': '  is duniyaa men ai dilavaalon dil kaa lagaanaa khel nahiin ulfat karanaa khel hai lekin kar ke nibhaanaa khel nahiin  jabase hue hain duur vo hamase  dhuundh rahii hai unako nazar  2  haay re o bedard zamaane  2 ye bhii nahiin hai unako kabar aag lagii hai dil men kuchh aisii jisakaa bujhaanaa khel nahiin is duniyaa men threedots  laakha sataaen pyaar ke dushman  bhuul sakenge unako na ham  2  aur badhegii unakii mohabbat  2 jitane bhii honge zulmositam kahade koii naadaanon se hamako mitaanaa khel nahiin is duniyaa men threedots ', 'correct_label': 'naushad', 'label': 6, 'split': 'test', 'title': 'is duniyaa men ai dilavaalon dil kaa lagaanaa khel nahiin', 'year': '1949'}`
- output: `{"pred": "naushad", "top3": ["naushad", "madan mohan", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='naushad' ref='naushad'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='naushad' in top3=['naushad', 'madan mohan', 'shankarjaikishan']

### #173 — FAIL

- item: `{'lyrics': ' duub gae aakaash ke taare jaake na tum aae takate takate nainaa haare jaake na tum aae  duub gaii baagon se bahaaren phail gae patajhad ke saae lekin tumako apane vaade bhuule se bhii yaad na aae duub gae threedots  bahate bahate chaand kii kashtii duur gagan men khone lagii aas kii ek nanhii sii kiran thii voh bhii ojhal hone lagii duur gae threedots ', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'duub gae aakaash ke taare', 'year': '1954'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "laxmikantpyarelal", "annu malik"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='shankarjaikishan' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='s d burman' in top3=['shankarjaikishan', 'laxmikantpyarelal', 'annu malik']

### #174 — FAIL

- item: `{'lyrics': '   morii atariyaa pe kaagaa bole moraa jiyaa dole koii aa rahaa hai  2   more man men uthii hai umang re o moraa phadake hai baanyaa ang re  2 more man kii muraliyaa pe haulehaule sur kholekhole koii gaa rahaa hai  morii atariyaa pe kaagaa bole moraa jiyaa dole koii aa rahaa hai  aaj bagiyaa men aaii bahaar re o mere jiiwan men solah singaar re ho mere jiiwan men solah singaar re more kaan men gungun bolebole ras gholeghole koii gaa rahaa hai  morii atariyaa pe kaagaa bole moraa jiyaa dole koii aa rahaa hai   more maathe pe kumakum kii bindiyaa aaj luungii na pal bhar main nindiyaa  2 ghar men thandii hawaa mast dole ghuunghat pat khole jiyaa laharaa rahaa hai  morii atariyaa pe kaagaa bole moraa jiyaa dole koii aa rahaa hai ', 'correct_label': 'madan mohan', 'label': 5, 'split': 'test', 'title': 'morii atariyaa pe kaagaa bole moraa jiyaa dole koii aa rahaa hai', 'year': '1950'}`
- output: `{"pred": "naushad", "top3": ["naushad", "c ramchandra", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='naushad' ref='madan mohan'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='madan mohan' in top3=['naushad', 'c ramchandra', 'shankarjaikishan']

### #175 — PASS

- item: `{'lyrics': ' sapane men dekhaa sapanaa  ho sapane men dekhaa sapanaa  aage  ek din sapane men dekhaa sapanaa  kyaa vo jo hai na amitaabh apana  bachchan haan threedots main amitaabh ho gayaa  ho sapane men dekhaa sapanaa   daayen men hemaa  maalinii baayen men ziinat  amaan saamane rekhaa piichhe jo dekhaa  kya hua ratnaa khadii thi haath men chhadii thi  dekhate dekhate main bhaag rahaa tha  dekhaa main bhaag rahaa tha  ho sapane men dekhaa sapane   haan ek aur yaad aya  ek din sapane men dekhaa sapanaa  kyaa vo jo hai na mistar pele apana  kaisaa khilaadii hai badaa anaadii hai  mere saath maich ho gayaa gayaa gayaa threedots are maaraa jo chhakkaa kaich ho gayaa  futabaul men criket kahaana sapane men dekhaa dekhaa sapanaa threedots  ek din chhotii si dekhii sapanii  sapanii are vo jo hai na lataa apanii  lataa gaa rahi thi main tabale pe tha  vo mukhade pe thi main antare pe thaa  taal kahaan taam kahaan tum kahaan ham kahaan  taal kahaan taam kahaan tum kahaan ham kahaan  lataafat fataafat fataafat karaamaat   taake tiikaa taake tikaa  taake tiikaa taake tikaa  thayya thai   sapane men dekhaa sapanaa  ho sapane men dekhaa sapana threedots', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'sapane men dekhaa sapanaa', 'year': '-1'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "kalyanjianandji", "madan mohan"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='r d burman' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='r d burman' in top3=['r d burman', 'kalyanjianandji', 'madan mohan']

### #176 — FAIL

- item: `{'lyrics': ' ye ishq hai ye junuun hai ye dard hai ye sukuun hai ye prem hai prem hai prem hai tum bachoge kis tarah kyaa ye aasaan kaam hai dil ke sau tukade hain har tukade pe teraa naam hai tuu hii merii subah tuu hii merii shaam hai tuu hii merii duniyaa tuu hii merii jaan hai ye ishq hai ye junuun hai threedots  muhabbat karane vaale ek hii dil men rahate hain main unake dil men rahatii huun vo mere dil men rahate hain le ke angadaaiiyaan shabaab kii tarah khilane lagii main gulaab kii tarah mausam nashiilaa sharaab kii tarah  le ke tujhe baahon men ghuumataa phiruun baalon ko gaalon ko chuumataa phiruun tuu hii bekaraarii merii tuu hii karaar hai meraa jiinaa maranaa ab se tere hii naam hai tum bachoge kis tarah threedots ', 'correct_label': 'annu malik', 'label': 1, 'split': 'test', 'title': 'ye ishq hai ye junuun hai  ye prem hai  tum bachoge kis tarah', 'year': '1997'}`
- output: `{"pred": "a r rahman", "top3": ["a r rahman", "annu malik", "s d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='a r rahman' ref='annu malik'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='annu malik' in top3=['a r rahman', 'annu malik', 's d burman']

### #177 — PASS

- item: `{'lyrics': ' ra rimjhim ke giit saavan gaae haay    bhiigiibhiigii raaton men la honthon pe baat dilakii aae haay    bhiigiibhiigii raaton men  la teraa meraa puuchhe naataa    badii vo ye ghataa ghanghor hai    chup huun aise men kah do kaise    meraa saajan nahiin tuu koii aur hai    ke teraa naam honthon pe mere terethreedots    sapane merii aankhon men  ra rimjhim ke giit saavan gaae haay    bhiigiibhiigii raaton men  ra meraa dil bhii hai diivaanaa    tere nainaa bhii hain naadaan se    kuchh na sochaa kuchh na dekhaa    kuchh bhii puuchhaa na is anjaan se    chal pade saath ham aise kaise    banake saathii raahon men   ra rimjhim ke giit saavan gaae haay    bhiigiibhiigii raaton men     badii lambii jii kii baaten    badii chhotii barakhaa kii raat jii la kahanaa kyaa hai sunanaa kyaa hai    kahane sunane kii ab kyaa baat hai rala bin kahe bin sune dil ne dilase    kar liin baaten baaton men  ra rimjhim ke giit saavan gaae haay    bhiigiibhiigii raaton men la honthon pe  baat dilakii aae haay    bhiigii bhiigii raaton menthreedots', 'correct_label': 'laxmikantpyarelal', 'label': 4, 'split': 'test', 'title': 'rimjhim ke giit saavan gaae haay', 'year': '1969'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "kalyanjianandji", "madan mohan"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='laxmikantpyarelal' ref='laxmikantpyarelal'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='laxmikantpyarelal' in top3=['laxmikantpyarelal', 'kalyanjianandji', 'madan mohan']

### #178 — PASS

- item: `{'lyrics': ' gii  saajan kii ho gaii gorii     saajan kii ho gaii ma   haay haay re gii  ab ghar kaa aangan vides laage re saajan ma gii  haay haay saajan kii ho gaii gorii saajan kii ho gaii  gii  suunii sii laagen maayake kii galiyaan ma   suunii sii laagen gii  bhaayen na na na bhaayen na ab jii ko bachapan kii sakhiyaan ma   bhaayen na gii  nainon men jhuume bairii kii nadiyaan man ko lubhaayen sajiyaa ki kaliyaan       har svaas pii kaa har svaas pii kaa sandes laage re       ab ghar kaa aangan vides laage re saajan ma gii  haay haay saajan kii ho gaii gorii saajan kii ho gaii  gii  kuchh jaagii jaagii kuchh soii soii ma   kuchh jaagii jaagii gii  baithii hai raadhe ma   o dekho o dekho baithii hai raadhe sapanon men khoii dekho baithii hai raadhe gii  chhedaa to samajho roii ke roii       aise men isako toke na koii       naajukataa pan naajukataa pan pe na thes laage re       ab ghar kaa aangan vides laage re saajan ma gii  haay haay saajan kii ho gaii gorii saajan kii ho gaii  gii  badhatii hai pal pal agnii lagan kii ma   badhatii hai pal pal gii  chatake hai nas nas komal badan kii ma   chatake hai nas nas gii  ham jaanate hain sab isake man kii       ab ho chukii ye apane sajan kii       naihar kaa jiivan       naihar kaa jiivan kales laage re ma   ab ghar kaa aangan vides laage re saajan ma gii  haay haay saajan kii ho gaii gorii saajan kii ho gaii agniikriiraa', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'saajan kii ho gaii gorii', 'year': '1955'}`
- output: `{"pred": "s d burman", "top3": ["s d burman", "r d burman", "c ramchandra"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='s d burman' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='s d burman' in top3=['s d burman', 'r d burman', 'c ramchandra']

### #179 — FAIL

- item: `{'lyrics': ' laalii laalii doliyaa men laalii re dulhaniyaa piyaa kii piyaarii bholii bhaalii re dulhaniyaa  laalii laalii doliyaa men laalii re dulhaniyaa miithe bain tiikhe nainon vaalii re dulhaniyaa  lautegii jo godii bhar hamen naa bhulaanaa ladduu pedhe laanaa apane haathon se khilaanaa terii sab raaten hon diivaalii re dulhaniyaa  duulhe raajaa rakhanaa jatan se dulhan ko kabhii na dukhaanaa tuu goriyaa ke man ko naazuk hai naazon kii hai paalii re dulhaniyaa ', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'laalii laalii doliyaa men', 'year': '1966'}`
- output: `{"pred": "a r rahman", "top3": ["a r rahman", "r d burman", "naushad"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='a r rahman' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='shankarjaikishan' in top3=['a r rahman', 'r d burman', 'naushad']

### #180 — FAIL

- item: `{'lyrics': ' sajanaa lagan terii sone na de ronaa bhii chaahuun to rone na de   samajhe to samajhe ye dil haar ke dard anokhe bade hote hain pyaar ke haae bairii pyaar ke sajanaa lagan terii sone na de   apane paraae merii samajhen na batiyaan kis sang bol ke bitaauun kaalii ratiyaan kaalii kaalii ratiyaan sajanaa lagan terii sone na de   kitnii kathin hain pyaar kii rasmen apanii hii nindiyaa wo bhii na bas men haaye mere bas men sajanaa lagan terii sone na de', 'correct_label': 'madan mohan', 'label': 5, 'split': 'test', 'title': 'sajanaa lagan terii sone na de', 'year': '1959'}`
- output: `{"pred": "naushad", "top3": ["naushad", "madan mohan", "c ramchandra"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='naushad' ref='madan mohan'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='madan mohan' in top3=['naushad', 'madan mohan', 'c ramchandra']

### #181 — FAIL

- item: `{'lyrics': ' jhuum chamelii jhuum chamelii jhaanjhar vaalii jhuum jhuum ghuum chamelii ghuum chamelii jhaanjhar vaalii ghuum jhuum o re kaanchii kaanch kii gudiyaa honthon men baandhe prem kii pudiyaa naa use khole naa munh se bole palakon pe rakh ke aankhon se taule suniyo suniyo o re kaanchii threedots  suniyo suniyaa mishrii se miithii aankhon men band hai baat rasiilii haan naa use khole threedots  pahaadii paar chalanaa hai to parabat hataa duun ghataaon men kahiin chhupanaa hai to saavan bulaa duun mahuaa mahuaa mahakaa mahakaa mahakaa mahakaa mahuaa mahuaa  pahaadii paar threedots koii udataa huaa panchhii bataa degaa thikaanaa jahaan se din nikalataa hai usii tiile pe aa jaanaa mahuaa mahuaa threedots o re kaanchii threedots  teraa koii parichay ho to ai sundarii bataa de badii miithii muskaan hai mundarii banaa de mahuaa mahuaa threedots teraa koii threedots hai paradesii mujhe bhuul jaaegaa kahiin pe de vachan main pahan luun use gahanaa samajh ke mahuaa mahuaa threedots o re kaanchii threedots ', 'correct_label': 'annu malik', 'label': 1, 'split': 'test', 'title': 'o re kaanchii kaanch kii gudiyaa  jhuum chamelii', 'year': '2002'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "annu malik", "r d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='annu malik'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='annu malik' in top3=['laxmikantpyarelal', 'annu malik', 'r d burman']

### #182 — FAIL

- item: `{'lyrics': '   he tuu naa milii to  2 ham jogii ban jaaenge saarii umariyaa ke rogii ban jaaenge tuu naa milii to threedots  o mere sapanon kii raanii tujhape nichhaavar merii javaanii aa terii tasviir banaa duun chiir ke apanaa siinaa dikhaa duun raam base hanumaan ke dil men tuu mere dil kii mahafil men tujhako agar ho koii shankaa jalaa den apane dil kii lankaa tere saamane hansate hue jal jaaenge tuu naa milii to threedots  aur suno tere milan men sukh hain saare tere darshan sabase pyaare tuu mahake jaise raat kii raanii angang se chhalake javaanii tuune bahut mere dil ko sataayaa daal de ab zulfon kaa saayaa kamal kalii sii terii kaayaa ruup menakaa jaisaa paayaa tujhe dekh ke jogii bhii bhogii ban jaaenge tuu naa milii to threedots ', 'correct_label': 'kalyanjianandji', 'label': 3, 'split': 'test', 'title': 'he tuu naa milii to ham jogii ban jaaenge', 'year': '1972'}`
- output: `{"pred": "s d burman", "top3": ["s d burman", "c ramchandra", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='s d burman' ref='kalyanjianandji'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='kalyanjianandji' in top3=['s d burman', 'c ramchandra', 'laxmikantpyarelal']

### #183 — PASS

- item: `{'lyrics': ' naa piilaa naa niilaa naa kaalaa naa goraa abhii hai dupattaa meraa koraa koraa  huun meraa man dole meraa tan dole meraa tan dole meraa man dole agar kare dil teraa o agar kare dil teraa aa rang de dupattaa meraa  is ke aashiq dekho log hazaar hain is pe jiine marane ko taiyaar hain aur koii le jaae baad men tuu pachhataae abhii to saare bebas hain laachaar hain agar kare dil teraa threedots  gore tan pe pandrah solah saal se maine is ko rakhaa hai sambhaal ke tuu chaahe mujh ko paanaa to ghar mere aa jaanaa le jaanaa mujh pe laal chunariyaa daal ke agar kare dil teraa threedots  meraa man dole meraa tan dole', 'correct_label': 'annu malik', 'label': 1, 'split': 'test', 'title': 'meraa man dole meraa tan dole  dupattaa', 'year': '2001'}`
- output: `{"pred": "annu malik", "top3": ["annu malik", "laxmikantpyarelal", "s d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='annu malik' ref='annu malik'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='annu malik' in top3=['annu malik', 'laxmikantpyarelal', 's d burman']

### #184 — FAIL

- item: `{'lyrics': ' raaten gaiin baaten gaiin jo bhii huaa bhuul jaa ab tuu nae parivesh men duniyaa naii phir basaa suuraj nayaa nikale agar aasaan ho usakaa safar kaate terii vaaris jise vo fasalen bo sakataa hai aur tujhase kuchh ho naa ho ye tujhase ho sakataa hai hambaa lilaa hambaa lilo hambaa lile chukumaa tukumaa tukumaa chukumaa chukumaa chile aaj ham hain kal ham nahiin kal kuchh bhii kho sakataa hai pyaar de pyaar le ye ek daulat hai tuu sabako de sakataa hai aur tujhase kuchh ho threedots  sach kah rahaa hai ai bekhabar kar le meraa aitabaar ye zindagii nemat kudaa kii milatii hai bas ek baar yuun hii ise khonaa nahiin phir baad men ronaa nahiin saansen terii hain ik ladii inako piro sakataa hai aur tujhase kuchh ho threedots  bangalonn men hai mahalon men hai par niind aatii nahiin daulat kaa ik saagar milaa par pyaas jaatii nahiin bhuukhaa hai jo badanaam hai santosh men aaraam hai gar chain ho dil men tere dharatii pe so sakataa hai aur tujhase kuchh ho threedots  ye aadamii us aadamii jaisaa nahiin hai to kyaa are kuchh karane kii taaqat to hai paisaa nahiin hai to kyaa jisane kahaa sach hii kahaa ye vaqt naa ik saa rahaa kismat kahe mehanat se tuu har daag dho sakataa hai aur tujhase kuchh ho threedots ', 'correct_label': 'annu malik', 'label': 1, 'split': 'test', 'title': 'raaten gaiin baaten gaiin  aur tujhase kuchh ho naa ho', 'year': '2000'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "r d burman", "a r rahman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='annu malik'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='annu malik' in top3=['laxmikantpyarelal', 'r d burman', 'a r rahman']

### #185 — PASS

- item: `{'lyrics': ' raat kii hathelii par chaand jagamagaataa hai usakii narm kiranon men tumako dekhataa huun to dil dhadak saa jaataa hai raat kii hathelii par threedots  tum kahaan se aaii ho kis nagar ko jaaogii sochataa huun main hairaan chaand jaisaa ye cheharaa raat jaisii ye zulfen hain jagaae sau aramaan ik nashaa saa aankhon men dhiire dhiire chhaataa hai raat kii hathelii par threedots  merii is tanhaaii men mere is viiraane men rang le ke tum aaiin phir bhii sochataa huun main kyaa yahaan tum sachamuch ho yaa ho sirf parachhaaiin khvaab jaise banataa hai aur tuut jaataa hai raat kii hathelii par threedots ', 'correct_label': 'annu malik', 'label': 1, 'split': 'test', 'title': 'raat kii hathelii par chaand jagamagaataa hai', 'year': '2000'}`
- output: `{"pred": "annu malik", "top3": ["annu malik", "shankarjaikishan", "s d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='annu malik' ref='annu malik'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='annu malik' in top3=['annu malik', 'shankarjaikishan', 's d burman']

### #186 — FAIL

- item: `{'lyrics': ' jaane vo kaise log the jinake pyaar ko pyaar milaa hamane to jab kaliyaan maangii kaanton kaa haar milaa jaane vo threedots  khushiyon kii manzil dhuundhii to gam kii gard milii chaahat ke nagame chaahe to aanhen sard milii dil ke bojh ko dhundhalaa kar gayaa jo gamakhaar milaa  hamane to jab threedots  bichhad gayaathreedots bichhad gayaa har saathii dekar  pal do pal kaa saath kisako furasat hai jo thaame diivaanon kaa haath hamako apanaa saayaa tak aqasar bezaar milaa hamane to jab threedots  isako hii jiinaa kahate hain to  yuunhii jii lenge uf na karenge lab sii lenge aansuu pii lenge gam se ab ghabaraanaa kaisaa gam sau baar milaa hamane to jab threedots', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'jaane vo kaise log the jinake pyaar ko pyaar milaa', 'year': '-1'}`
- output: `{"pred": "madan mohan", "top3": ["madan mohan", "kalyanjianandji", "s d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='madan mohan' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='s d burman' in top3=['madan mohan', 'kalyanjianandji', 's d burman']

### #187 — FAIL

- item: `{'lyrics': ' dhim taa daa re daa nii dhim taa daa re daa nii dhim taa naa de re naa o daa nii o daa nii dir dir daanii taa naa dir naa  dhin taa daa re daa nii dhim taa daa re daa nii dhim  taa daa re daa nii dhim taa naa de re naa o daa nii o daa nii dir dir daanii taa naa dir naa  dir dirannaa dir dirannaa o daa nii o daa nii dir daa  ma re re saa saa re ni ni saa saa re dha ni pa ma ma re re saa re ni saa re ma ga re saa re ni saa re saa saa ', 'correct_label': 'a r rahman', 'label': 0, 'split': 'test', 'title': 'dhim taa daa re daa nii', 'year': '1999'}`
- output: `{"pred": "annu malik", "top3": ["annu malik", "a r rahman", "s d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='annu malik' ref='a r rahman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='a r rahman' in top3=['annu malik', 'a r rahman', 's d burman']

### #188 — FAIL

- item: `{'lyrics': ' meraa kuchh saamaan tumhaare paas padaa hai  2 o o o  saavan ke kuchh bhiige bhiige din rakhe hain aur mere ek khat men lipatii raat padii hai vo raat bhulaa do meraa vo saamaan lautaa do  2 meraa kuchh saamaan tumhaare paas padaa hai  2  patajhad hai kuchh threedots hai naa  o  patajhad men kuchh patton ke girane kii aahat kaanon men ek baar pahan ke laut aai thii patajhad kii vo shaakh abhii tak kaanp rahii hai vo shaakh giraa do meraa vo saamaan lautaa do  2  ek akelii chhatarii men jab aadhe aadhe bhiig rahe the  2 aadhe suukhe aadhe giile sukhaa to main le aayii thii giilaa man shaayad bistar ke paas padaa ho   vo bhijavaa do meraa vo saamaan lautaa do  ek sau solaa chaand ki raaten ek tumhaare kaandhe kaa til  2 giilii menhadii ki khushabuu jhuthmuuth ke shikave kuchh jhuuthmuuth ke vaade sab yaad karaa duun sab bhijavaa do meraa vo saamaan lautaa do  2  ek ijaazat de do bas jab isako dafanaauungii main bhii vahiin so jaauungii main bhii vahiin so jaauungii', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'meraa kuchh saamaan tumhaare paas padaa hai', 'year': '1988'}`
- output: `{"pred": "madan mohan", "top3": ["madan mohan", "r d burman", "s d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='madan mohan' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='r d burman' in top3=['madan mohan', 'r d burman', 's d burman']

### #189 — FAIL

- item: `{'lyrics': '  aa \t tiitar ke do aage tiitar \ttiitar ke do piichhe tiitar \taage tiitar \tpiichhe tiitar \tbolo kitane tiitar  2  si \tbolo \tbataao  aa \ttiitar ke do aage tiitar \ttiitar ke do piichhe tiitar \taage tiitar \tpiichhe tiitar \tbolo kitane tiitar  ko \tdo si \tuun hun ko \tpaanch si \tain hun ko \tsaat si \tan hun ko \tta ta ta ta ta ta tiin si \tshaabaash \tlaugh  si \tchaar kachare kachhe chaachaa \tchaar kachare pakke \tpakke kachare kachhe chaachaa \tkachche kachare pakke aa \tchaar kachare kachhe chaachaa \tchaar kachare pakke \tpakke kachare kachhe chaachaa \tkachche kachare pakke  si \tbolo  ko \tchaar kachare kachhe chaachaa \tchaar kachare pakke \tpakke kachare kachhe chaachaa \tkachche kachare pakke  aa \tpakke kachare kachhe chaachaa \tkachche kachare pakke  \ttiitar ke do aage tiitar \ttiitar ke do piichhe tiitar \taage tiitar \tpiichhe tiitar \tbolo kitane tiitar  ko \ttiitar ke do aage tiitar \ttiitar ke do piichhe tiitar \taage tiitar \tpiichhe tiitar \tbolo kitane tiitar  si \tpiith uunchii uunth kii \tuunchaaii se nahiin hotii \thotii hii hai hotii hii hai \tpiith uunchii uunth kii aa \tpiith uunchii uunth kii \tuunchaaii se nahiin hotii \thotii hii hai hotii hii hai \tpiith uunchii uunth kii si \thain naa \traajuu tum bhii gaao  mu ko \tpiith uunchii uunth kii \tuunchaaii se nahiin hotii \thotii hii hai hotii hii hai \tpiith uunchii uunth kii  aa \thotii hii hai hotii hii hai \tpiith uunchii uunth kii  aa \ttiitar ke do aage tiitar \ttiitar ke do piichhe tiitar \taage tiitar \tpiichhe tiitar \tbolo kitane tiitar  ko \ttiitar ke do aage tiitar \ttiitar ke do piichhe tiitar \taage tiitar \tpiichhe tiitar \tbolo kitane tiitar  aa \taa ', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'tiitar ke do aage tiitar', 'year': '1970'}`
- output: `{"pred": "a r rahman", "top3": ["a r rahman", "s d burman", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='a r rahman' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='shankarjaikishan' in top3=['a r rahman', 's d burman', 'laxmikantpyarelal']

### #190 — PASS

- item: `{'lyrics': ' ki jo main hotaa ek tuutaa huaa taaraa     terii raaton kaa raaton kaa to kyaa hotaa aa jo main hotii ek koii bhatakii kiran     us taare kii us taare kii to kyaa hotaa  donon banate sang sangaa mitate sangsang     jiite sang sangaa marate sangsang  aa jo main hotii udiiudii niinden     terii aankhon kii aankhon kii to kyaa hotaa ki jo main hotaa miithaamiithaa sapanaa     un niindon kaa niindon kaa to kyaa hotaa  donon banate sangthreedots  ki jo main hotaa qismat kaa likhaa     tere haathon kaa haathon kaa to kyaa hotaa aa jo main hotii chhupaachhuptaa matalab     tere baaton kaa tere baaton kaa re to kyaa hotaa  donon banate sangthreedots ', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'jo main hotaa ek tuutaa huaa taaraa', 'year': '1973'}`
- output: `{"pred": "s d burman", "top3": ["s d burman", "laxmikantpyarelal", "r d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='s d burman' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='s d burman' in top3=['s d burman', 'laxmikantpyarelal', 'r d burman']

### #191 — PASS

- item: `{'lyrics': ' ai mere mushkilakushaa fariyaad hai fariyaad hai aapake hote hue duniyaa merii barabaad hai  bekas pe karam kiijiye sarkaaremadiinaa bekas pe karam kiijiye gardish men hai taqadiir bhanvar men hai safiina\t2 bekas pe karam kiijiye sarkaaremadiinaa bekas pe karam kiijiye  hai vaqtemadad aaii bigadii ko banaane goshiidaa nahiin aapase kuchh dil ke fasaane zakmon se bharaa hai kisii majabuur kaa siinaa bekas pe karam kiijiye threedots  chhaaii hai musiibat kii ghataa gesuon vaale gesuon vaale lillaah merii duubatii kashtii ko bachaale tuufaan ke aasaar hain dushvaar hai jiinaa bekas pe karam kiijiye threedots  gardish men hai taqadiir bhanvar men hai safiina bekas pe karam kiijiye sarkaaremadiinaa bekas pe karam kiijiye ', 'correct_label': 'naushad', 'label': 6, 'split': 'test', 'title': 'bekas pe karam kiijiye sarkaaremadiinaa', 'year': '-1'}`
- output: `{"pred": "naushad", "top3": ["naushad", "laxmikantpyarelal", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='naushad' ref='naushad'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='naushad' in top3=['naushad', 'laxmikantpyarelal', 'shankarjaikishan']

### #192 — FAIL

- item: `{'lyrics': '  badaa kushanasiib hai jise tuu nasiib hai use aur chaahie kyaa jisake tuu qariib hai badaa kushanasiib threedots  sadaqe jaaen terii nazar ke tiir chalaaen jii bharbhar ke jii uthen ham tujhape mar ke haaledil naa puuchhie haaledil ajiib hai use aur chaahie threedots  ham to kahaan the tere qaabil teraa qaram hai tuune diyaa dil kud hii chal ke aa gaii manzil vah to baadashaah hai bhale hii gariib hai use aur chaahie threedots ', 'correct_label': 'kalyanjianandji', 'label': 3, 'split': 'test', 'title': 'badaa kushanasiib hai jise tuu nasiib hai', 'year': '1961'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "naushad", "kalyanjianandji"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='kalyanjianandji'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='kalyanjianandji' in top3=['laxmikantpyarelal', 'naushad', 'kalyanjianandji']

### #193 — FAIL

- item: `{'lyrics': ' ki ho karegaa zamaanaa kyaa sach ko chhupaanaa kyaa     duniyaa ko aao batalaa den aa karegaa zamaanaa kyaa sach ko chhupaanaa kyaa     duniyaa ko aao batalaa den ki tum ho mere ham hain tere     daarling hai na bolo hai nathreedots  ki meraa sab kuchh tere lie teraa sab kuchh mere lie     bolo bolothreedots aa meraa sab kuchh tere lie teraa sab kuchh mere lie     aakhir ko haithreedots ki haan aakhir ko hain biivii miiyaan     daarling hai na bolo hai nathreedots  ki aae hue badii duur se hain ham to yahaan maiijuun se hain aa aae hue badii duur se hain ham to yahaan maiijuun se hain     aur aaj hiithreedots ki aur aaj hii hai vaapasii     daarling hai na bolo hai nathreedots', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'karegaa zamaanaa kyaa sach ko chhupaanaa kyaa', 'year': '-1'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "kalyanjianandji", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='r d burman' in top3=['laxmikantpyarelal', 'kalyanjianandji', 'shankarjaikishan']

### #194 — PASS

- item: `{'lyrics': ' niind ud rahii hai chain kho rahaa hai jaan jaa rahii hai ye kyaa ho rahaa hai ye kyaa ho rahaa hai ye kyaa ho rahaa hai aise naa mujhe dekho meraa dil dhadak rahaa hai niind ud rahii hai threedots  khushbuu khushbuu baaten terii mahakaa mahakaa cheharaa teraa terii baahen terii naramii saanson kii ye bhiinii garmii baarish kii buundon men saagar kii laharon men tum ho sanam diivaanii ho gaii huun aisaa lag rahaa hai jaan jaa rahii hai threedots  dhadakan merii sun lo jaanam kahatii kyaa hai socho jaanam tumase rishtaa itanaa gaharaa do hii pal men sadiyon jaisaa nagamon men saajon men dil men tum ho sanam dil ke mandiron men teraa diip jal rahaa hai niind ud rahii hai threedots ', 'correct_label': 'annu malik', 'label': 1, 'split': 'test', 'title': 'niind ud rahii hai  ye kyaa ho rahaa hai', 'year': '-1'}`
- output: `{"pred": "annu malik", "top3": ["annu malik", "shankarjaikishan", "r d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='annu malik' ref='annu malik'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='annu malik' in top3=['annu malik', 'shankarjaikishan', 'r d burman']

### #195 — PASS

- item: `{'lyrics': ' yun hasaraton ke dag muhabbat men dho liye khud dil se dil ki bat kahi aur ro liye yunthreedots  ghar se chale the ham to khushi ki talash men 2 khushi ki talash men gam rah men khade the vahi sath ho liye khud dil se dil ki bat kahi aur ro liye yunthreedots  murajhaa chukaa hai phir bhii ye dil phuul hii to hai haan phuul hii to hai ab aap kii khushii ise kaanton men toliye khud dil se dil kii baat kahii aur ro liye yuun   threedots  honthon ko si chuke to zamane ne ye kaha  2 zamane ne ye kaha ye chup si kyon lagi hai aji kuchh to boliye khud dil se dil ki bat kahi aur ro liye yunthreedots  ', 'correct_label': 'madan mohan', 'label': 5, 'split': 'test', 'title': 'yuun hasaraton ke daag muhabbat men dho liye', 'year': '1958'}`
- output: `{"pred": "madan mohan", "top3": ["madan mohan", "s d burman", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='madan mohan' ref='madan mohan'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='madan mohan' in top3=['madan mohan', 's d burman', 'shankarjaikishan']

### #196 — PASS

- item: `{'lyrics': '  sochataa huun ki piyuun piyuun na piyuun taak daaman ke siyuun siyuun na siyuun dekh kar jaam kashamakash men huun kyaa karuun main jiyuun jiyuun haay na jiyuun  saavan ke mahiine men ik aag sii siine men lagatii hai to pii letaa huun do chaar ghadii jii letaa huun saavan ke mahiine men  chaand kii chaal bhii hai bahakii huii raat kii aankh bhii sharaabii hai saarii kudarat nashe men hai chuur are main ne pii lii to kyaa kharaabii hai saavan ke mahiine men threedots   barason chhalakaaye main ne ye shiishe aur ye pyaale kuchh aa j pilaa de aisii jo mukjahko hii pii daale har roz to yuun hii dil ko bahakaa ke main pii letaa huun do chaar ghadii jii letaa huun threedots  lambe jiivan se achchaa vo ik pal jo apanaa ho us pal ke baad ye duniyaa kyaa gam hai agar sapanaa ho kuchh soch ke aisii baaten ghabaraa ke main pii letaa huun do chaar ghadii jii letaa huun threedots  maikhaane men aayaa huun mausam kaa ishaaraa paa ke dam bhar ke liye baithaa huun rangiin sahaaraa paa ke saathii jo terii ziddh hai to sharamaa ke main pii letaa huun do chaar ghadii jii letaa huun threedots  ', 'correct_label': 'madan mohan', 'label': 5, 'split': 'test', 'title': 'saavan ke mahiine men ik aag sii siine men', 'year': '-1'}`
- output: `{"pred": "madan mohan", "top3": ["madan mohan", "s d burman", "kalyanjianandji"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='madan mohan' ref='madan mohan'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='madan mohan' in top3=['madan mohan', 's d burman', 'kalyanjianandji']

### #197 — PASS

- item: `{'lyrics': '  o mere bechain dil ko chain tuune diyaa shukriyaa shukriyaa o shukriyaa shukriyaa o teraa ehasaan hai jo pyaar tuune kiyaa shukriyaa shukriyaa threedots  kabhii kvaabon men maine aaaa ke terii niinden churaaiin raaton men kabhii ulajhaayaa kabhii sulajhaayaa terii zulfon ko mulaaqaaton men o merii gustaakiyon ko tuune maaf kiyaa 2 shukriyaa shukriyaa threedots  har vaqt samaaii rahatii thii maayuusii merii nigaahon men main bhatak jaataa main bahak jaataa gir jaataa main in raahon men o mere saathii mujhe tuune thaam liyaa shukriyaa shukriyaa threedots  maujon ne terii hii baat kii taaron ne teraa hii naam liyaa jab gulashan men huaa teraa guzar phuulon ne bhii daaman thaam liyaa 2 o tuune jaanejahaan dil mujhako diyaa shukriyaa shukriyaa threedots ', 'correct_label': 'kalyanjianandji', 'label': 3, 'split': 'test', 'title': 'o mere bechain dil ko chain tuune diyaa shukriyaa shukriyaa', 'year': '1967'}`
- output: `{"pred": "kalyanjianandji", "top3": ["kalyanjianandji", "annu malik", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='kalyanjianandji' ref='kalyanjianandji'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='kalyanjianandji' in top3=['kalyanjianandji', 'annu malik', 'laxmikantpyarelal']

### #198 — FAIL

- item: `{'lyrics': ' ye kaun aayaa roshan ho gaii mahafil kisake naam se mere ghar men jaise suuraj nikala hai shaam se ye kaun aayaa  yaaden hain kuchh aaii sii yaa kiranen laharaaii sii dil men soe giiton ne lii hai phir angadaaii sii armaanon kii madiraa chhalake ankhiyon ke jaam se ye kaun aayaa  kyaa kahie is aane ko aayaa hai tarasaane ko dekhaa usane hans hans ke har apane begaane ko lekin kitanaa beparvaah hai mere hii salaam se ye kaun aayaa', 'correct_label': 'naushad', 'label': 6, 'split': 'test', 'title': 'ye kaun aayaa roshan ho gaii mahafil kisake naam se', 'year': '1968'}`
- output: `{"pred": "c ramchandra", "top3": ["c ramchandra", "laxmikantpyarelal", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='c ramchandra' ref='naushad'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='naushad' in top3=['c ramchandra', 'laxmikantpyarelal', 'shankarjaikishan']

### #199 — FAIL

- item: `{'lyrics': '  hamaare desh men kahate the har ladakii hindustaanii yaa raadhaa hai yaa siitaa hai yaa jhaansii kii raanii raamaa ho raamaa 3  hamane gaanv ke panaghat pe bhaii hamane gaanv ke panaghat pe dekhii thii panihaariyaan chakkar khaa gae ham to re bhaiyaa dekh shahar kii naariyaan ho ho  yahaan sadake hain vahaan galiyaan thiin yahaan kaante hain vahaan kaliyaan thiin vahaan taangaa thaa yahaan tamatam hai vahaan gorii thii yahaan madam hai vahaan paayal thii yahaan sandal hai vahaan jhuumar thaa yahaan pandel hai vahaan ghuunghat thaa yahaan jalavaa hai vahaan shaanti thii yahaan balavaa hai baatbaat pe karatii  hain ye ladane kii taiyaariyaan chakkar khaa gae ham threedots  koii bulabul hai koii titalii koii sholaa hai koii bijalii hai koii ma hai koii ba hai koiikoii to pa hai bas naam hii to ek asalii hai baaqii jo hai sab naqalii hai kaisii dolii kyaa baaraatii kud chun len ye jiivansaathii  shaadii se pahale karatii hain  2 aksar prem kuvaanriyaan chakkar khaa gae ham threedots ', 'correct_label': 'laxmikantpyarelal', 'label': 4, 'split': 'test', 'title': 'hamaare desh men kahate  hamane gaanv ke panaghat pe', 'year': '1972'}`
- output: `{"pred": "kalyanjianandji", "top3": ["kalyanjianandji", "a r rahman", "annu malik"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='kalyanjianandji' ref='laxmikantpyarelal'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='laxmikantpyarelal' in top3=['kalyanjianandji', 'a r rahman', 'annu malik']

### #200 — PASS

- item: `{'lyrics': ' aise naa thukaraao aise naa o thukaraao ai sanam ab ke gaye to phir naa aaenge ham o aise naa thukaraao ai sanam ab ke gaye to phir naa aaenge ham  kaise ham usase kahen ab koii sapanaa nahiin bhiigii aankhon men tere sivaa tadape dil jisake liye koii aisaa dilabar nahiin suunii raaton men tere sivaa o aise naa threedots  ham to tuutaa dil liye ye jalate aansuu piiye bhatakenge jaane kahaan kahaan par itanaa tum bhii suno ki chaahanewaalaa koii  milataa hai mushakil se jaanejaan o aise naa threedots', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'aise naa thukaraao', 'year': '1985'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "s d burman", "madan mohan"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='r d burman' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='r d burman' in top3=['r d burman', 's d burman', 'madan mohan']

### #201 — PASS

- item: `{'lyrics': ' raqqaasaa meraa naam raqqaasaa mera naam ai saahib sab ko salaam 2 aap kii kidamat ke liye main haazir huun aaj kii shaam raqqaasaa meraa naam ai saahib saba ko salaam  taubaa taubaa dekhe to mere andaaz koii aa uu taubaa taubaa dekhe to mere andaaz koii phir sun ke dekhe apane dil kii aawaaz koii maine chhedii gazal ab chhedegaa koii mahveraqs huun main dekho mahvediid hain log tamaam ai saahib 2 raqqaasaa meraa naam ai saahiib saba ko salaam  rafii marahabaa dilarubaa marahabaa e dilarubaa 3 taubaa aashaa taubaa rafii al habiibii khubas marhabaa e dilarubaa taubaa aashaa o o rafii taariif ke qaabil hai tuu ik hasiin qaatil hai tuu ik nazar dekh idhar jaanejigar dil chaahe bas ho jaauun tere ishq men main badanaam raqqaasaa teraa naam aashaa ai saahib sab ko salaam rafii o raqqaasaa teraa naam aashaa ai saahib sab ko salaam aap kii kidamat ke liye main haazir huun aaj kii shaam raqqaasaa meraa naam ai saahib sab ko salaam', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'raqqaasaa meraa naam', 'year': '1979'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "laxmikantpyarelal", "kalyanjianandji"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='r d burman' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='r d burman' in top3=['r d burman', 'laxmikantpyarelal', 'kalyanjianandji']

### #202 — PASS

- item: `{'lyrics': ' jaan tum ho merii duuriyaan kyuun ham se  ab to aa ke mil jaa pyaas man men kab se  ye suhaanii shaam hai pyaar kar le ham se  chuum lo aao mujhe hai guzaarish tum se  jaan tum ho merii pyaar ho gayaa tum se  main bhii to huun pyaasaa tum ko dekhaa jab se  ye javaanii kaa nashaa chhaa rahaa hai kab se  ho naa jaaye josh men bhuul koii ham se   aaj tum lagatii ho sundar khilate phuulon kii jaisii  jhilamilaatii terii aankhen chandaa taaron ke jaisii  saath mil kar jaanejaan aao ham naachenge  mastiyon men jhuumenge aao ham gaayenge  ye nazaare aur tum saath mere hamadam  aaj apane pyaar kaa ho gayaa hai sangam   tuufaanon men bhii ai saathii tum ko ham naa chhodenge  mushkil se hotii hai mohabbat janamjanam naa todenge  aaj meraa dil bole phuulon pe so jaayen  jaan merii kah do tum baanhon men kho jaayen  jaan terii hai sadaa kah rahii hai dhadakan  dil men rahate ho sadaa tum hii mere hamadam ', 'correct_label': 'a r rahman', 'label': 0, 'split': 'test', 'title': 'jaan tum ho merii duuriyaan kyuun ham se', 'year': '1997'}`
- output: `{"pred": "a r rahman", "top3": ["a r rahman", "r d burman", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='a r rahman' ref='a r rahman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='a r rahman' in top3=['a r rahman', 'r d burman', 'shankarjaikishan']

### #203 — PASS

- item: `{'lyrics': ' lataa\taavaaz deke hamen tum bulaao mohabbat men itanaa naa hamako sataao  abhii to merii zindagii hai pareshaan kahiin mar ke ho khaak bhii na pareshaan diye kii tarah se na hamako jalaao mohabbat men itanaa naa hamako sataao  rafii\tmain saanson ke har taar men chhup rahaa huun main dhadakan ke har raag men bas rahaa huun zaraa dil kii jaanib nigaahen jhukaao mohabbat men itanaa naa hamako sataao  lataa\tnaa honge agar ham to rote rahoge sadaa dil kaa daaman bhigote rahoge jo tum par mitaa ho use naa mitaao mohabbat men itanaa naa hamako sataao  rafii\taavaaz deke hamen tum bulaao mohabbat men itanaa naa hamako sataao', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'aavaaz deke hamen tum bulaao mohabbat men itanaa naa hamako sataao', 'year': '1962'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "s d burman", "annu malik"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='shankarjaikishan' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='shankarjaikishan' in top3=['shankarjaikishan', 's d burman', 'annu malik']

### #204 — FAIL

- item: `{'lyrics': '  mu \t dhaaginaa tinak dhin  2 taa thaiyaa \t dhaaginaa tinak dhin  3 vaah bhaiyaa \tjab tak ye sansaar nachaae jab tak ye sansaar \tjab tak ye sansaar nachaae jhuumjhuum ke naache jaa \tdhaaginaa tinak dhin threedots  \tare vaah mere baanke naacho isii latak se \tlachakaao re kamariyaa ho zaraa aur matak ke \tjag tujhape hanse to chal sar ko jhatak ke \tzaraa aur maze se pyaare thumakthumak ke \tsar par topii laal sajaae sar par topii laal \tsar par topii laal sajaae muunchh taan ke naache jaa \tdhaaginaa tinak dhin threedots uu \t\tdhaaginaa tinak dhin threedots  mu \tpag dekh ruke naa chaahe bahe pasiinaa \tho terii raah take hai kahiin koii hasiinaa \tsapanon men basar ho chaahe kaii mahiinaa \tshiqavaa mat kariyo pyaare yahii hai jiinaa \tjab tak pag betaal na jaae yuun hii umar bhar naache jaa do \t\tdhaaginaa tinak dhin threedots ', 'correct_label': 'laxmikantpyarelal', 'label': 4, 'split': 'test', 'title': 'dhaaginaa tinak dhin  jab tak ye sansaar nachaae', 'year': '1966'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "s d burman", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='r d burman' ref='laxmikantpyarelal'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='laxmikantpyarelal' in top3=['r d burman', 's d burman', 'laxmikantpyarelal']

### #205 — PASS

- item: `{'lyrics': ' vaae vaahe zuum zuum zuum vaae vaahe pa ni pa ni saa saa saa ga re saa ni pa ni pa ni saa saa saa ma re saa ra ra ra ra ra kuchh saal pahale doston ye baat huii thii hamako bhii muhabbat kisii ke saath huii thii apanii bhii kabhii pahalii mulaakaat huii thii hamako bhii muhabbat threedots  baarish men sadak par chhatarii pakad kar main jaa rahaa thaa yuun vo aa rahii thii yuun yuun yuun yuun yuun haay pakadaa gae donon ghabaraa gae donon ghabaraake ye kahaa jii maaf kiijiye matalab thaa jisakaa ye dil hamako diijiye ho romance ho gayaa bychance ho gayaa ham ban gae sanam thaa vaqt bahut kam jaldii se dil diyaa pandit bulaa liyaa ghode pe baith ke ham duulhaa ban gae kitanii hasiin vo milan kii raat huii thii hamako bhii muhabbat threedots  phir kyaa huaa kyaa huaa raaj baabuu haan kyaa jaane kyaa khabar kisakii lagii nazar vaadon ko todake yaadon ko chhodake vo kyaa bichhad gaii duniyaa ujad gaii diipak hai lau nahiin main huun vo nahiin vo nahiin vo nahiin  hotii vo aaj to dholak bajaatii vo mastii men jhuumatii betii ko chuumatii detii duaaen vo letii balaaen vo gaatii suhaag vo lagatii na aag vo main jisamen jal gayaa sab kuchh badal gayaa us roz aansuon kii barasaat huii thii hamako bhii muhabbat threedots  nagamen hain shikave hain kisse hain baaten hain baaten bhuul jaatii hain yaaden yaad aatii hain yaaden yaaden yaaden ye yaaden kisii dilojaanam ke chale jaane ke baad aatii hain ', 'correct_label': 'annu malik', 'label': 1, 'split': 'test', 'title': 'kuchh saal pahale doston ye baat huii thii', 'year': '2001'}`
- output: `{"pred": "annu malik", "top3": ["annu malik", "madan mohan", "kalyanjianandji"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='annu malik' ref='annu malik'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='annu malik' in top3=['annu malik', 'madan mohan', 'kalyanjianandji']

### #206 — FAIL

- item: `{'lyrics': ' naa jaane din kaise jiivan men aaye hain ke mujhase to bichhade kud mere saaye hain  kyaa kyaa sochaa thaa kyaa thii ummiiden jisake liye bhii mainne kho dii aankhon kii ye niinden usiise dukhon ke tohafe ye paaye hain naa jaane threedots  samajhaa sukh jisako chhaayaa thii gam kii jaise kahiin ret pe chamake kuchh buunden shabanam kii ye dhokhe nazar ke hamane bhii khaaye hain naa jaane threedots', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'naa jaane din kaise jiivan men aaye hain', 'year': '1977'}`
- output: `{"pred": "kalyanjianandji", "top3": ["kalyanjianandji", "shankarjaikishan", "r d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='kalyanjianandji' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='r d burman' in top3=['kalyanjianandji', 'shankarjaikishan', 'r d burman']

### #207 — FAIL

- item: `{'lyrics': '  main vahii vahii baat 2 mere lie to har din nayaa din har raat naii raat main vahii vahii baat threedots  achchhii yaa karaab pii lii jaisii milii sharaab pii lii saaqii nayaa hai jaam puraanaa rang nayaa hai naam puraanaa subah ho yaa shaam mujhe mastii se kaam kyuunki har din nayaa din threedots  apanaa hii lahuu pii rahaa huun marane ki lie jii rahaa huun dil apanaa hai gam apane hain duniyaa paraaii  ham apane hain  2 mujhe aae naa qaraar main rahuun beqaraar kyuunki har din nayaa din threedots ', 'correct_label': 'laxmikantpyarelal', 'label': 4, 'split': 'test', 'title': 'main vahii vahii baat  har din nayaa din har raat naii raat', 'year': '1974'}`
- output: `{"pred": "madan mohan", "top3": ["madan mohan", "shankarjaikishan", "c ramchandra"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='madan mohan' ref='laxmikantpyarelal'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='laxmikantpyarelal' in top3=['madan mohan', 'shankarjaikishan', 'c ramchandra']

### #208 — FAIL

- item: `{'lyrics': '  shaa \tpaigaam laayaa saawan \tdaaman se bandh jaaye daaman \trimajhim kushiyon kii barase ham pe barakhaa \tchanchal hawaa ye bolii \tsajanii phir terii dolii \tdolii phir dole jaise dole chandaa \tjii karataa hai pankh lagaa ke ud jaauun main \tniil gagan ko baadal ban ke chhuu jaauun main \tjii karataa hai pankh lagaa ke ud jaauun main  ka \tbarakhaa pawan ye buunden \tsabane udaa dii niinden \tjaagii aankhon men merii jaagaa sapanaa \tmanawaa meraa bhii dole \thaule haule ye bole \tbegaanii duniyaa men hai tuu hii apanaa \tjii karataa hai pankh lagaa ke ud jaauun main \tniil gagan ke baadal tujh men chhup jaauun main \tjii karataa hai pankh lagaa ke ud jaauun main  \tbarakhaa pawan ye buunden \tsabane udaa dii niinden \tjaagii aankhon men merii jaagaa sapanaa \t ko \tsii le sii le  shaa \tsaagar kinaare kisii parabat ke saaye men \tdikhataa hai ek aashiyaan ka \thai jaan jab tak main rahuun tere dil men hii \tvahii hai meraa aashiyaan shaa \tmaasuum hain baaten aisii \tphuulon pe ho shabanam jaisii \tmain khil saa gayaa \tmahak uthaa jag saaraa\t  ka \tjii karataa hai pankh lagaa ke ud jaauun main \tniil gagan ke baadal tujh men chhup jaauun main  shaa \tjii karataa hai pankh lagaa ke ud jaauun main \tpaigaam laayaa saawan \tdaaman se bandh jaaye daaman \trimajhim kushiyon kii barase ham pe barakhaa  ka \tmanawaa meraa bhii dole \thaule haule ye bole \tbegaanii duniyaa men hai tuu hii apanaa  ko \tsii le sii le  ka \tshaakon pe jhuulaa jhuulen naii navelii ye kaliyaan \tterii baanhon men jhuulen ham shaa \tchaahat kaa mausam aayaa \ttanahaaii sang laayaa \tmadahosh hain aaj ham ka \tmadahoshii ab naa tuute \tdaaman ye teraa naa chhuute \thai sang teraa rang teraa meraa kyaa  shaa \tjii karataa hai pankh lagaa ke ud jaauun main \tniil gagan ko baadal ban ke chhuu jaauun main \t ka \tjii karataa hai pankh lagaa ke ud jaauun main  shaa \tpaigaam laayaa saawan \tdaaman se ka \tjaagii aankhon men merii jaagaa sapanaa  ka \tjii karataa hai pankh lagaa ke ud jaauun main \tniil gagan ke baadal tujh men chhup jaauun main \tjii karataa hai pankh lagaa ke ud jaauun main \tjii karataa hai pankh lagaa ke ud jaauun main ', 'correct_label': 'a r rahman', 'label': 0, 'split': 'test', 'title': 'paigaam laayaa saawan daaman se bandh jaaye daaman', 'year': '2004'}`
- output: `{"pred": "annu malik", "top3": ["annu malik", "a r rahman", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='annu malik' ref='a r rahman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='a r rahman' in top3=['annu malik', 'a r rahman', 'shankarjaikishan']

### #209 — PASS

- item: `{'lyrics': ' ko \t chinnammaa chilakammaa \tchuud chuud chhuuduu \tchindammaa gurachammaa \taadu aadu aaduu 2  \twatch out  \t chinnammaa chilakammaa \tchuud chuud chhuuduu \tchindammaa gurachammaa \taadu aadu aaduu 2  \t guruchammaa gurugammaa \tthulasammaa ganagammaa  2  \t chinnammaa chilakammaa \tchindammaa gurachammaa  2  su \t titalii daboch lii mainne \tzindagii kayaal kii tere  2 \tsaare jahaan kii rangat \tmutthii men aa gaii mere \tzindagii kayaal kii tere \thansataa huaa chaman dede \tshiqawe shiqaayaton kaa dam \tdaaman gamon ko bhii dede  ko \t chinnammaa chilakammaa \tchindammaa gurachammaa  2  \t guruchammaa gurugammaa \tthulasammaa ganagammaa  2  \t chinnammaa chilakammaa \tchindammaa gurachammaa   \tballii ballii ballii ballii  su \tgaliyaan merii ko \trangiinrangiin su \tmahafil merii ko \trangiinrangiin su \traste mere afasaane  su \tummiiden hain ko \trangiinrangiin su \tdiipak mere ko \trangiinrangiin su \tummiiden hain diipak mere \tummiiden hain parawaane  \tzindagii kayaal kii tere \thansataa huaa chaman dede \tshiqawe shiqaayaton kaa dam \tdaaman gamon ko bhii dede  ko \tchinnammaa chilakammaa \tchindammaa gurachammaa  \tguruchammaa gurugammaa \tthulasammaa ganagammaa  \tchittammaa ragammaa 2  su \tqadamon pe ab ko \trangiinrangiin su \tbaandh liin mainne ko \trangiinrangiin su \tsisakiyaan saarii yaaro  su \tpyaasii aankhon ko \trangiinrangiin su \tmen bhar daaliin ko \trangiinrangiin su \tkwaahish kii nazaren yaaro \t \tzindagii kayaal kii tere \thansataa huaa chaman dede \tshiqawe shiqaayaton kaa dam \tdaaman gamon ko bhii dede  \t titalii daboch lii mainne \tzindagii kayaal kii tere  2 \tsaare jahaan kii rangat \tmutthii men aa gaii mere \tzindagii kayaal kii tere \thansataa huaa chaman dede \tshiqawe shiqaayaton kaa dam \tdaaman gamon ko dede  ko \t chinnammaa chilakammaa \tchindammaa gurachammaa  2  \t guruchammaa gurugammaa \tthulasammaa ganagammaa  2  \tchinnammaa chilakammaa 2 ', 'correct_label': 'a r rahman', 'label': 0, 'split': 'test', 'title': 'chinnamma chilakammaa  titalii daboch lii mainne', 'year': '2003'}`
- output: `{"pred": "a r rahman", "top3": ["a r rahman", "kalyanjianandji", "naushad"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='a r rahman' ref='a r rahman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='a r rahman' in top3=['a r rahman', 'kalyanjianandji', 'naushad']

### #210 — FAIL

- item: `{'lyrics': ' puuchho naa kaise maine rain bitaai ik pal jaise ik yug biita  2 yug biite mohe niind naa aayii puuchho naa kaise threedots  naa kahiin chandaa naa kahiin taare jyot ke pyaase mere nain bichaare   2 bhor bhii aas kii kiran naa laayi puuchho naa kaise threedots  ik jale diipak ik man meraa mera man mera mera threedots ik jale diipak ik man meraa phir bhi naa jaaye mere ghar kaa andheraa tadapat tarasat umar ganvaayii puuchho naa kaise threedots', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'puuchho naa kaise main ne rain bitaaii ik pal jaise ik yug biita', 'year': '1963'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "s d burman", "naushad"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='s d burman' in top3=['laxmikantpyarelal', 's d burman', 'naushad']

### #211 — FAIL

- item: `{'lyrics': ' gaataa rahe meraa dil tuu hii merii manzil kahiin biiten na ye raaten kahiin biiten na ye din  2  pyaar karane vaale are pyaar hii karenge jalane vaale chaahe jal jal marenge dil se jo dhadake hain vo dil haradam ye kahenge kahiin biiten na threedots  o mere hamaraahii merii baanh thaame chalanaa badale duniyaa saarii tum na badalanaa pyaar hame bhii sikhalaa degaa garadish men sambhalanaa kahiin biiten na threedots  duuriyaan ab kaisii are shaam jaa rahii hai hamako dhalate dhalate samajhaa rahii hai aatii jaatii saans jaane kab se gaa rahii hai kahiin biiten na threedots ', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'gaataa rahe meraa dil tuu hii merii manzil', 'year': '1965'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "laxmikantpyarelal", "r d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='shankarjaikishan' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='s d burman' in top3=['shankarjaikishan', 'laxmikantpyarelal', 'r d burman']

### #212 — PASS

- item: `{'lyrics': '  taakaa dhinaa taak dhinaa taa  aa aa aa aa aa o aa ho o ho o  chaaron taraf machii traahimaam jab paapiyon kii badh jaae trishnaa tab dharm ko bachaane chalaa nae ruup men aa jaae krishnaa om om om om om om namah shivaay krishnaa o krishnaa  om om om om om om namah shivaay  so \tjiitenge baazii ham himmat naa hogii kam 2 ma \tdil men hai ik agan man men hai ik lagan do \thamane lii hai qasam  om om om om om om namah shivaay krishnaa o krishnaa  taakaa dhinaa dhinaa taa taa daa taa daa taakaa dhinaa dhinaa taa  so \thamane kiyaa faisalaa haarenge naa hausalaa \tkatare men ye jaan ho koii bhii tuufaan ho  koii samay ho koii naxatr le ke chalen ye haathon ke astr kar denge apane dushman ko past honge kisii se ham na past  om om om om om om namah shivaay krishnaa o krishnaa  so \tjiitenge baazii ham himmat naa hogii kam 2 ma \tdil men hai ik agan man men hai ik lagan do \thamane lii hai qasam  chaaron taraf machii traahimaam jab paapiyon kii badh jaae trishnaa tab dharm ko bachaane chalaa nae ruup men aa jaae krishnaa  om om om om om om namah shivaay  koii samay ho koii naxatr le ke chalen ye haathon ke astr kar denge apane dushman ko past honge kisii se ham na past  krishnaa o krishnaa  om om om om om om namah shivaay ', 'correct_label': 'annu malik', 'label': 1, 'split': 'test', 'title': 'chaaron taraf  om namah shivaay  krishnaa  jiitenge baazii ham', 'year': '2003'}`
- output: `{"pred": "annu malik", "top3": ["annu malik", "laxmikantpyarelal", "a r rahman"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='annu malik' ref='annu malik'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='annu malik' in top3=['annu malik', 'laxmikantpyarelal', 'a r rahman']

### #213 — FAIL

- item: `{'lyrics': ' kuchh din pahale ek taal men kamal kunj ke andar rahataa thaa ek hans kaa jodaa ek hans kaa jodaa    roz roz roz bhor hote hii jab khil jaate kamal duur duur duur motii chugane ko hans ghar se jaataa nikal  2 sandhyaa hotii sandhyaa hotii ghar ko aataa jhuum jhuum ke kuchh din pahalethreedots    jab jab jab dhal jaataa thaa din taare jaate the khil so jaate hilmil ke vo donon jaise laharon ke dil  2 chandaa hansataa chandaa hansataa donon kaa mukh chuum chuum ke kuchh din pahalethreedots    thii unakii ek nanhii sii betii chhotii sii hansanii donon ke nayanon kii vo jyotii ghar kii raushanii 2 mamataa gaatii mamataa gaatii aur muskaatii jhuum jhuum ke kuchh din pahalethreedots   kuchh din pahale ek taal men kamal kunj ke andar kaun thaa ek hans kaa jodaa ek hans kaa jodaa    phir ek din aisaa tuufaan aayaa chalii aisii havaa bechaare hansaa ud gae re hoke sabase judaa 2 saagarsaagar saagarsaagar saagarsaagar rote hain ab ghuum ghuum ke ghuum ghuum ke', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'kuchh din pahale ek taal men kamal kunj ke andar', 'year': '1958'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "laxmikantpyarelal", "s d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='r d burman' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='s d burman' in top3=['r d burman', 'laxmikantpyarelal', 's d burman']

### #214 — FAIL

- item: `{'lyrics': '  aae re din saavan ke saavan ke balam tere aavan ke aavan ke aae re din threedots  tere pyaar kaa jog liyaa mohe log kahen diivaanii 2 ho gharghar kii is kahaasunii men main ban gaii kahaanii o aae re din threedots  do nainon ke diip jalaae jaaguun saarii rainaa 2 o kaise laagen nain piyaa jab tum sang laage nainaa o aae re din threedots ', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'aae re din saavan ke balam tere aavan ke', 'year': '1966'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "naushad", "r d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='shankarjaikishan' in top3=['laxmikantpyarelal', 'naushad', 'r d burman']

### #215 — FAIL

- item: `{'lyrics': '  mere lie aatii hai shaam chandaa bhii hai meraa gulaam dharatii se sitaaron tak hai meraa intazaam raaton kaa raajaa huun main  mahafil saje doluun jidhar se saaqii bahake merii nazar se chaahuun to abhii khud chal ke aae jaam raaton kaa raajaa threedots  khidakii khule mujhe bulaae mahalon men hai mere hii saae sotejaagate sab jaanen meraa naam raaton kaa raajaa threedots  mainen javaan honthon kii laalii akasar palakon se hii churaa lii saare gulabadan mujhe karate hain salaam dharatii se sitaaron tak threedots ', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'mere lie aatii hai shaam  raaton kaa raajaa huun main', 'year': '1970'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "s d burman", "r d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='r d burman' in top3=['laxmikantpyarelal', 's d burman', 'r d burman']

### #216 — FAIL

- item: `{'lyrics': ' lataa thandii thandii hawaa khaane raajaa gayaa gaanv men jaate jaate muii suii chubh gayii paanv men raajaa ne waziir bhejaa raanii daudii aaii raajaa kii sawaarii ko kaalii ghodii laaii ho aage aage baithaa raajaa piichhe baithii raanii raanii ne sunaaii aake munne ko kahaanii raajaa jaanii pyaare chor hamaare luk chhup luk chhup jaanaa chaahe koii jiite chaahe koii haare luk chhup luk chhup jaanaa  ko  raajaa jaanii pyaare chor hamaare luk chhup luk chhup jaanaa  ko aaaa lataa  dhuup banii bebii to baabaa banaa saayaa dhuup ke piichhe dekho saayaa daudaa aayaa 2 daudaa aayaa daudaa aayaa ko  dekho aayaa aayaa aayaa la  ho duniyaa se nyaare khel hamaare luk chhup luk chhup jaanaa ko raajaa jaanii pyaare chor hamaare luk chhup luk chhup jaanaa  la  phuul se ik din bulabul bolii aajaa khelen aankh michaulii ko  aa aa la  phuul ye kahane lagaa tuu ud jaaegii haath na aaegii ghuum ke daalii daalii giit ye gaaegii ho  raajaa jaanii pyaare chor hamaare luk chhup luk chhup jaanaa ko  chaahe koii jiite chaahe koii haare luk chhup luk chhup jaanaa  la badalii ke piichhe jo chhup gayaa taaraa dhuundh dhuundh haaraa chandaa maamaa bechaaraa 2 dekho haaraa haaraa haaraa ko chandaa maamaa bechaaraa la  ho piichhe piichhe chandaa aage aage taare luk chhup luk chhup jaanaa raajaa jaanii pyaare chor hamaare luk chhup luk chhup jaanaa ko  chaahe koii jiite chaahe koii haare luk chhup luk chhup jaanaa', 'correct_label': 'madan mohan', 'label': 5, 'split': 'test', 'title': 'thandii thandii hawaa khaane  raajaa jaanii pyaare chor hamaare', 'year': '1956'}`
- output: `{"pred": "s d burman", "top3": ["s d burman", "c ramchandra", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='s d burman' ref='madan mohan'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='madan mohan' in top3=['s d burman', 'c ramchandra', 'laxmikantpyarelal']

### #217 — PASS

- item: `{'lyrics': '  aaj hai pyaar kaa faisalaa ai sanam aaj meraa muqaddar badal jaaegaa tuu agar sangadil hai to paravaah nahiin mere nagamon se patthar pighal jaaegaa  dekh main huun badii chot khaae hue tere qadamon men huun sar jhukaae hue aa gale se lagaa le mujhe varanaa phir baat rah jaaegii vaqt tal jaaegaa aaj hai pyaar kaa threedots  dil ko mere teraa dil nahiin chaahie aur sivaa isake kuchh nahiin chaahie tuune kar dii agar ik nigaaheqaram meraa tuutaa huaa dil sambhal jaaegaa aaj hai pyaar kaa threedots ', 'correct_label': 'naushad', 'label': 6, 'split': 'test', 'title': 'aaj hai pyaar kaa faisalaa ai sanam', 'year': '1964'}`
- output: `{"pred": "naushad", "top3": ["naushad", "shankarjaikishan", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='naushad' ref='naushad'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='naushad' in top3=['naushad', 'shankarjaikishan', 'laxmikantpyarelal']

### #218 — FAIL

- item: `{'lyrics': ' aa jaao ki sab mil ke rab se duaa maangen  jiivan men sukuun chaahen chaahat men vafaa maangen  haalaat badalane men ab der na ho maalik  jo de chuke phir le andher na ho maali   ek tuu hii bharosaa ek tuu hii sahaaraa  is tere jahaan men nahiin koii hamaaraa  he ishvar yaa allaah ye pukaar sunale  he ishvar yaa allaah he daataa   hamase naa dekhaa jaaye barabaadiyon kaa samaan  ujadii huii bastii men ye tadap rahe insaan  nanhe jismon ke tukade liye khadii hai ek maan  baaruud ke dhuven men tuu hii bol jaaye kahaan   naadaan hain ham to maalik kyuun dii hamen ye sazaa  yaa hai sabhii ke dil men nafarat kaa zahar bharaa  inhen phir se yaad dilaa de sabak vahii pyaar kaa  ban jaaye gulashan phir se kaanton bharii duniyaa  merii pukaar sun le ', 'correct_label': 'a r rahman', 'label': 0, 'split': 'test', 'title': 'aa jaao kii sab mil ke  ek tuu hii bharosaa', 'year': '1999'}`
- output: `{"pred": "s d burman", "top3": ["s d burman", "r d burman", "naushad"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='s d burman' ref='a r rahman'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='a r rahman' in top3=['s d burman', 'r d burman', 'naushad']

### #219 — FAIL

- item: `{'lyrics': '  zindagii aaj mere naam se sharamaatii hai apane haalaat pe mujhe khud hii hansii aatii hai zindagii aaj mere threedots  ek gam chain se jiine nahiin detaa mujhako 2 ek ulajhan hai jo aksar mujhe tadapaatii hai zindagii aaj mere threedots  is tarah chhod ke nikalaa huun main apanii manzil jaise hasarat koii siine se nikal jaatii hai zindagii aaj mere threedots  raah chalate hue kuchh soch ke ruk jaataa huun 2 har qadam par koii bhuulii huii yaad aatii hai zindagii aaj mere threedots ', 'correct_label': 'naushad', 'label': 6, 'split': 'test', 'title': 'zindagii aaj mere naam se sharamaatii hai', 'year': '1962'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "laxmikantpyarelal", "naushad"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='shankarjaikishan' ref='naushad'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='naushad' in top3=['shankarjaikishan', 'laxmikantpyarelal', 'naushad']

### #220 — FAIL

- item: `{'lyrics': ' aa mere saathii aa dil kii baat sunataa jaa raahon men bichhaauun taare ho ho aa mere saathii aa dil kii baat sunataa jaa raahon men bichhaauun taare  ruu  ruu ruu ruu ruu  ruu ruu ruu ruu  ruu ruu ruu ruu   wahaan terii duniyaa jahaan main huun magar tuu naa jaane kahaan main huun  2 ujaalon men khoye hue  o sanam yahaan main huun mere hamadam yahaan main huun ho ho aa mere saathii aa dil kii baat sunataa jaa raahon men bichhaauun taare   idhar bhii zaraa bekabar dekh le jo dhuundhe tujhe wo nazar dekh le  2 pukaaruun main kab se tujhe o sanam udhar tuu hai mere hamadam idhar main huun ho ho aa mere saathii aa dil kii baat sunataa jaa raahon men bichhaauun taare   zamiin se pare is jahaan se pare mere saath chal aasamaan se pare  2 kayaalon men duube hue o sanam jawaan tuu hai mere hamadam jawaan main huun ho ho aa mere saathii aa dil kii baat sunataa jaa raahon men bichhaauun taare ', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'aa mere saathii aa', 'year': '1973'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "madan mohan", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='r d burman' in top3=['laxmikantpyarelal', 'madan mohan', 'shankarjaikishan']

### #221 — FAIL

- item: `{'lyrics': ' aa\tjaba andheraa hotaa hai aadhii raata ke baada \tek chorthreedots bhuu\tpaa para paathreedots aa\tthreedots nikalataa hai kaalii sii sadaka pe \tye aavaaza aatii hai dono\tchorachora chorachora chorachora chorachora        aa\tshaharon kii galiyon men jaba andheraa hotaa hai  \taadhii raat ke baada \tek chora nikalataa hai kaalii sii sadaka pe  \tye aavaaza aatii hai \tchorachora chorachora chorachora chorachora \tshaharon kii galiyon men jabathreedots \tandheraa hotaa hai aadhii raata ke baadathreedots  aa\tloga banda kamaron men chaina se jaba sote hain bhuu\tlog banda kamaron men chaina se jaba sote hain dono\tye jaagataa hai saarii raata bhaagataa hai aa\ttale tute hote hain jaba saveraa hotaa hai ya \tpapa paraathreedots  a lot of lala laing without lyrics \tjaba andheraathreedots  aa\tsuna lo paharedaaron hosha men rahanaa yaaron bhuu\tsuna lo paharedaaron hosha men rahanaa yaaron         dono\tsaatha ghuumatii hai naagana raata jhuumatii hai aa\talbelaa mastaanaa vo saveraa hotaa hai ya \tpapa parathreedots  a lot of lala laing without lyrics \tjaba andheraathreedots', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'jaba andheraa hotaa hai aadhii raata ke baad ek chor', 'year': '1973'}`
- output: `{"pred": "a r rahman", "top3": ["a r rahman", "s d burman", "madan mohan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='a r rahman' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='r d burman' in top3=['a r rahman', 's d burman', 'madan mohan']

### #222 — FAIL

- item: `{'lyrics': ' mere saath chale naa saayaa dharam nahiin karam nahiin janam ganvaayaa  mere liye din bhii andheraa mere liye raat bhii na laaye saveraa  2 jo de ujaalaa de saveraa 2 vahii meraa hamasaayaa dharam nahiin karam nahiin threedots  mere liye jagat sautelaa bharii huii bhiid men bhii rahaa akelaa 2 jo de sahaaraa de kinaaraa 2 vahii meraa hamasaaya dharam nahiin karam nahiin threedots', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'mere saath chale naa saayaa', 'year': '1977'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "madan mohan", "kalyanjianandji"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='shankarjaikishan' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='r d burman' in top3=['shankarjaikishan', 'madan mohan', 'kalyanjianandji']

### #223 — FAIL

- item: `{'lyrics': '  pyaase panchhii niil gagan men  giit milan ke gaaen  2 is mele men ham hain akele saathii kise banaaen giit milan ke gaaen pyaase panchhii threedots  o matavaale raahii tujhako manzil kahaan bulaae kisako kabar hai in raahon men kaun kahaan mil jaae jaise saagar kii do laharen chupake se mil jaaen giit milan ke gaaen pyaase panchhii threedots  chhupii hain aahen kis premii kii baadal kii aahon men bikharii huii hai kushbuu kaisii alabelii raahon men kisakii zulfen chhuu kar aaiin mahakii huii ye havaaen giit milan ke gaaen pyaase panchhii threedots ', 'correct_label': 'kalyanjianandji', 'label': 3, 'split': 'test', 'title': 'pyaase panchhii niil gagan men  giit milan ke gaaen', 'year': '1961'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "s d burman", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='shankarjaikishan' ref='kalyanjianandji'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='kalyanjianandji' in top3=['shankarjaikishan', 's d burman', 'laxmikantpyarelal']

### #224 — PASS

- item: `{'lyrics': ' churaa lo dil churaa lo dil tum churaa lo dil meraa sanam suno buraa kyaa hai dil tumhaaraa ho chukaa sanam suno buraa kyaa hai dil denaa thaa dil de chuke tumape maranaa thaa ham mar chuke aur kyaa karen bolo naa tum churaa lo threedots  pal pal teraa ab intazaar dil bhii rahe kuchh bekaraar jiinaa mushkil huaa hai ajab pyaar kaa ye khumaar yaad terii aatii rahe jaan merii jaatii rahe ye mujhe kyaa ho gayaa bin tere kuchh naa achchhaa lage dil denaa thaa threedots  dil kii dhadakan bas tuu hii tuu merii chaahat bas tuu hii tuu lo kasam kii khaaii kasam merii duniyaa bas tuu hii tuu mujhako naa karo itanaa pyaar kal kaa kyaa pataa mere yaar is pyaar kii jiit men ho na jaae kahiin apanii haar dil denaa thaa threedots ', 'correct_label': 'annu malik', 'label': 1, 'split': 'test', 'title': 'tum churaa lo dil meraa sanam suno buraa kyaa hai', 'year': '2000'}`
- output: `{"pred": "annu malik", "top3": ["annu malik", "shankarjaikishan", "r d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='annu malik' ref='annu malik'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='annu malik' in top3=['annu malik', 'shankarjaikishan', 'r d burman']

### #225 — FAIL

- item: `{'lyrics': '  he he chaar paise kyaa mile kyaa mile bhaii kyaa mile vo kud ko samajh baithe kudaa vo kudaa hii jaane ab hogaa teraa anjaam kyaa   kaahe paise pe  2 itanaa  guruur kare hai  2  yahii paisaa to  2 apanon se  duur kare hai  2 kaahe paise pe threedots  sonechaandii ke uunche mahalon men dard zyaadaa hai chain thodaa hai 2 is zamaane men paise vaalon ne pyaar chhiinaa hai dil ko todaa hai 2 paise kii ahamiyat se to inkaar nahiin hai paisaa hii magar sab kuchh sarakaar nahiin hai insaaninsaan hai paisaapaisaa hai dil hamaaraa bhii tere jaisaa hai hai bhalaa paisaa to buraa bhii hai ye zahar bhii hai ye nashaa bhii hai 2  ye nashaa koii  2 dhokhaa zaruur kare hai yahii paisaa to threedots  are chale kahaan ai paise se kyaakyaa tum yahaan kariidoge he dil kariidoge yaa ke jaan kariidoge baazaaron men pyaar kahaan bikataa hai dukaanon pe yaar kahaan bikataa hai phuul bik jaate hain kushbuu bikatii nahiin jism bik jaate hain ruuh bikatii nahiin chain bikataa nahiin kvaab bikate nahiin dil ke aramaan betaab bikate nahiin are paise se kyaakyaa threedots   he in havaaon kaa mol kyaa doge in ghataaon kaa mol kyaa doge are in zamiinon kaa mol ho shaayad aasamaanon kaa mol kyaa doge  2 paas paisaa hai to hai ye  duniyaa hasiin  2 ho zaruurat se zyaadaa to  maanon yaqiin  2  ye dimaagon men  2 paidaa fituur kare hai yahii paisaa to threedots ', 'correct_label': 'kalyanjianandji', 'label': 3, 'split': 'test', 'title': 'he chaar paise kyaa mile  kaahe paise pe itanaa guruur', 'year': '1981'}`
- output: `{"pred": "annu malik", "top3": ["annu malik", "laxmikantpyarelal", "r d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='annu malik' ref='kalyanjianandji'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='kalyanjianandji' in top3=['annu malik', 'laxmikantpyarelal', 'r d burman']

### #226 — PASS

- item: `{'lyrics': ' jaane de gaadii terii jaane de jaane de 2 apanaa bhii hai donon paanv re 2 o o o  itanaa magar nahiin bhuulanaa bhuulanaa 2 ik hai teraa meraa gaanv re jaane de gaadii terii threedots  are tel binaa baabuu haay haay haay tel binaa baabuu ho jaayegii bekaabu ik roj tere chakare kii chaal us din phir aauungii re dekhane ko main bhii teraa haal 2 waah re waah dekho kaisaa ainth gayaa dhat jaane de gaadii terii threedots  maanaa terii surat kuchh aisii nahiin phir bhii tujhamen hain alag thodii sii baat main kuchh naa boluungii re chaahe to aajaa mere saath 2 do kadam chalaa nahiin baith gayaa dhat waah waah jaane de gaadii terii threedots  soche nahiin paagal main kitanaa chaluun paidal raste hii men naa ho jaaye shaam kar sakataa ye bhii nahiin ke badhake letaa mujhe thaam 2 besharam baithaa baithaa let gayaa dhat waah waah waah jaane de gaadii terii threedots', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'jaane de gaadii terii jaane de', 'year': '1980'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "s d burman", "madan mohan"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='r d burman' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='r d burman' in top3=['r d burman', 's d burman', 'madan mohan']

### #227 — FAIL

- item: `{'lyrics': '  aa aa raat barasaat kii pahalii mulaaqaat kii yaad rakho balamaa3 yaad rakho balamaa jo ruuthne kii baat thii  buund buund barase dil meraa tarase pahalii pahalii baar piyaa nikalii huun gharase2 chorii chorii aake sainyyaa2 main ne mulaaqaat kii raat barasaat kii   threedots  bijalii ne rokaa paanii ne tokaa  chalii aaii sochake jo hogaa so hogaa2 tere liye thand sahii2 bhiigii bhiigii raat men raat barasaat kii  threedots ', 'correct_label': 'c ramchandra', 'label': 2, 'split': 'test', 'title': 'raat barasaat kii pahalii mulaaqaat kii', 'year': '1953'}`
- output: `{"pred": "madan mohan", "top3": ["madan mohan", "s d burman", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='madan mohan' ref='c ramchandra'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='c ramchandra' in top3=['madan mohan', 's d burman', 'shankarjaikishan']

### #228 — FAIL

- item: `{'lyrics': '  aur kyaa ehadevafaa hote hain log milate hain judaa hote hain  kab bichhad jaaye hamasafar hii to hai kab badal jaaye ik nazar hii to hai jaanodil jisape fidaa hote hain aur kyaa ehadevafaa hote hain   threedots  baat nikalii thii is zamaane kii jisako aadat hai bhuul jaane kii aap kyon hamase khafaa hote hain aur kyaa ehadevafaa hote hain   threedots  jab rulaa lete hain jii bhar ke hamen jab sataa lete hain jii bhar ke hamen tab kahiin khush vo zaraa hote hain aur kyaa ehadevafaa hote hain   threedots ', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'aur kyaa ehadevafaa hote hain', 'year': '-1'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "r d burman", "kalyanjianandji"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='r d burman' in top3=['laxmikantpyarelal', 'r d burman', 'kalyanjianandji']

### #229 — PASS

- item: `{'lyrics': ' haan naa haan hothreedots  ho gumasum kyon hai sanam ab zaraa maan jaa pyaar kaa ye mausam hai aise men dil na jalaa  2 gumasum kyon hai sanam  2  jaane buujhe nazar churaaye dil kii baaten samajh na paaye o sitamagar dekh ab to ho jaa maharabaan  2 dard diyaa hai to de de davaa gumasum threedots  kab se hai beqaraar ye dil kab se kahatii huun jhuumake mil o anaadi ban khilaadi le le baahon mein  2 kaise piyaa se meraa palaa padaa gumasum threedots', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'gumasum kyon hai sanam ab zaraa maan jaa', 'year': '1978'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "s d burman", "annu malik"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='r d burman' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='r d burman' in top3=['r d burman', 's d burman', 'annu malik']

### #230 — FAIL

- item: `{'lyrics': ' chalat musaafir moh liyo re pinjade vaalii muniyaa   4 \t ud ud baithii halavaiyaa dukaniyaa  2 he raamaa ud ud baithii halavaiyaa dukaniyaa aare barafii ke sab ras le liyo re pinjade vaalii muniyaa   2 \t  a he a he threedots he raamaa \t  ud ud baithii bajajavaa dukaniyaa  2 aahaa ud ud baithii bajajavaa dukaniyaa aare kapadaa ke sab ras le liyo re pinjade vaalii muniyaa   3 \t jiyo jiyo palakadas jiyo  \t ud ud baithii panavadiyaa dukaniyaa  2 he raamaa ud ud baithii panavadiyaa dukaniyaa aare biidaa ke sab ras le liyo re pinjade vaalii muniyaa   3', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'chalat musaafir moh liyo re pinjade vaalii muniyaa', 'year': '1966'}`
- output: `{"pred": "s d burman", "top3": ["s d burman", "annu malik", "a r rahman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='s d burman' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='shankarjaikishan' in top3=['s d burman', 'annu malik', 'a r rahman']

### #231 — PASS

- item: `{'lyrics': '  ai aasamaan ke raahii tuu hii gavaah rahanaa thamataa nahiin hai kabase in aansuon kaa bahanaa teraa agar guzar ho is desh kii taraf se koii tadap rahaa hai itanaa hii unase kahanaa  haay saavan ban gae nain saavan ban gae nain piyaa bin saavan ban gae nain  suunaasuunaa ghar hai balam bin suune hain dinrain ho puuchho na jii ke bain saavan ban gae threedots  nain hamaare gangaajamanaa baadal se ye haragiz kam naa mushqil hai ansuvan kaa thamanaa katatii nahiin mose birahaa kii rain saavan ban gae threedots  dil ke chhaale phuut gae hain pyaar ke taare tuut gae hain chor mere man luut gae hain milataa nahiin mujh abhaagan ko chain saavan ban gae threedots ', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'ai aasamaan ke raahii  haay saavan ban gae nain', 'year': '1961'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "kalyanjianandji", "annu malik"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='shankarjaikishan' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='shankarjaikishan' in top3=['shankarjaikishan', 'kalyanjianandji', 'annu malik']

### #232 — PASS

- item: `{'lyrics': ' pyaar zindagii hai pyaar bandagii hai bandagii hai  yahallaa yahallaa uu yaa allaah  pyaar se pyaar karo ye umr pyaar kii hai  pyaar binaa kyaa jiinaa ye bhii koi zindagii hai pyaarthreedots  1 pyaar karam pyaar duaa pyaar sitam pyaar vafaa  pyaar se judaa to yahaan koi nahiin koi nahiin  pyaar khushii pyaar nashaa kyaa vo najar kyaa vo adaa  ho kisii ke pyaar men jo koii nahiin koii nahiin  dil ko lagaa ke dekho pyaar men kyaa khushii hai  pyaar binaa kyaa jiinaa ye bhii koi zindagii hai pyaarthreedots  2 dur rahe paas rahe dil men tere pyaas rahe  tere liye main huun tuu hai mere liye mere liye  pyaar sanam pyaar khudaa yaar kabhii ho naa judaa  yaar binaa koi yahaan kaise jiye kaise jiye  baahon men yaar ke hii duniyaa bahaar kii hai pyaarthreedots  3 dekh hamen koi jale koi jale haath male  tuu jo mere saath chale logon se kyaa daranaa yahaan  pyaar yahaan jo naa kare kaak jiye kak mare  yaar mere tere liye jiinaa yahaan maranaa yahaan  marake bhii naa mite jo ye vo divaanagii hai pyaarthreedots', 'correct_label': 'kalyanjianandji', 'label': 3, 'split': 'test', 'title': 'pyaar zindagii hai pyaar bandagii hai bandagii hai', 'year': '1978'}`
- output: `{"pred": "kalyanjianandji", "top3": ["kalyanjianandji", "r d burman", "a r rahman"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='kalyanjianandji' ref='kalyanjianandji'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='kalyanjianandji' in top3=['kalyanjianandji', 'r d burman', 'a r rahman']

### #233 — FAIL

- item: `{'lyrics': ' rafii\to hasinaa zulfon vaalii jaanejahaan dhuundhatii hain kaafir aankhen kisakaa nishaan o hasinaa zulfon vaalii jaanejahaan\t dhuundhatii hain kaafir aankhen kisakaa nishaan mahafil mahafil ai shamaa phiratii ho kahaan  2  aashaa\tvo anjaanaa dhuundhatii huun vo divaanaa dhuundhatii huun jalaakar jo chhip gayaa hai vo paravaanaa dhuundhatii huun  aashaa garm hai sez hai ye nigaahen merii rafii\tkaam aa jaayegii sard aahen merii aashaa\ttum kisii raah men to miloge kahiin rafii\tare ishq huun main kahiin thaharataa hii nahiin aashaa\tmain bhii huun galiyon kii parachhaaii kabhii yahaan kabhii vahaan shaam hii se kuchh ho jaataa hai mera bhii jaaduu javaan  rafii\to hasinaa zulfon vaalii jaanejahaan\t dhuundhatii hain kaafir aankhen kisakaa nishaan mahafil mahafil ai shamaa phiratii ho kahaan  2  aashaa\tvo anjaanaa dhuundhatii huun vo divaanaa dhuundhatii huun jalaakar jo chhip gayaa hai vo paravaanaa dhuundhatii huun  aashaa\tchhip rahe hai ye kyaa dhang hai aapakaa rafii\taaj to kuchh nayaa rang hai aapakaa aashaa\thai  aaj kii raat main kyaa se kyaa ho gayii rafii\taha aapakii saadagii to bhalaa ho gayii aashaa\tmain hii huun galiyon kii parachhaaii kabhii yahaan kabhii vahaan shaam hii se kuchh ho jaataa hai mera bhii jaaduu javaan  rafii\to hasinaa zulfon vaalii jaanejahaan\t dhuundhatii hain kaafir aankhen kisakaa nishaan mahafil mahafil ai shamaa phiratii ho kahaan  2  aashaa\tvo anjaanaa dhuundhatii huun vo divaanaa dhuundhatii huun jalaakar jo chhip gayaa hai vo paravaanaa dhuundhatii huun  aashaa\tthahariye to sahii kahiye kyaa naam hai rafii\tmerii badanaamiyon ka vafaa naam hai aashaa\toho  qatl kar ke chale ye vafaa khuub hai rafii\thai naadaan terii ye adaa khuub hai aashaa\tmain bhii huun galiyon ki parachhaai kabhii yahaan kabhii vahaan shaam hii se kuchh ho jaataa hai mera bhii jaaduu javaan  rafii\to hasinaa zulfon vaalii jaanejahaan\t dhuundhatii hain kaafir aankhen kisakaa nishaan mahafil mahafil ai shamaa phiratii ho kahaan  2  aashaa\tvo anjaanaa dhuundhatii huun vo divaanaa dhuundhatii huun jalaakar jo chhip gayaa hai vo paravaanaa dhuundhatii huun', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'o hasiinaa zulfon vaalii jaanejahaan', 'year': '-1'}`
- output: `{"pred": "kalyanjianandji", "top3": ["kalyanjianandji", "r d burman", "s d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='kalyanjianandji' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='r d burman' in top3=['kalyanjianandji', 'r d burman', 's d burman']

### #234 — FAIL

- item: `{'lyrics': ' chhotii sii umar men lag gayaa rog   chhotii sii umar meneh lag gayaa rog kahate hain log main mar jaaungii ho main mar jaaungii  2  par marane se pahale kuchh karane se pahale le ke teraa naam tujhe badanaam main kar jaauungii ho main mar jaauungii  ho ho  yehe kisii saharii chhorii kii priit nahiin hai baabuu  2 ek banjaaran keh matawaare nainonoh kaa hai jaaduu tuu na jaa merii musakaan pe khel jaauungii main jiijaan pe chhoduungii naa saath 2 aisii kyaa hai baat ke main dar jaauungii  ho main mar jaauungii  chhotii sii umar menhe lag gayaa rog kahate hain log main mar jaaungii ho main mar jaaungii  par marane se pahale kuchh karane se pahale le ke teraa naam tujhe badanaam main kar jaauungii ho main mar jaauungii  ho ho  kab talak rokegaa meraa rastaa laaj kaa paharaa  2 yaad ye rakhanaa tuu sajanaa ye meraa vaadaa thaharaa baabul kii galiyaan chhod ke aauungii chunariyaa odh ke laike umang 2 sainyaan tere sang tere ghar jaauungii  ho main mar jaauungii  chhotii sii umar menhe lag gayaa rog kahate hain log main mar jaaungii ho main mar jaaungii  par marane se pahale kuchh karane se pahale le ke teraa naam tujhe badanaam main kar jaauungii ho main mar jaauungii', 'correct_label': 'kalyanjianandji', 'label': 3, 'split': 'test', 'title': 'chhotii sii umar men lag gayaa rog', 'year': '1976'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "s d burman", "r d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='kalyanjianandji'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='kalyanjianandji' in top3=['laxmikantpyarelal', 's d burman', 'r d burman']

### #235 — FAIL

- item: `{'lyrics': ' aap kii nazaron ne samajhaa pyaar ke kaabil mujhe dil kii ai dhadakan thahar jaa mil gaii manzil mujhe aap kii nazaron ne samajhaa  jii hamen manzuur hai aapakaa ye faisalaa\t 2 kah rahii hai har nazar bandaaparavar shukariyaa do jahaan kii aaj khushiyaan ho gaiin haasil mujhe aap kii nazaron ne samajhaa threedots  aap kii manzil huun main merii manzil aap hain      2 kyuun main tuufaan se daruun mere saahil aap hain koii tuufaanon se kah de mil gayaa saahil mujhe aap kii nazaron ne samajhaa threedots  pad gaii dil par merii aap kii parchhaaiyaan         2 har taraf bajane lagiin saikadon shahanaaiyaan hansake apanii zindagii men kar liyaa shaamil mujhe aap kii nazaron ne samajhaa threedots ', 'correct_label': 'madan mohan', 'label': 5, 'split': 'test', 'title': 'aap kii nazaron ne samajhaa', 'year': '1962'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "kalyanjianandji", "madan mohan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='shankarjaikishan' ref='madan mohan'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='madan mohan' in top3=['shankarjaikishan', 'kalyanjianandji', 'madan mohan']

### #236 — FAIL

- item: `{'lyrics': '  maalik main puuchhataa huun mujhe tuu javaab de bahate hain kyuun gariib ke aansuu javaab de  bataa mujhe o jahaan ke maalik ye kyaa nazaare dikhaa rahaa hai tere samundar men kyaa kamii thii ke aadamii ko rulaa rahaa hai bataa mujhe o threedots  kabhii hansaae kabhii rulaae ye khel kaisaa hai tuu bataa de jise banaayaa thaa apane haathon usii ko ab kyuun mitaa rahaa hai bataa mujhe o threedots  jo khud hii gam se bujhaabujhaa hai teraa phir isamen kamaal kyaa hai ki ek diipak kii raah men tuu hazaaron tuufaan uthaa rahaa hai bataa mujhe o threedots ', 'correct_label': 'madan mohan', 'label': 5, 'split': 'test', 'title': 'maalik main puuchhataa huun  bataa mujhe o jahaan ke maalik', 'year': '1958'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "s d burman", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='shankarjaikishan' ref='madan mohan'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='madan mohan' in top3=['shankarjaikishan', 's d burman', 'laxmikantpyarelal']

### #237 — PASS

- item: `{'lyrics': '  tuu hii to mere paas hai phir ye kaisii pyaas hai ye kaisaa ehasaas hai koii bataa de mujhe  aaj main huun aur tum ho aur mohabbat hai huun huun huun huun huun aur mohabbbat hai 2 huun main bhii gum huun tum bhii gum ho haan ye chaahat hai huun huun huun huun huun haan ye chaahat hai aur mohabbat hai  ye kaise mumakin hai tumako kisii ne ab tak pyaar naa kiyaa ho ye kaise mumakin hai tumako kisii ne ab tak pyaar naa kiyaa main kaise ye maanuun tumako kisii ne ab tak dil naa diyaa kaisii hai ye ulajhan dil ye lagaa sochane tez hain kyon dhadakanen koii bataa de mujhe aaj main huun aur tum ho aur mohabbat hai huun huun huun huun huun aur mohabbbat hai 2  jo tumase kahanaa thaa maine kahaa naa lab par baat hai rukii ko \tyeah yeah yeah yeah yeah yeah  ho jo tumase kahanaa thaa maine kahaa naa lab par baat hai rukii lagataa hai ye aksar mere liye hii shaayad tuu hai banii kaisaa aitabaar hai kaisaa intazaar hai kyon tumase itanaa pyaar hai koii bataa de mujhe aaj main huun aur tum ho aur mohabbat hai huun huun huun huun huun aur mohabbbat hai 2 main bhii gum huun tum bhii gum ho haan ye chaahat hai huun huun huun huun huun haan ye chaahat hai aur mohabbat hai ko \tlaa raa raa laa o ', 'correct_label': 'annu malik', 'label': 1, 'split': 'test', 'title': 'tuu hii to mere paas hai  ye chaahat hai aur mohabbbat hai', 'year': '2003'}`
- output: `{"pred": "annu malik", "top3": ["annu malik", "kalyanjianandji", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='annu malik' ref='annu malik'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='annu malik' in top3=['annu malik', 'kalyanjianandji', 'shankarjaikishan']

### #238 — FAIL

- item: `{'lyrics': ' l ye kalii jab talak phuul ban ke khile  intazaar intazaar intazaar karo intazaar karo  rafii intazaar vo bhalaa kyaa kare tum jise  bekaraar bekaraar bekaraar karo  l intazaar karo   m pyaar men pyaar kii bhii izaazat nahiin 2  berukhii hai ajii ye muhaubbat nahiin  l aa rahaa hai mazaa tum shikaayat yahii  baar baar baar baar baar baar karo intazaar karo   l husn pe to asar hone vaalaa nahiin 2  ishq tum ko na kar de divaanaa kahiin  m hai ye diivaanagii bhii qubuul tum agar  hamase pyaar hamase pyaar hamase pyaar karo  l intazaar karo   m roz hamane bayaan ye fasaanaa kiyaa 2  roz tumane nayaa ek bahaanaa kiyaa  l ye bahaanaa magar aakhirii hai sanam  aitabaar aitabaar aitabaar karo intazaar karo ', 'correct_label': 'laxmikantpyarelal', 'label': 4, 'split': 'test', 'title': 'ye kalii jab talak phuul ban ke khile', 'year': '1966'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "r d burman", "annu malik"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='shankarjaikishan' ref='laxmikantpyarelal'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='laxmikantpyarelal' in top3=['shankarjaikishan', 'r d burman', 'annu malik']

### #239 — FAIL

- item: `{'lyrics': '  aap ke anurodh par main ye giit sunaataa huun apane dil kii baaton se aap kaa dil bahalaataa huun aap ke anurodh pe   threedots  mat puuchho auron ke duhkh men ye prem kavi kyon rotaa hai bas chot kisii ko lagatii hai aur dard kisii ko hotaa hai duur kahiin koi darpan tuute tadap ke main rah jaataa huun aap ke anurodh pe   threedots  taariif main jisakii karataa huun kyaa ruup hai vo kyaa khushabuu hai kuchh baat nahiin aisii koii ye ek suron kaa jaaduu hai koal kii ek kuuk se sabake dil men huuq uthaataa huun aap ke anurodh pe   threedots  main pahane phirataa huun jo vo zanjiiren kaise banatii hain ye bhed bataa duun giiton men tasaviiren kaise banatii hain sundar honthon kii laalii se main rang ruup churaataa huun aap ke anurodh pe main ye giit sunaataa huun   threedots ', 'correct_label': 'laxmikantpyarelal', 'label': 4, 'split': 'test', 'title': 'aap ke anurodh pe main ye giit sunaataa huun', 'year': '-1'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "kalyanjianandji", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='shankarjaikishan' ref='laxmikantpyarelal'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='laxmikantpyarelal' in top3=['shankarjaikishan', 'kalyanjianandji', 'laxmikantpyarelal']

### #240 — FAIL

- item: `{'lyrics': '  ki \tgore rang pe naa itanaa gumaan kar 2 \tgoraa rang do din men dhal jaaegaa la \tmain shamaa huun tuu hai paravaanaa 2 \tmujhase pahale tuu jal jaaegaa ki \tgore rang pe threedots  ki \truup mit jaataa hai ye pyaar ai diladaar nahiin mitataa la \tho ho phuul murajhaane se gulazaar o sarakaar nahiin mitataa ki \tkyaa baat kahii hai hoy taubaa 2 \tye dil beiimaan machal jaaegaa \tgore rang pe threedots  ki \to o aapako hai aisaa inkaar to ye pyaar yahiin chhodo la \to o pyaar kaa mausam hai bekaar kii takaraar yahiin chhodo ki \thaathon men haath zaraa dedo 2 \tbaaton men vaqt nikal jaaegaa \tgore rang pe threedots  la \to o main tujhe kar daaluun masaruur nashe men chuur to maanoge ki \to o tumase main ho jaauun kuchh duur e magaruur ho maanoge la \ttuu laakh bachaa mujhase daaman 2 \tye husn kaa jaaduu chal jaaegaa ki \tgore rang pe threedots ', 'correct_label': 'laxmikantpyarelal', 'label': 4, 'split': 'test', 'title': 'gore rang pe naa itanaa gumaan kar', 'year': '1974'}`
- output: `{"pred": "kalyanjianandji", "top3": ["kalyanjianandji", "r d burman", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='kalyanjianandji' ref='laxmikantpyarelal'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='laxmikantpyarelal' in top3=['kalyanjianandji', 'r d burman', 'shankarjaikishan']

### #241 — FAIL

- item: `{'lyrics': '  are bhaii nikal ke aa ghar se 2 e e e  are bhaii nikal ke aa ghar se aa ghar se 2 duniyaa kii raunak dekh phir se dekh le phir se 2 hoy are bhaii nikal ke aa ghar se aa ghar se  kem uungheche bhaii ghanashyaam jii o 2 o duniyaa badal gayii pyaare aage nikal gayii pyaare 2 andhe kune men ghus ke kyon baithaa huaa hai man maare 2 are bhaii nikal ke aa ghar se threedots  tulaa bhiitii hii kasalii vaat te re 2 o paanii ko tel ko chhodaa bijalii kii rel ko chhodaa 2 kal chaand aur taaron men pahunchegaa aitamii ghodaa are bhaii are bhaii are bhaii nikal ke aa ghar se threedots  kaino bhaaben okaaran ai bankii baabuu re 2 o kal jo thaa kal rahaa hogaa aage kii soch kyaa hogaa 2 tuutii puraanii dhaphalii pe tuu kal kamar diyaa malegaa 2 are bhaii nikal ke aa ghar se threedots ', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'are bhaii nikal ke aa ghar se', 'year': '1956'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "c ramchandra", "s d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='r d burman' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='shankarjaikishan' in top3=['r d burman', 'c ramchandra', 's d burman']

### #242 — FAIL

- item: `{'lyrics': '  mu \thonii to ho ke rahe anahonii naa hoy \tjaako raakhe saaiyaan maar sake naa koy la \thonii to ho ke rahe threedots  mu \tkans ne kitane jatan kie re bhaiyaa \tkans ne kitane jatan kie lekin tumane dekhaa la \tsau talavaaren mitaa sakiin naa bhaagy kii ek bhii rekhaa ko \tsau talavaaren threedots mu \tkishan kaa aisaa janm huaa la \tatyaachaar yuun katm huaa mu \tbandiighar ke dvaar khule aur paharedaar soe do \tjaako raakhe saaiyaan threedots ko \tjaako raakhe saaiyaan threedots  la \tchhuut gaii jinase re bhaiyaa \tchhuut gaii jinase apane bachapan kii sundar galiyaan mu \tbagiyaa ke badale ban men dekhiin khilatii vo kaliyaan ko \tbagiyaa ke badale threedots la \tkhel hai jogsanjog kaa mu \tsach kahanaa hai logon kaa la \triit atal ye jiivan kii koii hanse yaa roe do \tjaako raakhe saaiyaan threedots ko \tjaako raakhe saaiyaan threedots  mu \thaath samay kaa is duniyaa men koii rok na paayaa la \tdhokhaa dene vaale ne ek din kud dhokhaa khaayaa ko \tdhokhaa dene vaale threedots mu \taaj mile yaa chaahe kal la \tmilataa hai karmon kaa phal mu \tphuul vo kaise paaegaa jisane hon kaante boe ko \tjaako raakhe saaiyaan threedots ', 'correct_label': 'laxmikantpyarelal', 'label': 4, 'split': 'test', 'title': 'honii to ho ke rahe  jaako raakhe saaiyaan', 'year': '1973'}`
- output: `{"pred": "kalyanjianandji", "top3": ["kalyanjianandji", "laxmikantpyarelal", "r d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='kalyanjianandji' ref='laxmikantpyarelal'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='laxmikantpyarelal' in top3=['kalyanjianandji', 'laxmikantpyarelal', 'r d burman']

### #243 — FAIL

- item: `{'lyrics': ' terii shaadii pe duun tujhako tohafaa main kyaa pesh karataa huun dil ek tuutaa huaa  khush rahe tuu sadaa ye duaa hai merii bevafaa hii sahii dilarubaa hai merii khush rahe threedots  jaa main tanahaa rahuun tujhako mahafil mile duubane de mujhe tujhako saahil mile aaj marazii yahii naakudaa hai merii  umr bhar ye mere dil ko tadapaaegaa dardedil ab mere saath hii jaaega maut hii aakirii bas davaa hai merii', 'correct_label': 'laxmikantpyarelal', 'label': 4, 'split': 'test', 'title': 'khush rahe tuu sadaa ye duaa hai merii', 'year': '1970'}`
- output: `{"pred": "madan mohan", "top3": ["madan mohan", "kalyanjianandji", "r d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='madan mohan' ref='laxmikantpyarelal'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='laxmikantpyarelal' in top3=['madan mohan', 'kalyanjianandji', 'r d burman']

### #244 — FAIL

- item: `{'lyrics': ' ai ishq ye sab duniyaa vaale bekaar kii baaten karate hain paayal ke gamon kaa ilm nahiin jhankaar kii baaten karate hain  har dil men chhupaa hai piir koii har paanv men hai zanjiir koii puuchhe koii un se gam ke maze jo pyaar kii baaten karate hain  ulfat ke naye diivaanon ko kis tarah se koii samajhaaye nazaron pe lagii hai paabandii diidaar kii baaten karate hain  bhanvare hain agar madahosh to kyaa paravaane bhii hain khaamosh to kyaa sab pyaar ke nagamen gaate hain sab yaar kii baaten karate hain ', 'correct_label': 'naushad', 'label': 6, 'split': 'test', 'title': 'ai ishq ye sab duniyaa vaale', 'year': '1960'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "madan mohan", "a r rahman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='naushad'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='naushad' in top3=['laxmikantpyarelal', 'madan mohan', 'a r rahman']

### #245 — PASS

- item: `{'lyrics': ' aaine ke sau tukade karake hamane dekhe hain 2 ek men bhii tanhaa the  sau men bhii akele hain  2 aaine ke sau tukade threedots  jo banaa thaa ek saathii vo bhii hamase chhuutaa hai bevafaa nahiin jo vo  phir kyuun hamase ruuthaa hai  2 khoii khoii aankhon men aansuon ke mele hain ek men bhii tanhaa the threedots  usakaa kyaa haal hogaa yahii gam sataataa hai  dard badhataa jaataa hai  2 zindagii kii raahon men log hamase khele hain ek men bhii tanhaa the threedots  har taraf ujaalaa hai dil men ek andheraa hai saamane vo kab aaegaa  jo chhupaa saveraa hai  2 meraa dil jigar dekho kitane dard jhele hain ek men bhii tanhaa the threedots ', 'correct_label': 'annu malik', 'label': 1, 'split': 'test', 'title': 'aaine ke sau tukade karake hamane dekhe hain', 'year': '1991'}`
- output: `{"pred": "annu malik", "top3": ["annu malik", "madan mohan", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='annu malik' ref='annu malik'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='annu malik' in top3=['annu malik', 'madan mohan', 'laxmikantpyarelal']

### #246 — PASS

- item: `{'lyrics': ' ki mainne dekhaa tujhe tuune dekhaa mujhe  2     aankhon aankhon men donon ke dil mil gae  aa dil se dil jo mile chal paden silasile  2     sharm aur shokhiyon ke kamal khil gae  ki mainne dekhaa tujhe       phuul milane lage chupake shaakon tale  2     mainne suuraj kii jalatii kiran chuum lii     saare gulashan men charche chhide pyaar ke  2     prem ke dhaage men do jism sil gae  aa mainne dekha tujhe        parbaton pe baraf kaa pighalataa badan  2     dharatii aur ye gagan kaa tadapataa milan     ye hawaaon kii galiyaan jame raaste  2     saans banake hii saanson men ghul mil gae  ki mainne dekhaa tujhe       priit ke gaanv men dhuup men chhaanv men     baandhakar manzilon ko chalen paanv men  aa raat ke munh pe hamane saveraa kiyaa     baat kuchh naa kahii phir bhii lab hil gae  do mainne dekhaa tujhe ', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'mainne dekhaa tujhe tuune dekhaa mujhe', 'year': '1977'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "kalyanjianandji", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='r d burman' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='r d burman' in top3=['r d burman', 'kalyanjianandji', 'shankarjaikishan']

### #247 — PASS

- item: `{'lyrics': ' qasam khaao tum ik baar mere yaar mere diladaar chale to naa jaaoge tum baabuu kahiin leke meraa pyaar he he he he he he he he qasam khaataa hai meraa pyaar mere yaar mere diladaar aayegaa diiwaanaa leke dolii sanam kabhii tere dwaar haa haa aa aa aa aa aa aa  qasam khaao tum ik baar  paagal kaho mujhe yaa diiwaanii kaho la la la ab to terii huii balam jo ho so ho la la la merii balaa se koii rahe yaa naa rahe la la la agar merii nazar men tuu sajii rahe aa la la la laa he he he he he he he he basaa kar lenaa sarakaar mere yaar mere diladaar chale to naa jaaoge tum baabuu kahiin leke meraa pyaar he he he he he he he he  qasam khaataa hai meraa pyaar  tuune to ye samaan chhodaa mere liye la la la mainne saaraa jahaan chhodaa tere liye la la la chhotii se main badii jis aangan men huii la la la naataa us aangan se todaa tere liye la la la laa he he he he he he he he jiivaa kar duniyaa is baar mere yaar mere diladaar aayegaa diiwaanaa leke dolii sanam kabhii tere dwaar haa haa he he he he he he  qasam khaao tum ik baar  rang se tere chunarii merii rangii rahe la la la maathe mere bindiyaa terii lagii rahe la la la chandaa suuraj ko to mudake naa dekhuun main la la la agar merii baanhon men tuu sajii rahe ho la la la laa he he he he he he he he sajaa kar lenaa sarakaar mere yaar mere diladaar chale to naa jaaoge tum baabuu kahiin leke meraa pyaar haa haa aa aa haa haa aa aa ', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'qasam khaao tum ik baar', 'year': '1974'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "kalyanjianandji", "c ramchandra"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='r d burman' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='r d burman' in top3=['r d burman', 'kalyanjianandji', 'c ramchandra']

### #248 — FAIL

- item: `{'lyrics': ' o gangaa maiyaa  2 paar lagaa de mere sapanon kii naiyaa  2 o gangaa maiyaa threedots  guzare idhar se bhii kaalii ghataayen  2 maan terii mamataa ko degii duaayen  2 dukhiyaa ke aangan kii tuu thii kalaiyaa o gangaa maiyaa threedots  jisaliye nainaa taras rahe hain saawan bhaado se baras rahe hain  2 sandes laike wo aaye purawaiyaa o gangaa maiyaa threedots  suunaa padaa hai chandan kaa palanaa  2 palane men jhuule ek chandaa saa lalanaa  2 jaise yashodaa kaa krrishna kanhaiyaa o gangaa maiyaa threedots ', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'o gangaa maiyaa paar lagaa de mere sapanon kii naiyaa', 'year': '1967'}`
- output: `{"pred": "kalyanjianandji", "top3": ["kalyanjianandji", "laxmikantpyarelal", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='kalyanjianandji' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='r d burman' in top3=['kalyanjianandji', 'laxmikantpyarelal', 'shankarjaikishan']

### #249 — PASS

- item: `{'lyrics': '  nazar bachaa kar chale gaye vo varanaa ghaayal kar detaa dil se dil takaraa jaataa to dil men agni bhar detaa varanaa ghaayal kar detaa nazar bachaa kar threedots   milatii aankh to vo bhii dekhate mere pyaar kaa jaaduu apane rang men ham bhii kam na the kar dete beqaabuu  2 nazar bachaa kar threedots   agar thaharate mere saamane dil pe tiir chal jaate vo hasiin hain main javaan huun saare bhed khul jaate  2 nazar bachaa kar threedots   hamase kab tak yuun chhupenge vo apanii shaan dikhalaa ke ek roz to aa hii jaaenge vo mere paas sharamaa ke  2 nazar bachaa kar threedots ', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'nazar bachaa kar chale gaye vo varanaa ghaayal kar detaa', 'year': '1962'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "naushad", "madan mohan"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='shankarjaikishan' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='shankarjaikishan' in top3=['shankarjaikishan', 'naushad', 'madan mohan']

### #250 — FAIL

- item: `{'lyrics': ' sun le o jaanam main huun paramashivam  tuu hai paarvatii milanaa janamjanam  sun le miinaakshii tuu hii meraa dil  luut ke yuun mujhako chup kyuun hai qaatil   pyaar kaa desh bhalaa puunam kii raat bhalii  tum sang mere piyaa pyaar kii do baat bhalii  man kaa miit bhalaa ghar sansaar bhalaa  kahataa dil meraa tum saa yaar bhalaa   sun le o jaanam tum se pyaar huaa  jab se pyaar huaa jiinaa dushvaar huaa   koyal sii bolii hai baadal sii zulfen hain  mujh ko jaan se bhii merii mainaa pyaarii hai tuu  jabjab dekhuun tujhe naache man meraa  pyaar kii rut aaii jhuume tan meraa ', 'correct_label': 'a r rahman', 'label': 0, 'split': 'test', 'title': 'sun le o jaanam main huun paramashivam', 'year': '1995'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "naushad", "a r rahman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='shankarjaikishan' ref='a r rahman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='a r rahman' in top3=['shankarjaikishan', 'naushad', 'a r rahman']

### #251 — FAIL

- item: `{'lyrics': ' ishq meraa bandagii hai  ishq merii zindagii hai aashiqon kaa arsh deraa aashiqon kaa farsh deraa aashiqon ke saaton jahaan 2  ishq meraa bandagii hai  yuun to jahaan men sabhii naam ke hain ye rishte jo pyaar men duub jaaen wahii hain farishte  2 ishq men hai wo kumaarii jo na utare umr saarii dinbadin ye hotii jawaan ishq meraa bandagii hai  ishq merii zindagii hai  dil jis men shammaa jale ishq kii dil wahii hai mainne to apane hii dil kii kahaanii kahii hai  2 dharm apanaa aashiqii hai karm apanaa aashiqii hai ishq hii hai meraa iimaan ishq meraa bandagii hai  ishq merii zindagii hai  laa laa la la laa laa laa laa laa laa la la laa laa laa laa  aashiq wahii hai jo duuje kaa gam jaane sahanaa tuu is jahaan men kabhii na kisii se ye kahanaa 2 ishq hai kyaa tuu kyaa jaane na sunaa tuu ye fasaane kyon kare ye jhuuthaa gumaan ishq meraa bandagii hai  ishq merii zindagii hai aashiqon kaa arsh deraa aashiqon kaa farsh deraa aashiqon ke saaton jahaan ishq meraa bandagii hai  ishq merii zindagii hai ', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'ishq meraa bandagii hai', 'year': '1981'}`
- output: `{"pred": "annu malik", "top3": ["annu malik", "naushad", "c ramchandra"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='annu malik' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='r d burman' in top3=['annu malik', 'naushad', 'c ramchandra']

### #252 — FAIL

- item: `{'lyrics': ' ham aah bhii bharate hain to ho jaate hain badnaam vo qatl bhii karate hain to chachraa nahiin hotaa  aa a matalab kii ye duniyaa hai yahaan kaun kisii kaa hotaa hai dhokhaa de dete hain vahii jin par ke bharosaa hotaa hai  baag men sair ko aaye the ek daag jigar men leke chale rangiiniyon men bhuul gaye har phuul men kaantaa hotaa hai matalab kii ye duniyaa hai   threedots  behoshiyon men dil kho baithe jab hosh aayaa to ye samajhe aa aa a behoshiyon men dil kho baithe jab hosh aayaa to ye samajhe sab jisako muhabbat kahate hain darasal vo dhokhaa hotaa hai  khuunejigar se baag ko siinchaa phuul khile to aag lagii jal hii gayii ab saarii duniyaa rone se ab kyaa hotaa hai matalab kii ye duniyaa hai   threedots  matalab kii ye duniyaa hai yahaan kaun kisii kaa hotaa hai dhokhaa de dete hain vahii jin par ke bharosaa hotaa hai', 'correct_label': 'c ramchandra', 'label': 2, 'split': 'test', 'title': 'matalab kii ye duniyaa hai', 'year': '1957'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "s d burman", "madan mohan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='shankarjaikishan' ref='c ramchandra'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='c ramchandra' in top3=['shankarjaikishan', 's d burman', 'madan mohan']

### #253 — FAIL

- item: `{'lyrics': '  raat suhaanii jaag rahii hai dhiiredhiire chupakechupake choriichorii ho prem kahaanii jaag rahii hai dhiiredhiire threedots  chal rahe hain jaaduu tham gayaa zamaanaa dil churaa rahaa hai ye samaan suhaanaa paalakii chaman men phuulon kii utaar ke ye bahaar gaa rahii hai giit pyaar ke o aur javaanii jaag rahii hai dhiiredhiire threedots  chaand kar rahaa hai pyaar ke ishaare ye hamaare nayanaa ban gae hain taare niind ne na aane kii uthaaii hai qasam o niind kaise aae man ke dvaar pe sanam o priit diivaanii jaag rahii hai dhiiredhiire threedots  ek pahelii tum mujhase puuchho aa gae kahaan ham ye kisii se puuchho ye zamiin lag rahii hai aasamaan sii dil kii dhadakanon men pad gaii hai taan sii o zindagaanii jaag rahii hai dhiiredhiire threedots ', 'correct_label': 'laxmikantpyarelal', 'label': 4, 'split': 'test', 'title': 'raat suhaanii jaag rahii hai dhiiredhiire chupakechupake', 'year': '1969'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "laxmikantpyarelal", "c ramchandra"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='shankarjaikishan' ref='laxmikantpyarelal'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='laxmikantpyarelal' in top3=['shankarjaikishan', 'laxmikantpyarelal', 'c ramchandra']

### #254 — FAIL

- item: `{'lyrics': '     chi \t shin shinaa kii la \tbuubalaa buu  3 do \tdo hain jism ek hai ruuh \tbuubalaa buu 3  la \tshin ye puuchhe buubalaa \tye to bataa buubalaa \tishq hai kyaa buubalaa \tbuubalaa ai buubalaa chi \tmain bataauun kyaa bhalaa \tphir bhii ye huun jaanataa \tishq kud ko dhuundhane kii justajuu hai justajuu do \tdo hain jism ek hai ruuh \tbuubalaa buu 3 \tshin shinaa kii buubalaa buu 3 \tdo hain jism ek hai ruuh \tbuubalaa buu 3  la \tmain jo puuchhuun main huun kyaa chi \tmain jo kah duun kuchh nahiin la \tmain ye puuchhuun tuu huun kyaa chi \tmain jo kah duun kuchh nahiin do \tdonon kuchh nahiin magar \ttuu hai main aur main huun tuu \tdo hain jism ek hai ruuh \tbuubalaa buu 3 \tshin shinaa kii buubalaa buu 3 \tdo hain jism ek hai ruuh \tbuubalaa buu 4 ', 'correct_label': 'c ramchandra', 'label': 2, 'split': 'test', 'title': 'shin shinaa kii buubalaa buu', 'year': '1952'}`
- output: `{"pred": "a r rahman", "top3": ["a r rahman", "madan mohan", "kalyanjianandji"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='a r rahman' ref='c ramchandra'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='c ramchandra' in top3=['a r rahman', 'madan mohan', 'kalyanjianandji']

### #255 — PASS

- item: `{'lyrics': ' ruuth na jaanaa tum se kahuun to  main in aankhon men jo rahuun to  tum ye jaano yaa naa jaano  2 mere jaisa divaanaa tum paaoge nahiin  yaad karoge main jo na huun to ruuth threedots  1 merii ye divaanagii kabhii na hogii kam  jitane bhii chaahe tum kar lo sitam  mujhase bolo yaa naa bolo  mujhako dekho yaa naa dekho  ye bhii maanaa mujhase milane aaoge nahiin  saare sitam hansake main sahuun to ruuth threedots  2 prem ke dariyaa men laharen hazaar  laharon men jo bhii dubaa huaa vahii paar  uunchii niichii niichii uunchii niichii uunchii uunchii niichii laharon men tum dekhuun kaise aaoge nahiin  main in laharon men jo bahuun to ruuth threedots', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'ruuth na jaanaa tum se kahuun to', 'year': '1994'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "annu malik", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='r d burman' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='r d burman' in top3=['r d burman', 'annu malik', 'shankarjaikishan']

### #256 — FAIL

- item: `{'lyrics': ' dil ke jharokhe men tujhako bithaakar yaadon ko terii main dulhan banaakar rakhuungaa main dil ke paas  mat ho merii jaan udaas  kal tere jalave paraaye bhii honge lekin jhalak mere khvaabon men honge phulon kii dolii men hogii tu rukhasat lekin mahak merii saanson men hogii dil ke jharokhe men threedots  ab bhii tere surkh hothon ke pyaale   mere tasavvur men saaqii bane hain ab bhii terii zulf ke mast saaye birahaa kii dhuup men saathii bane hain dil ke jharokhe men threedots  merii muhabbat ko thukaraa de chaahe main koi tujhase naa shikavaa karungaa aankhon men rahatii hain tasviir terii   saarii umar terii puujaa karungaa dil ke jharokhe men threedots', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'dil ke jharokhe men tujhako bithaakar', 'year': '1968'}`
- output: `{"pred": "madan mohan", "top3": ["madan mohan", "shankarjaikishan", "c ramchandra"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='madan mohan' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='shankarjaikishan' in top3=['madan mohan', 'shankarjaikishan', 'c ramchandra']

### #257 — FAIL

- item: `{'lyrics': '  terii nagariyaa na bhaaii priit kie pachhataaii re saanvariyaa priit kie pachhataaii  baandh paayaliyaa priit kii saanchii re kaanton ke biich men hanshans naachii re tohe dayaa nahiin aaii priit kie pachhataaii threedots  tere mahal kii dekh diivaalii maine apanii duniyaa jalaa lii priit kii holii manaaii priit kie pachhataaii threedots  main huun bhagavaan chhod chalii re apane saajan kii priit galii re jaane kab raam milaaii priit kie pachhataaii threedots ', 'correct_label': 'c ramchandra', 'label': 2, 'split': 'test', 'title': 'terii nagariyaa na bhaaii priit kie pachhataaii re', 'year': '1949'}`
- output: `{"pred": "s d burman", "top3": ["s d burman", "madan mohan", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='s d burman' ref='c ramchandra'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='c ramchandra' in top3=['s d burman', 'madan mohan', 'shankarjaikishan']

### #258 — FAIL

- item: `{'lyrics': ' diye jalate hain phul khilate hain badii mushkil se magar duniyaa men log milate hain  jab jis vaqt kisiikaa yaar judaa hotaa hain kuchh naa puchho yaaron dil kaa haal buraa hotaa hai dil pe yaadon ke jaise tiir chalate hain diye threedots  daulat aur javaanii ek din kho jaatii hai sach kahataa huun saarii duniyaa  dushman ban jaatii hai umr bhar dost lekin saath chalate hain diye threedots  is rangdhuup pe dekho haragij naaz naa karanaa jaan bhii maange yaar to de denaa naaraaz naa karanaa rang ud jaate hain dhuup dhalate hain diye threedots', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'diye jalate hain phuul khilate hain badii mushkil se magar', 'year': '1973'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "r d burman", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='r d burman' in top3=['laxmikantpyarelal', 'r d burman', 'shankarjaikishan']

### #259 — PASS

- item: `{'lyrics': ' afasaana likh rahii huun 2 dilebeqaraar kaa  aankhon men rang bhar ke tere intazaar kaa afasaanaa likh rahii huun   jab tuu nahiin to kuchh bhii nahiin hai bahaar men nahiin hai bahaar men jii chaahataa hai muunh bhii jii chaahataa hai muunh bhii na dekhuun bahaar kaa aankhon men rang bhar ke tere intazaar kaa afasaanaa likh rahii huun   haasil hain yuun to mujhako zamaane kii daulaten zamaane kii daulaten lekin nasiib laaii  lekin nasiib laaii huun ik sogavaar kaa aankhon men rang bhar ke tere intazaar kaa afasaanaa likh rahii huun   aajaa ki ab to aankh men aansuu bhii aa gaye aansuu bhii aa gaye saagar chhalak uthaa  saagar chhalak uthaa mere sabroqaraar kaa aankhon men rang bhar ke tere intazaar kaa afasaanaa likh rahii huun  ', 'correct_label': 'naushad', 'label': 6, 'split': 'test', 'title': 'afasaana likh rahii huun', 'year': '1947'}`
- output: `{"pred": "naushad", "top3": ["naushad", "laxmikantpyarelal", "c ramchandra"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='naushad' ref='naushad'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='naushad' in top3=['naushad', 'laxmikantpyarelal', 'c ramchandra']

### #260 — FAIL

- item: `{'lyrics': '  raam kare babuaa ho raam kare babuaa hamaar phulavaa ko hamarii umar lagi jaaye ho patajhar aaye basant rut jaaye ho jaaye champaa chamelii muskaaye raam kare babuaa ho  pyaare munne tuu bhii ik dilkhus gulaab hai toharii khusabuu kaa kahiin koii javaab hai tohe na kisii kii najar lagi jaaye raam kare babuaa ho threedots  bol siyaabar ramachandra ki jay pavan put hanumaan kii jay  raam jii ne duniyaa men duhkh sukh baante phulavaa ke sang sang bagiyaa men kaante tore pag men na koii kaantaa lagi jaaye raam kare babuaa threedots  kaas aisaa hovai jab banai tuu dulhaa raajaa galiyon men baaje jab saadii kaa baajaa yahii gangaa raam hau yahii gangaa raam toharaa seharaa banaavai raam kare babuaa threedots ', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'raam kare babuaa hamaar phulavaa ko', 'year': '-1'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "shankarjaikishan", "s d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='s d burman' in top3=['laxmikantpyarelal', 'shankarjaikishan', 's d burman']

### #261 — FAIL

- item: `{'lyrics': ' huzuur is kadar bhii na itaraa ke chaliye khule aam aanchal na laharaa ke chaliye 2  koi manachalaa gar pakad legaa aanchal zaraa sochiye aap kyaa kiijiyegaa lagaa den agar badhake zulfon men kaliyaan to kyaa apanii zulfen jhatak diijiyegaa huzuur is threedots  bahut dilanashiin hain hansii kii ye ladiyaan ye motii magar yuun naa bikharaayaa kiije udaakar na le jaaye jhonkaa havaa kaa lachakataa badan yuun naa laharaayaa kiije huzuur is threedots  bahut khuubasuurat hai har baat lekin agar dil bhii hotaa to kyaa baat hotii likhii jaatii phir daastaanemuhabbat ek afasaane jaise mulaaqaat hotii huzuur is threedots', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'huzuur is kadar bhii na itaraake chaliye', 'year': '1986'}`
- output: `{"pred": "s d burman", "top3": ["s d burman", "laxmikantpyarelal", "madan mohan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='s d burman' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='r d burman' in top3=['s d burman', 'laxmikantpyarelal', 'madan mohan']

### #262 — FAIL

- item: `{'lyrics': ' tuu kyaa bangalaa banaaegaa gaadii kyaa dilaaegaa sair kyaa karaaegaa jaane de jaane de jaane de zaraa parade pe aane de mujhe hiiro to ban jaane de phir dekh tamaashaa phir dekh tamaashaa  bade bol naa bol tuu lagataa hai zero kaun banaaegaa tujhako filmy hero are rang laaegii jis din ye kundalii merii us din pakad ke chal duungaa ungalii terii are dil ko churaane kaa teraa bahaanaa hai baaten badii naa banaa zaraa chakkar chal jaane de mujhe tv pe aane de phir dekh tamaashaa threedots  ik din meraa sach ho jaaegaa sapanaa haan mere tan pe hogii resham kii saadii apane niiche hogii phir motar gaadii are bangalaa bhii hogaa gaadii bhii hogii khulane de kismat zaraa zaraa photo chhap jaane de meraa dankaa baj jaane de phir dekh tamaashaa threedots ', 'correct_label': 'annu malik', 'label': 1, 'split': 'test', 'title': 'tuu kyaa bangalaa banaaegaa  phir dekh tamaashaa', 'year': '1997'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "s d burman", "annu malik"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='annu malik'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='annu malik' in top3=['laxmikantpyarelal', 's d burman', 'annu malik']

### #263 — PASS

- item: `{'lyrics': ' o maariyaa o maariyaa o maariyaa o ho o o maariyaa o maariyaa o maariyaa ho ho ho ho jaacnii jab bolaa thaa tujhase shaadii karegii mujhase kaise kahaa thaa ye bataa o maariyaa o maariyaa   threedots  kyaa bolii thii tuu jab vo paas aayaa thaa mammii se puuchhuungii kyaa aisaa bolii thii  sardii ke din the ya garmii kii raaten khoii thii jab tuu jaacnii kii baaton men thaamaa haath bhii thaa kyaa apane haathon men', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'o maariyaa o maariyaa', 'year': '-1'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "annu malik", "kalyanjianandji"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='r d burman' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='r d burman' in top3=['r d burman', 'annu malik', 'kalyanjianandji']

### #264 — PASS

- item: `{'lyrics': ' mere desh kii dharatii sonaa ugale ugale hiire motii mere desh kii dharatii threedots  bailon ke gale men jab ghungharuu jiivan kaa raag sunaate hain gam kos duur ho jaataa hai khushiyon ke kanval muskaate hain sunake rahat kii aavaazen yuun lage kahiin shahanaai baje aate hii mast bahaaron ke dulhan kii tarah har khet saje mere desh threedots  jab chalate hain is dharatii pe hal mamataa angadaaiyaan letii hai kyuun naa puuje is maatii ko jo jiivan kaa sukh detii hai is dharatii pe jisane janam liyaa usane hii paayaa pyaar teraa yahaan apanaa paraayaa koi nahiin hai sab pe hai maan upakaar teraa mere desh threedots  ye baag hai gautam naanak kaa khilate hain chaman ke phuul yahaan gaandhii subhaashh taigor tilak aise hain aman ke phuul yahaan rang haraa harii sinh nalave se rang laal hai laal bahaadur se rang banaa basantii bhagat sinh rang aman kaa viir javaahar se mere desh threedots', 'correct_label': 'kalyanjianandji', 'label': 3, 'split': 'test', 'title': 'mere desh kii dharatii sonaa ugale ugale hiire motii', 'year': '1967'}`
- output: `{"pred": "kalyanjianandji", "top3": ["kalyanjianandji", "laxmikantpyarelal", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='kalyanjianandji' ref='kalyanjianandji'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='kalyanjianandji' in top3=['kalyanjianandji', 'laxmikantpyarelal', 'shankarjaikishan']

### #265 — FAIL

- item: `{'lyrics': '  jawaab aataa hai jab dilbar kaa to dil kho hii jaataa hai mohabbat wo nashaa hai bepiiye jo ho hii jaataa hai  ye kaisii khushii hai ye kaisaa nashaa hai mujhe kyaa huaa hai mujhe kyaa huaa hai 2  kadam dolaten hain nazar jhuumatii hai 2 tasavur men jaise zamiin ghuumatii hai 2 khayaalon men koii chalaa aa rahaa hai mujhe kyaa huaa hai  threedots  aa aa aa aa  laa laa laa laa khabar dilarubaa tere aane kii aayii mohabbat kii duniya men chhalkii surahii 2 meraa dil hawaa men udaa jaa rahaa hai mujhe kyaa huaa hai  threedots ', 'correct_label': 'c ramchandra', 'label': 2, 'split': 'test', 'title': 'ye kaisii khushii hai ye kaisaa nashaa hai', 'year': '1953'}`
- output: `{"pred": "annu malik", "top3": ["annu malik", "shankarjaikishan", "madan mohan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='annu malik' ref='c ramchandra'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='c ramchandra' in top3=['annu malik', 'shankarjaikishan', 'madan mohan']

### #266 — FAIL

- item: `{'lyrics': ' guzare hain is tarah se duniyaa men din hamaare bhiige rahen hameshaa aankhon ke do kinaare  siine se ranjogam ko hamane lagaa ke rakhaa majabuuriyon ko dil hii dil men chhupaa ke rakhaa karate bhii kyaa ai qisamat tere sitam ke maare guzare hai is tarah se  hasarat bharii kahaanii kissaa hai bekasii kaa likhaa hai aansuuon se afasaanaa zindagii kaa kuchh naa kisii se kahanaa ai merii bezubaanii gardish nasiib kii hai kyaa dosh hai kisii kaa tuute chamakchamak kar taqadiir ke sitaare guzare hai is tarah se threedots', 'correct_label': 'madan mohan', 'label': 5, 'split': 'test', 'title': 'guzare hain is tarah se duniyaa men din hamaare', 'year': '1960'}`
- output: `{"pred": "c ramchandra", "top3": ["c ramchandra", "naushad", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='c ramchandra' ref='madan mohan'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='madan mohan' in top3=['c ramchandra', 'naushad', 'laxmikantpyarelal']

### #267 — PASS

- item: `{'lyrics': '  la \t koyal bolii duniyaa dolii  2 samajho dil kii bolii ra \tdil duniyaa men farq hai kitanaa tuu hai kitanii bholii ho ho la \tkoyal bolii threedots  ra \tis dil ke dhokhe men rah lo \tkuchh bhii sun lo kuchh bhii kah lo \trang binaa naa khelii jaae is jiivan kii holii la \tkoyal bolii threedots  \tuupar ambar niiche zamiin haii \titanaa badaa ghar koii nahiin hai \tphuul pavan baadal panchhii ye sab apane hamajolii o o\t la \tkoyal bolii threedots  \tdekho hans do dil na todo \tmain kush huun tum meraa saath na chhodo ra \tteraa saath main chhoduungaa par bhej ke terii dolii la \tkoyal bolii threedots ', 'correct_label': 'laxmikantpyarelal', 'label': 4, 'split': 'test', 'title': 'koyal bolii duniyaa dolii samajho dil kii bolii', 'year': '1979'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "naushad", "s d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='laxmikantpyarelal' ref='laxmikantpyarelal'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='laxmikantpyarelal' in top3=['laxmikantpyarelal', 'naushad', 's d burman']

### #268 — FAIL

- item: `{'lyrics': ' aa ham jis raste pe chale us raste pe thii priit khadii    priit ne hamako pahanaa dii armaanon kii hathakadii    tuu jahaan chale main vahaan chaluun    tuu jahaan ruke main vahaan rukuun la ham jis raste threedots  la ham anjaane ik duuje kii jaan bane     pahale do dil the ab sau armaan bane 2 aa are jaan ke dekho ham kaise anjaan bane    jaane kab dil takaraae jaane kab aankh se aankh ladii laaa priit ne hamako threedots  aa mausam hai yaa pyaar kaa ek paigaam hai     isiilie ye pyaar badaa badanaa hai 2 la bhuul gae ham duniyaa kisakaa naam hai    yaad rahenge hamen hameshaa ye din ye rut ye ghadii laaa priit ne hamako threedots  aa dekho abhii subah thii ho gaii shaam abhii la dil phir tadapaa aayaa thaa aaraam abhii aa are apane dil par likh do meraa naam abhii la o chhote se saajanaa tuu baaten karataa hai badii laaa priit ne hamako threedots', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'ham jis raste pe chale us raste pe thii priit khadii', 'year': '0'}`
- output: `{"pred": "c ramchandra", "top3": ["c ramchandra", "s d burman", "kalyanjianandji"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='c ramchandra' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='r d burman' in top3=['c ramchandra', 's d burman', 'kalyanjianandji']

### #269 — FAIL

- item: `{'lyrics': '  duniyaa kaa mazaa le lo  duniyaa tumhaarii hai  2 duniyaa tumhaarii hai ye  duniyaa tumhaarii hai  2  duniyaa ko laat maaro duniyaa salaam kare mud mud salaam kare jhuk jhuk salaam kare kabhii namaste kare to kabhii raam raam kare duniyaa se daroge to duniyaa dabaaegii rob jamaaegii hansii udaaegii chain na lene degii jaan jalaaegii taan ke siinaa chalo duniyaa kaa mazaa le lo threedots ', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'duniyaa kaa mazaa le lo duniyaa tumhaarii hai', 'year': '1951'}`
- output: `{"pred": "naushad", "top3": ["naushad", "c ramchandra", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='naushad' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='s d burman' in top3=['naushad', 'c ramchandra', 'shankarjaikishan']

### #270 — PASS

- item: `{'lyrics': '  yahii hai tamannaa tere dar ke saamane merii jaan jaae merii jaan jaae haay yahii hai tamannaa threedots  tere dar pe aayaa to bas aa gayaa main na piichhe hatuungaa zamaane ke dar se zaraa dekh luun main ye ruk kii bahaaren ye qad pyaaraapyaaraa ye zulfon ke saae haay yahii hai tamannaa threedots  gilaa hai mujhako tere kudaa se hasiin jisane itanaa banaayaa hai tujhako na aataa kabhii terii galiyon men zaalim tere husn ne khud bulaayaa hai mujhako jalaakar koii shammaa kaise kahegaa ke dekho yahaan par naa paravaanaa aae haay yahii hai tamannaa threedots  muhabbat men terii agar maut aae to vo maut kitanii hasiin maut hogii kisii roz main teraa daaman pakadakar jo mar jaauun kyaa dilanashiin maut hogii kabhii aisii koii ghadii aa rahii ho to merii duaa hai vo jaldii se aae haay yahii hai tamannaa threedots ', 'correct_label': 'madan mohan', 'label': 5, 'split': 'test', 'title': 'yahii hai tamannaa tere dar ke saamane', 'year': '1964'}`
- output: `{"pred": "madan mohan", "top3": ["madan mohan", "annu malik", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='madan mohan' ref='madan mohan'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='madan mohan' in top3=['madan mohan', 'annu malik', 'laxmikantpyarelal']

### #271 — FAIL

- item: `{'lyrics': '  ki \thamaare sivaa tumhaare aur kitane diivaane hain la \tqasam se kisii ko nahiin main jaanatii ki \tachchhaa la \taur kisii ko nahiin pahachaanatii ki \tchhodochhodo ye to bahaane hain \thamaare sivaa tumhaare threedots  \tkuubasuuratii aur vafaa \tdekhiin na donon ek jagah haan dekhiin na donon ek jagah la \thote hain mard bade shaqqii \tbaat hai ye bilkul pakkii ki \tbholii sii aatii ho nazar haan haan bholii sii aatii ho nazar \tho chanchal chaalaak magar la \taurat kaa dil jaane nahiin \taap hamen pahachaane nahiin ki \tchhodochhodo ham bhii sayaane hain \thamaare sivaa tumhaare threedots  \ttum ho pareshaan kis gam se \traazedil kah do ham se haan raazedil kah do ham se la \tapanii kaho chhodo merii \tkarate ho kyon heraapherii ki \tyaaron pe tohamat lagaate nahiin \tsabako nishaanaa banaate nahiin la \tkud harajaaii bhaunre ho tum \tek jagah kab thahare ho tum ki \tchhodochhodo ham to paravaane hain \thamaare sivaa tumhaare threedots ', 'correct_label': 'kalyanjianandji', 'label': 3, 'split': 'test', 'title': 'hamaare sivaa tumhaare aur kitane diivaane hain', 'year': '1972'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "r d burman", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='kalyanjianandji'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='kalyanjianandji' in top3=['laxmikantpyarelal', 'r d burman', 'shankarjaikishan']

### #272 — PASS

- item: `{'lyrics': '  meraa dil ab teraa o saajanaa kaisaa jaadu pheraa o saajanaa  2 meraa dil threedots  nain hamaare tum sang laage tum sang priit hamaarii man bhaaye tum jaano na jaano jaane hai duniyaa saarii koii aur na meraa o saajanaa meraa dil threedots  moranii ban ke raah takuun main tum baadal ban jaao mere pyaase rom rom pe ras barasaate jaao teraa dil men baseraa o saajanaa meraa dil threedots  pyaar kaa bandhan janam janam kaa saans ke sang hii tuute saare hii rang phiike pad jaae pyaar kaa rang na chhute tuune tan man gheraa o saajanaa meraa dil threedots ', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'meraa dil ab teraa o saajanaa', 'year': '1959'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "naushad", "kalyanjianandji"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='shankarjaikishan' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='shankarjaikishan' in top3=['shankarjaikishan', 'naushad', 'kalyanjianandji']

### #273 — FAIL

- item: `{'lyrics': '  aa \tvaqt thodaa saa abhii kuchh aur guzar jaane de \tdil men uthataa huaa tuufaan thahar jaane de ki \taur thodii der dekh lene de ye cheharaa \tzindagii bhar kii hasarat dil se nikal jaane de aa \tvaqt thodaa saa threedots  ki \tterii maasuum javaanii kaa hai ehasaas mujhe \tphir bhii baithaa le ghadii bhar ke lie paas mujhe \to raanii aa \ttan kii duurii na rahe man kaa milan ho sachchaa \tpyaar kii aag men tanman bikhar jaane de \tvaqt thodaa saa threedots  \tterii baanhon kaa kanval chuum luun to chain mile raajaa \tterii baanhon men zaraa jhuum luun to chain mile raajaa ki \tchand ghadiyaan mil gaiin jo zindagii se hamako \tapanii baanhon kii panaahon men guzar jaane de do \tvaqt thodaa saa threedots ', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'vaqt thodaa saa abhii kuchh aur guzar jaane de', 'year': '1971'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "madan mohan", "r d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='shankarjaikishan' in top3=['laxmikantpyarelal', 'madan mohan', 'r d burman']

### #274 — FAIL

- item: `{'lyrics': '  na hanso ham pe zamaane ke hain thukaraae hue darbadar phirate hain taqadiir ke bahakaae hue na hanso ham pe threedots  kyaa bataaen tumhen kal ham bhii chaman vaale the ye na puuchho ki hai viiraane men kyon aae hue na hanso ham pe threedots  baat kal kii hai ki phuulon komasal dete the aaj kaanton ko bhii siine se hain lipataae hue na hanso ham pe threedots  aisii gardish men na daale kabhii qismat tum ko aap ke saamane jis haal men hain aae hue na hanso ham pe threedots  ek din phir vahii pahalii sii bahaaren hongii is ummiid pe ham dil ko hain bahalaae hue na hanso ham pe threedots ', 'correct_label': 'madan mohan', 'label': 5, 'split': 'test', 'title': 'na hanso ham pe zamaane ke hain thukaraae hue', 'year': '-1'}`
- output: `{"pred": "c ramchandra", "top3": ["c ramchandra", "naushad", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='c ramchandra' ref='madan mohan'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='madan mohan' in top3=['c ramchandra', 'naushad', 'shankarjaikishan']

### #275 — FAIL

- item: `{'lyrics': '  ra \tpiyaa bin naahiin aavat chain \tmil gae milane vaale ho mil gae milane vaale \tab ghar men baithe kaajii \tkah do jii kah do miyaanbiivii raajii  su \tho ham tumhaare e e tum hamaare \tek jagah aae do sitaare \thamane kisii kaa kyaa liyaa hai bolo \tdil deke jiite hain jii dil kii ye baazii \tmil gae milane vaale threedots  ra \tho dil chaahe e e jise chaahe e e \tjahaan pyaar to nibhaae \tsoch samajh ke baat badhaaii hamane \tphir is duniyaa ko kaahe kii hai naaraazii do \tare mil gae milane vaale threedots  su \tho na kazaanaa a a na ghabaraanaa a a \tpyaare badal chukaa hai zamaanaa \tdil se dil kaa saath hai ye to ra \ttum jisamen raajii ham bhii raajiiraajii do \tmil gae milane vaale threedots ', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'piyaa bin naahiin  mil gae milane vaale  miyaanbiivii raajii', 'year': '1960'}`
- output: `{"pred": "naushad", "top3": ["naushad", "shankarjaikishan", "kalyanjianandji"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='naushad' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='s d burman' in top3=['naushad', 'shankarjaikishan', 'kalyanjianandji']

### #276 — FAIL

- item: `{'lyrics': ' tumane piyaa tumane piyaa diyaa sab kuchh mujhako apanii priit daii ke raam kare yuun hii biite jiivan tumhare giit gaii ke2 tumane piyaa  main to huun bholii aisii bholii piyaa  jaise thii raadhikaa kaanhaa kii premikaa2 shyaam kahiin shyaam kahiin ban jaiyyo na tum merii sudh bhulaii ke raam kare yuun hii biite jiivan tumhare giit gaii ke tumane piyaa  mere mitawaa re mere mitawaa re mile jab se tum mujhe bindiyaa maathe saje paayal merii baje2 maang bhare  maang bhare merii nis din ab sinduurii saanjh aii ke  tum ne piyaa diyaa saba kuchh mujhako apanii priit daii ke raam kare yuun hii biite jiivan tumhare giit gaii ke', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'tumane piyaa diyaa sab kuchh', 'year': '1974'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "laxmikantpyarelal", "s d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='r d burman' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='s d burman' in top3=['r d burman', 'laxmikantpyarelal', 's d burman']

### #277 — FAIL

- item: `{'lyrics': ' muhabbat jaag uthii hai zamaanaa so rahaa hai ai ye kyaa ho rahaa hai are ye kyaa ho rahaa hai bhaaii kuchh nahiin kuchh nahiin pyaar ho rahaa hai niind jaa rahii hai chain kho rahaa hai pyaar pyaar pyaar pyaar pyaar ho rahaa hai hai pyaar ho rahaa hai haay ye kyaa ho rahaa hai threedots  dilon men aag lagii hai zamaanaa so rahaa hai sone do sone do sone do zamaane ko sone do haay ye kyaa ho rahaa hai threedots  pyaar men sharaab sii mastii hai chaal men dekh na le koii hamen is haal men ham dekh to rahaa hai ye kyaa ho rahaa hai threedots  tere mere biich kaa bhed na khol de koii jaa ke kuchh mere bhaiyaa se na bol de bhaiyaa bol to rahaa hai ye kyaa ho rahaa hai threedots  saare jahaan pe nashaa chhaa rahaa hai koii hans rahaa hai koii gaa rahaa hai are koii ro rahaa hai ye kyaa ho rahaa hai threedots ', 'correct_label': 'annu malik', 'label': 1, 'split': 'test', 'title': 'muhabbat jaag uthii hai  ye kyaa ho rahaa hai', 'year': '2002'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "annu malik", "c ramchandra"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='shankarjaikishan' ref='annu malik'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='annu malik' in top3=['shankarjaikishan', 'annu malik', 'c ramchandra']

### #278 — FAIL

- item: `{'lyrics': ' main pankh lagaake ud jaauun main pankh lagaake ud jaauun aur phir naa palat ke aauun main pankh lagaake ud jaauun na na naa na na naa na na naa2 main pankh lagaake ud jaauun  laharon men jhuuluun taaron ko chhuuluun laharon men jhuuluun ambar kii chhaatii se lag kar sapanon men kho jaauun anajaanii raahon men chhup kar anajaanii ho jaauun aur kud bhii khoj naa paauun main pankh lagaake ud jaauun threedots  laharon men jhuuluun taaron ko chhuuluun laharon men jhuuluun badalii banakar ban ban ghuumuun bijalii ban musakaauun jharanon kii jhaalar men baithii giit suhaanii gaauun duniyaa ko nazar naa aauun main pankh lagaake ud jaauun threedots', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'main pankh lagaa ke ud jaauun', 'year': '1953'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "shankarjaikishan", "madan mohan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='s d burman' in top3=['laxmikantpyarelal', 'shankarjaikishan', 'madan mohan']

### #279 — FAIL

- item: `{'lyrics': ' dil naa ummiid to nahiin naakaam hii to hai  lambii hai gam kii shaam magar shaam hii to hai   ye safar bahut hai kathin magar  na udaas ho mere hamasafar   1 ye sitam kii raat hai dhalane ko  hai andheraa gam kaa pighalane ko  zaraa der is men lage agar na udaas threedots   2 nahiin rahanevaalii ye mushkilen  ye hain agale mod pe manzilen  merii baat kaa tuu yakiin kar na udaas threedots   3 kabhii dhundh legaa ye kaaravaan  vo naii zamiin nayaa aasamaan  jise dhuundhatii hai terii najar na udaas threedots ', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'ye safar bahut hai kathiin magar', 'year': '-1'}`
- output: `{"pred": "madan mohan", "top3": ["madan mohan", "kalyanjianandji", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='madan mohan' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='r d burman' in top3=['madan mohan', 'kalyanjianandji', 'laxmikantpyarelal']

### #280 — FAIL

- item: `{'lyrics': ' e bhaaii zaraa dekhake chalo aage hii nahiin piichhe bhii  daayen hii nahiin baayen bhii uupar hii nahiin niiche bhii  2 e bhaaii  tuu jahaan aayaa hai vo teraa  ghar nahiin gaanv nahiin galii nahiin kuuchaa nahiin rastaa nahiin bastii nahiin  duniyaa hai aur pyaare duniyaa yah ek sarakas hai aur is sarakas men  bade ko bhii chote ko bhii khare ko bhii khote ko bhii mote ko bhii patale ko bhii niiche se uupar ko uupar se niiche ko  baraabar aanaajaanaa padataa hai   aur ring maastar ke kode par  kodaa jo bhuukh hai  kodaa jo paisaa hai kodaa jo qismat hai  tarahtarah naach kar dikhaanaa yahaan padataa hai  baarbaar ronaa aur gaanaa yahaan padataa hai  hiiro se jokar ban jaanaa padataa hai\t\t 2  girane se darataa hai kyon marane se darataa hai kyon thokar tuu jab na khaaegaa paas kisii gam ko na jab tak bulaaegaa zindagii hai chiiz kyaa nahiin jaan paayegaa rotaa huaa aayaa hai chalaa jaaegaa kaisaa hai karishmaa kaisaa khilavaad hai jaanavar aadamii se zyaadaa vafaadaar hai khaataa hai kodaa bhii rahataa hai bhuukhaa bhii phir bhii vo maalik par karataa nahiin vaar hai  aur insaan yah  maal jis kaa khaataa hai pyaar jis se paataa hai giit jis ke gaataa hai usii ke hii siine men bhokataa kataar hai   haan baabuu yah sarakas hai sho tiin ghante kaa pahalaa ghantaa bachapan hai duusaraa javaanii hai tiisaraa budhaapaa hai   aur usake baad  maan nahiin baap nahiin betaa nahiin betii nahiin tuu nahiin main nahiin kuchh bhii nahiin rahataa hai rahataa hai jo kuchh vo  kaaliikaalii kursiyaan hain kaaliikaalii taambuu hai kaaliikaalii gheraa hai binaa chidiyaa kaa baseraa hai na teraa hai na meraa hai ', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'ai bhaaii zaraa dekhake chalo aage hii nahiin piichhe bhii', 'year': '1970'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "a r rahman", "s d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='shankarjaikishan' in top3=['laxmikantpyarelal', 'a r rahman', 's d burman']

### #281 — PASS

- item: `{'lyrics': '  ra \tmujhe kitanaa pyaar hai tum se apane hii dil se puuchho tum \tjise dil diyaa hai vo tum ho merii zindagii tumhaarii la \tmujhe kitanaa pyaar threedots  ra \tchaahat ne terii mujhako kuchh is tarah se gheraa \tdin ko hain tere charche raaton ko kvaab teraa la \ttum ho jahaan vahiin par rahataa hai dil bhii meraa \tbas ik kyaal teraa kyaa shaam kyaa saveraa ra \tmujhe kitanaa pyaar threedots  la \tye duniyaa kaise badalii kuchh bhii samajh na aae \tkyuun ho gae hain apane kal tak the jo paraae ra \tdil kii lagan ho sachchii phir kyon na rang laae \tmere the tum sadaa se par ab qariib aae la \tmujhe kitanaa pyaar threedots  ra \tmerii vafaa ko ab to yuun aajamaanaa chhodo \tdil ko churaa ke mere aankhen churaanaa chhodo la \tmujhako banaa ke apanaa baaten banaanaa chhodo \tmain kab na thii tumhaarii ab to sataanaa chhodo ra \tmujhe kitanaa pyaar threedots do \tmujhe kitanaa pyaar threedots ', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'mujhe kitanaa pyaar hai tum se apane hii dil se puuchho tum', 'year': '1962'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "kalyanjianandji", "madan mohan"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='shankarjaikishan' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='shankarjaikishan' in top3=['shankarjaikishan', 'kalyanjianandji', 'madan mohan']

### #282 — FAIL

- item: `{'lyrics': '  chhod kar tere pyaar kaa daaman ye bataa de ki ham kidhar jaayen ham ko dar hai ki terii baahon men ham khushii se na aaj mar jaayen  mil gaye aaj qaafile dil ke ham khade hain kariib manzil ke muskuraa kar jo tum ne dekh liye mit gaye hans ke sab gile dil ke kitanii pyaarii hain ye hasiin ghadiyaan in se kah do yahiin thahar jaayen ham ko dar hai threedots  tere kadamon pe zindagii rakh duun apanii aankhon kii roshanii rakh duun tuu agar khush ho main tere dil men apane dil kii har ik khushii rakh duun mere hamadam merii khushii ye hai tuu nazar aaye ham jidhar jaayen chhod kar tere threedots ', 'correct_label': 'madan mohan', 'label': 5, 'split': 'test', 'title': 'chhod kar tere pyaar kaa daaman', 'year': '-1'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "madan mohan", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='madan mohan'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='madan mohan' in top3=['laxmikantpyarelal', 'madan mohan', 'shankarjaikishan']

### #283 — FAIL

- item: `{'lyrics': ' r jis din se maine tumako dekhaa hai is dil men ik sapanaa saa jaagaa hai ijaazat ho to sunaa duun  2  a is dil ne jabase tumako paayaa hai kuchh choriichorii maine bhii dekhaa hai gar ijaazat ho to bataa duun  2  r shokhii hai nazaaqat hai aankhon men sharaarat hai aise bhii sharamaanaa kyaa kah do ki mohabbat hai a kahane kii zaruurat kyaa baaton kii haqiiqat kyaa chhalake na nigaahon se aisii bhii muhabbat kyaa kuchh khoyaakhoyaa dil bhii rahataa hai kuchh choriichorii maine bhii dekhaa hai ijaazat ho threedots  r dil ko naa sambhaaluun to siine se lagaa luun to hothon kii jo laalii hai usako main churaa luun to a yuun nazaren na daalo tum ab dil ko sambhaalo tum dekhe na hamen duniyaa siine men chhupaa lo tum na jaane mujhako dar kyon lagataa hai kuchh choriichorii maine bhii dekhaa hai ijaazat ho threedots', 'correct_label': 'madan mohan', 'label': 5, 'split': 'test', 'title': 'jis din se main ne tumako dekhaa hai is dil men ik sapanaa saa jaagaa hai', 'year': '1971'}`
- output: `{"pred": "annu malik", "top3": ["annu malik", "shankarjaikishan", "r d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='annu malik' ref='madan mohan'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='madan mohan' in top3=['annu malik', 'shankarjaikishan', 'r d burman']

### #284 — PASS

- item: `{'lyrics': ' jab ziiro diyaa mere bhaarat ne  bhaarat ne mere bhaarat ne  duniyaa ko tab ginatii aayii  taaron kii bhaashhaa bhaarat ne  duniyaa ko pahale sikhalaayii   detaa na dashamalav bhaarat to  yuun chaand pe jaanaa mushkil thaa dharatii aur chaand kii duurii kaa andaaz lagaanaa mushkil thaa  sabhyataa jahaan pahale aayii pahale janamii hai jahaan pe kalaa  apanaa bhaarat jo bhaarat hai  jisake piichhe sansaar chalaa sansaar chalaa aur aage badhaa jyuun aage badhaa badhata hii gayaa  bhagavaan kare ye aur badhe  badhataa hii rahe aur phuulephale   madanapuri chup kyon ho gaye aur sunaao  hai priit jahaan kii riit sadaa  main giit vahaan ke gaataa huun bhaarat kaa rahane vaalaa huun  bhaarat kii baat sunaataa huun   kaalegore ka bhed nahiin  har dil se hamaaraa naataa hai  kuchh aur na aataa ho hamako  hamen pyaar nibhaanaa aataa hai  jise maan chukii saarii duniyaa  main baat vohii doharaataa huun  bhaarat kaa rahane vaalaa huun  bhaarat kii baat sunaataa huun   jiite ho kisiine desh to kyaa hamane to dilon ko jiitaa hai  jahaan raam abhii tak hai nar men  naarii men abhii tak siitaa hai  itane paavan hain log jahaan  main nitnit shiish jhukaataa huun  bhaarat kaa rahane vaalaa huun  bhaarat kii baat sunaataa huun   itanii mamataa nadiyon ko bhii  jahaan maataa kahake bulaate hai  itanaa aadar insaan to kyaa patthar bhii puuje jaaten hai  is dharatii pe mainne janam liyaa  ye soch ke main itaraataa huun  bhaarat kaa rahane vaalaa huun  bhaarat kii baat sunaataa huun ', 'correct_label': 'kalyanjianandji', 'label': 3, 'split': 'test', 'title': 'hai priit jahaan kii riit sadaa', 'year': '1970'}`
- output: `{"pred": "kalyanjianandji", "top3": ["kalyanjianandji", "a r rahman", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='kalyanjianandji' ref='kalyanjianandji'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='kalyanjianandji' in top3=['kalyanjianandji', 'a r rahman', 'shankarjaikishan']

### #285 — FAIL

- item: `{'lyrics': ' tera cheharaa mujhe gulaab lage  dono aalam men laajavaab lage  din ko dekhun to aafatab lage  shab ko dekhun to maahataab lage   roz milate ho par nahiin milate  aisaa milana bhi mujhako khvab lage  padhata rahata hun teri surat ko  teri surat mujhe kitaab lage  tera cheharaa mujhethreedots   teri ankhon ki mastiyan taubaa  mujhako chhalaki hui sharaab lage  jab bhi chamake ghata men bijali  mujhako teraa hi vo shabaab lage  tera cheharaa mujhethreedots   tujhako dekhun to kis tarah dekhun  rukh pe kiranon ke sau naqaab lage  pyaar shaayad isi ko kahate hain  ek mujhase hi kyun hijaab lage  tera cheharaa mujhethreedots ', 'correct_label': 'annu malik', 'label': 1, 'split': 'test', 'title': 'teraa cheharaa mujhe gulaab lage', 'year': '-1'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "a r rahman", "kalyanjianandji"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='annu malik'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='annu malik' in top3=['laxmikantpyarelal', 'a r rahman', 'kalyanjianandji']

### #286 — PASS

- item: `{'lyrics': ' tuu kahe agar tuu kahe agar tuu kahe agar jiivan bhar main giit sunaataa jaaun man biin bajaataa jaaun tuu kahe agar  main saaz huun tuu saragam hai  2 detii jaa sahaare mujhako  2 main raag huun tu binaa hai  2 is dam jo pukaare tujhako aavaaz men teri har dam aavaaz milaataa jaauun aakaash pe chhaataa jaauun tu kahe agarthreedots  in bolon men tuu hii tuu hai main samajhuun yaa tuu jaane ho jaane inamen hai kahaanii merii inamen hai tere afasaane inamen hai tere afasaane tu saaz uthaa ulfat kaa main jhuum ke gaataa jaauun sapanon ko jagaataa jaauun tuu kahe agarthreedots', 'correct_label': 'naushad', 'label': 6, 'split': 'test', 'title': 'tuu kahe agar jiivan bhar main giit sunaataa jaauun', 'year': '1949'}`
- output: `{"pred": "naushad", "top3": ["naushad", "laxmikantpyarelal", "s d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='naushad' ref='naushad'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='naushad' in top3=['naushad', 'laxmikantpyarelal', 's d burman']

### #287 — FAIL

- item: `{'lyrics': '  pyaar kii manzil mast safar tum ho hasiin ham hain javaan saamane tum ho phir bhii hamen hosh nahiin ham hain kahaan pyaar kii manzil threedots  yuun hii sataauungaa din aur raat jab tak na dogii tum haathon men haath 2 ye zid bhii hai kitanii hamako dekhanaa hai pyaar kii manzil threedots  dam se hamaare hai tum par bahaar ehasaan maano jo kiyaa tumase pyaar 2 jalave to laakhon hain kaun puuchhataa hai pyaar kii manzil threedots  maano yaa na maano jii tum ho hasiin ajii dil kii baaton kaa kar lo yaqiin 2 mere dil ko tere dil se pyaar ho gayaa hai pyaar kii manzil threedots ', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'pyaar kii manzil mast safar tum ho hasiin', 'year': '1964'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "kalyanjianandji", "madan mohan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='shankarjaikishan' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='s d burman' in top3=['shankarjaikishan', 'kalyanjianandji', 'madan mohan']

### #288 — FAIL

- item: `{'lyrics': ' la ai dil na mujhase chhupaa     sach bataa kyaa huaa mu jaane bhii do dilarubaa     jo huaa so huaa  la taare gine raat bhar     jaane kab yaad men so gaii     vo kaab thaa madabharaa     jis men behosh main kho gaii     koii niind men hamase ruuth ke     hamako luut ke chal diyaa mu jaane bhii do dilarubaa     jo huaa so huaa  mu khidakii na chhodo khulii     pyaar ke chor hain taak men     kitanon kii chorii huii     madabharii chaandanii raat men     aise marz kii dil ke dard kii     dil kaa dard hii hai davaa la ai dil na mujhase chhupaa     sach bataa kyaa huaa  la baaten banaao na jii     raaz to aapake khul gae mu aankhen churaao na jii     nain se nain to mila gae la kyaa buraa huaa dil machal gayaa     ghar badal gayaa aapakaa mu jaane bhii do dilarubaa     jo huaa so huaa', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'ai dil na mujhase chhupaa sacha bataa kyaa huaa', 'year': '-1'}`
- output: `{"pred": "madan mohan", "top3": ["madan mohan", "c ramchandra", "s d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='madan mohan' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='shankarjaikishan' in top3=['madan mohan', 'c ramchandra', 's d burman']

### #289 — PASS

- item: `{'lyrics': '  mujhe tum mil gae hamadam sahaaraa ho to aisaa ho jidhar dekhuun udhar tum ho nazaaraa ho to aisaa ho mujhe tum mil gae threedots  kisii kaa chaand saa cheharaa nazar se chuum letii huun 2 kushii kii intahaan ye hai nashe men jhuum letii huun 2 huii taqadiir bhii roshan sitaaraa ho to aisaa ho jidhar dekhuun udhar threedots  udhar dil hai idhar jaan hai ajab mushkil kaa saamaan hai 2 labon par muskaraahat hai magar saanson men tuufaan hai 2 ye main jaanuun yaa tum jaano ishaaraa ho to aisaa ho jidhar dekhuun udhar threedots ', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'mujhe tum mil gae hamadam sahaaraa ho to aisaa ho', 'year': '1966'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "naushad", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='shankarjaikishan' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='shankarjaikishan' in top3=['shankarjaikishan', 'naushad', 'laxmikantpyarelal']

### #290 — FAIL

- item: `{'lyrics': ' baalam mujhase ruuth ke sautan ke ghar jaate ho sautan ke ghar jaate mujh ko kyon rulaate ho mujh ko kyon rulaate ho kyaa mazaa paate ho sautan ke ghar jaate  kal bhii to thii main baalam tumhaare gale kii haar dil laagaakar mere baalam dil laagaakar mere baalam tum ne kiyaa thaa pyaar  sautan ke ghar jaate  huii kyaa kataa bataado mujhako muunh jo tum ne pher liyaa priit kii riit sikhaake mujhako dil se duur hataa diyaa 2 sautan ke ghar jaate', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'baalam mujh se ruuth ke sautan ke ghar jaate ho', 'year': '-1'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "c ramchandra", "naushad"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='shankarjaikishan' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='s d burman' in top3=['shankarjaikishan', 'c ramchandra', 'naushad']

### #291 — PASS

- item: `{'lyrics': '  dil ko haay dil ko terii tasviir se bahalaae hue hain is ghar men ham ik chaand ko chamakaae hue hain  ab kaun sii daulat hai jo taqadiir se maange ulfat hii badii chiiz thii jo paae hue hain  jab tuu hai kyaalon men to duniyaa se hamen kyaa duniyaa ko terii yaad men thukaraae hue hain  mitakar bhii na daaman teraa haathon se chhuutegaa ham terii mohabbat kii qasam khaae hue hain ', 'correct_label': 'naushad', 'label': 6, 'split': 'test', 'title': 'dil ko terii tasviir se bahalaae hue hain', 'year': '1950'}`
- output: `{"pred": "naushad", "top3": ["naushad", "c ramchandra", "madan mohan"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='naushad' ref='naushad'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='naushad' in top3=['naushad', 'c ramchandra', 'madan mohan']

### #292 — PASS

- item: `{'lyrics': '  dil tuu bhii gaa pyaar men muskaraa sapane men jo aate hain akasar mahafil men unako bulaa ke laa dil tuu bhii gaa kal jo huaa so huaa bhuul jaa  vo bhii na bole ham bhii na bole aankh milii pahachaan huii koii chalaa jab saath safar men hamako dagar aasaan huii  ruupnagar kii bhiid men hamane kud ko bhulaanaa siikh liyaa hai  dard balaa kaa dard hai lekin hosh nahiin to kuchh bhii nahiin aaj jahaan ko ham duniyaa ko chhod ke aae duur kahiin ', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'dil tuu bhii gaa pyaar men muskaraa', 'year': '1963'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "naushad", "c ramchandra"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='shankarjaikishan' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='shankarjaikishan' in top3=['shankarjaikishan', 'naushad', 'c ramchandra']

### #293 — FAIL

- item: `{'lyrics': ' aasamaan ke niiche ham aaj apane piichhe pyaar kaa jahaan basaa ke chale kadam ke nishaan banaa ke chale aasamaan  threedots  tum chale to phuul jaise aanchal ke rang se saj gai raahen saj gai raahen paas aao mai pahanaa duun chaahat kaa haar ye khulii khulii baahen khulii khulii baahen jis kaa ho aanchal khud hii chaman kahiye vo kyuun haar baahon ke daale aasamaan threedots  bolatii hain aaj aankhen kuchh bhii na aaj tum kahane do hamako kahane do hamako bekhudii badhatii chalii hai ab to kaamosh hii rahane do hamako rahane do hamako ik baar ek baar mere liye kah do khanaken laal honthon ke pyaale aasamaan threedots  saath mere chal ke dekho aai hain duur se ab kii bahaaren ab kii bahaaren har galii har mod pe vo donon ke naam se hamako pukaare tumako pukaare kah do bahaaron se aae na idhar un tak uthakar ham nahiin jaane vaale aasamaan threedots', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'aasamaan ke niiche ham aaj apane piichhe', 'year': '1967'}`
- output: `{"pred": "madan mohan", "top3": ["madan mohan", "shankarjaikishan", "r d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='madan mohan' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='s d burman' in top3=['madan mohan', 'shankarjaikishan', 'r d burman']

### #294 — PASS

- item: `{'lyrics': ' ko \tbol kisakaa naam hai 2 \tkaalii kaalii aankhon men gore gore gaalon \tpe lambe lambe baalon men \tsaanson men kvaabon men baaton men baahon men \tbol bol bol bol bol bol bol  ku \tlaal laal honthon pe gorii kisakaa naam hai \tdil men kaun rahataa hai kisakaa muqaam hai \tare laal laal honthon pe gorii kisakaa naam hai 2 \tlaal laal honthon pe bol kisakaa naam hai  a \tlaal laal honthon pe piyaa teraa naam hai \tmain huun kaniiz dil teraa gulaam hai \tare laal laal honthon pe piyaa teraa naam hai \tlaal laal honthon pe bas teraa naam hai \tdil kaa tuu maalik hai dil teraa muqaam hai ko \tlaal laal honthon pe threedots  ku \ttere dil kii kalii pahale kabhii kyaa khilii thii \tmujhase pahale kabhii kyaa tuu kisii se milii thii a \tare naa baabaa naa ilzaam ye naa lagaanaa \ttujhase pahale kabhii apanaa kisii ko naa maanaa  \thaa aa 2 ku \tmere siine pe locket \tlocket men terii hii tasviir maine sajaaii a \tmeraa tuu chaandii sonaa \tteraa hii honaa hai karanii hai tujhase sagaaii ku \tniichii nigaahon kaa  tujhako salaam hai  2 \tkaalii kaalii aankhon men gorii kisakaa naam hai a \tkaalii kaalii aankhon men piyaa teraa naam hai ku \tare laal laal honthon pe threedots  a \to tere haath men rumaal paan kii rachaaii hai laalii \ttirachhii topii terii lagataa hai tuu to mavaalii ku \tmain huun majanuun teraa merii lailaa nahiin main mavaalii \tapane aashiq ko tuu detii hai kyuun aisii gaalii a \thaa aa 2 ku \tdil tujh pe qurbaan kiyaa teraa hii naam liyaa \tzindaa merii shaayarii tuu a \tnahiin dekhaa naa dekhuungii tere sivaa auron ko \tzindaa merii aashiqii tuu \tmujhako ek bas  tujhase hii kaam hai  2 ku \tterii har dhadakan men gorii kisakaa naam hai a \tmerii har dhadakan men piyaa teraa naam hai ku \tare laal laal honthon pe threedots ', 'correct_label': 'annu malik', 'label': 1, 'split': 'test', 'title': 'bol kisakaa naam hai  laal laal honthon pe', 'year': '1995'}`
- output: `{"pred": "annu malik", "top3": ["annu malik", "r d burman", "s d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='annu malik' ref='annu malik'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='annu malik' in top3=['annu malik', 'r d burman', 's d burman']

### #295 — FAIL

- item: `{'lyrics': '  diivaanon se ye mat puuchho diivaanon pe kyaa guzarii hai haan unake dilon se ye puuchho aramaanon pe kyaa guzarii hai diivaanon se ye mat puuchho   threedots  auron ko pilaate rahate hain aur kud pyaase rah jaate hain ye piine vaale kyaa jaane paimaanon pe kyaa guzarii hai diivaanon se ye mat puuchho   threedots  maalik ne banaayaa inasaan ko inasaan muhabbat kar baithaa vo uupar baithaa kyaa jaane inasaanon pe kyaa guzarii hai diivaanon se ye mat puuchho   threedots', 'correct_label': 'kalyanjianandji', 'label': 3, 'split': 'test', 'title': 'diivaanon se ye mat puuchho', 'year': '1967'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "shankarjaikishan", "kalyanjianandji"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='kalyanjianandji'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='kalyanjianandji' in top3=['laxmikantpyarelal', 'shankarjaikishan', 'kalyanjianandji']

### #296 — FAIL

- item: `{'lyrics': ' kyaa se kyaa ho gayaa bevafaa aaa tere pyaar men chaahaa kyaa kyaa milaa bevafaa aaa tere pyaar men  chalo suhaanaa bharam to tuutaa jaanaa ke husn kyaa hai ho o o chalo suhaanaa bharam to tuutaa jaanaa ke husn kyaa hai kahatii hai jisako pyaar duniyaa kyaa chiiz kyaa balaa hai dil ne kyaa naa sahaa bevafaa aaa tere pyaar men chaahaa kyaa threedots  tere mere dil ke biich ab to sadiyon ke faasale hain ho o o tere mere dil ke biich ab to sadiyon ke faasale hain yaqiin hogaa kise ki ham tum ik raah sang chale hain honaa hai aur kyaa bevafaa aaa tere pyaar men chaahaa kyaa threedots', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'kyaa se kyaa ho gayaa bevafaa tere pyaar men', 'year': '1965'}`
- output: `{"pred": "annu malik", "top3": ["annu malik", "shankarjaikishan", "s d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='annu malik' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='s d burman' in top3=['annu malik', 'shankarjaikishan', 's d burman']

### #297 — FAIL

- item: `{'lyrics': '  na tuu zamiin ke lie hai na aasamaan ke lie 2  teraa vajuud hai   2 ab sirf daastaan ke lie na tuu zamiin ke threedots  palat ke suuechaman dekhane se kyaa hogaa 2 vo shaak hii na rahii jo thii aashiyaan ke lie na tuu zamiin ke threedots  garazparast jahaan men vafaa talaash na kar 2 ye shai banii hai kisii duusare jahaan ke lie na tuu zamiin ke threedots ', 'correct_label': 'laxmikantpyarelal', 'label': 4, 'split': 'test', 'title': 'na tuu zamiin ke lie hai na aasamaan ke lie', 'year': '1972'}`
- output: `{"pred": "madan mohan", "top3": ["madan mohan", "laxmikantpyarelal", "s d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='madan mohan' ref='laxmikantpyarelal'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='laxmikantpyarelal' in top3=['madan mohan', 'laxmikantpyarelal', 's d burman']

### #298 — FAIL

- item: `{'lyrics': '  mehandii lagii mere haath re mehandii lagii mere haath bhuul jaa isako e dil ye to sapanon kii thii baat re mehandii lagii mere threedots  anajaane men main baavariyaa likh baithii tere naam umariyaa nibh na sakegii baat re mehandii lagii mere threedots  maang bhii ujadii dil bhii tuutaa mehandii kaa rang bhii nikalaa jhuuthaa ansuan se dhoe haath re mehandii lagii mere threedots  unakii galii kaa pheraa chhodaa aap hii apane dil ko todaa ban gaii aisii baat re mehandii lagii mere threedots  dvaar bajii thii jo shahanaaii vah shahanaaii thii harajaaii chhod gaii meraa haath re mehandii lagii mere threedots ', 'correct_label': 'kalyanjianandji', 'label': 3, 'split': 'test', 'title': 'mehandii lagii mere haath re', 'year': '1962'}`
- output: `{"pred": "annu malik", "top3": ["annu malik", "shankarjaikishan", "r d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='annu malik' ref='kalyanjianandji'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='kalyanjianandji' in top3=['annu malik', 'shankarjaikishan', 'r d burman']

### #299 — FAIL

- item: `{'lyrics': ' ki shokhiyon men gholaa jaaye phuulon kaa shabaab  usamen phir milaayii jaaye thodii sii sharaab hogaa yuun nashaa jo taiyaar haanthreedots hogaa yun nashaa jo taiyaar vo pyaar hai \t shokhiyon men gholaa jaaye phuulon kaa shabaab  usamen phir milaayii jaaye thodii sii sharaab   hogaa yuun nashaa jo taiyaar vo pyaar hai shokhiyon men gholaa jaaye phuulon ka shabaab \t he he he he he threedots \t lataa \thansataa huaa bachapan vo bahakaa huaa mausam hai chhedo to ik sholaa hai chhuulo to bas shabanam hai hansataa huaa bachapan vo bahakaa huaa mausam hai chhedo to ik sholaa hai chhuulo to bas shabanam hai gaaon men mele men raah men akele men aataa jo yaad baar baar vo pyaar hai shokhiyon men gholaa jaaye phuulon ka shabaab usamen phir milaayii jaaye thodii sii sharaab ki are hogaa yun nashaa jo taiyaar vo pyaar hai dono shokhiyon men gholaa jaaye phuulon kaa shabaab  \t lataa \tothreedots ra ra ra rathreedots ki rang men pighale sonaa ang se yuun ras jhalake jaise baje dhun koii raat men halake halake rang men pighale sonaa ang se yun ras jhalake jaise baje dhuna koii raat men halke halke dhuup men chhaaon men jhuumatii havaaon men har dam kare jo intazaar vo pyaar hai shokhiyon men gholaa jaaye phulon ka shabab  usamen phir milaayii jaaye thodii sii sharaab lataa othreedots hogaa yun nashaa jo taiyaar ki vo pyaar \t ki yaad agar vo aaye lataa \tho threedots yaad agar vo aaye kaise kate tanahai         suune shahar men jaise bajane lage shahanai   ki yaad agar vo aaye kaise kate tanahai         suune shahar men jaise bajane lage shahanai   dono aanaa ho jaanaa ho kaisaa bhii zamaanaa ho utare kabhii naa jo khumaar vo pyaar hai  shokhiyon men gholaa jaaye phuulon kaa shabaab  usamen phir milaayii jaaye thodii sii sharaab ki are hogaa yuun nashaa jo taiyaar lataa vo pyaar hai  dono shokhiyon men gholaa jaaye phuulon kaa shabaab', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'shokhiyon men gholaa jaaye phuulon kaa shabaab', 'year': '-1'}`
- output: `{"pred": "a r rahman", "top3": ["a r rahman", "c ramchandra", "s d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='a r rahman' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='s d burman' in top3=['a r rahman', 'c ramchandra', 's d burman']

### #300 — FAIL

- item: `{'lyrics': ' sharm aatii hai mujhako sahelii nayaa ghar hai main dulhan navelii baat man kii ye hai kuchh pahelii rahane do ise tum pahelii  kyaa merii prem kahaanii  nadiyaa se bichhadaa paanii  2 kyaa merii prem kahaanii  nadiyaa se bichhadaa paanii  2  bhuul jaatii hain baabul kii galiyaan duur sanjog le jaate hain phuul banatii hain jab khilake kaliyaan todake log le jaate hain ek raajaa le aayaa banaake mujhe raanii  nadiyaa se bichhadaa paanii  2  jaane kis kis galii se guzarake ghar saajan ke baaraat aaii sab saathii puraane wahiin chhuute yaad unakii mere saath aaii ye jo aansuu hain ye hain un hii kii nishaanii  nadiyaa se bichhadaa paanii  2  kyaa merii prem kahaanii  nadiyaa se bichhadaa paanii  2', 'correct_label': 'laxmikantpyarelal', 'label': 4, 'split': 'test', 'title': 'kyaa merii prem kahaanii', 'year': '1975'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "a r rahman", "s d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='r d burman' ref='laxmikantpyarelal'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='laxmikantpyarelal' in top3=['r d burman', 'a r rahman', 's d burman']

### #301 — FAIL

- item: `{'lyrics': '  kaun rokegaa ab pyaar kaa raastaa main to pii kii nagariyaa jaane lagii aaj baithebithaae ye kyaa ho gayaa dil kii har baat aankhon men aane lagii main to pii kii nagariyaa threedots   aa gae  2 muskuraane ke din ladakhadaane ke din gunagunaane ke din maine paayal to paanvon men baandhii nahiin aur aavaaz ghungharuu kii aane lagii main to pii kii nagariyaa threedots  koii raahon men kaliyaan bichhaane lagaa aur ishaaron se mujhako bulaane lagaa maine darpan abhii tak to dekhaa nahiin  aur bindiyaa  2 magar jhilamilaane lagii main to pii kii nagariyaa threedots  aaj kaisii chalii bhiigiibhiigii pavan sarasaraane lagaa meraa naazuk badan maine palaken abhii tak jhukaaii nahiin niind kyuun merii aankhon men aane lagii main to pii kii nagariyaa threedots ', 'correct_label': 'madan mohan', 'label': 5, 'split': 'test', 'title': 'kaun rokegaa ab  main to pii kii nagariyaa jaane lagii', 'year': '1968'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "r d burman", "kalyanjianandji"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='madan mohan'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='madan mohan' in top3=['laxmikantpyarelal', 'r d burman', 'kalyanjianandji']

### #302 — FAIL

- item: `{'lyrics': ' itanaa to yaad hai mujhe o itanaa to yaad hai mujhe haay itanaa to yaad hai mujhe ke unase mulaaqaat huii baad men jaane kyaa huaa naa jaane kyaa baat huii  saare vafaa ke karz apane chukaake kisii se dil lagaake chalaa aayaa nazaren milaake niind apanii ganvaake kasak dil men basaake chalaa aayaa din to guzar jaayegaa kyaa hogaa jab raat huii itanaa to yaad hai mujhe   threedots  maare hayaa ke main to aankhen jhukaake zaraa daaman bachaake chalii aayii pardaa hataake unakii baaton men aake unhen suurat dikhaake chalii aayii kis se shiqaayat karuun sharaarat mere saath huii itanaa to yaad hai mujhe   threedots  thii ik kahaanii pahale ye zindagaanii tumhen dekhaa to jiinaa mujhe aayaa dilbarojaanii sharm se paanii paanii huii main bas pasiinaa mujhe aayaa aise main bhiig gayii jaise ke barasaat huii itanaa to yaad hai mujhe   threedots ', 'correct_label': 'laxmikantpyarelal', 'label': 4, 'split': 'test', 'title': 'itanaa to yaad hai mujhe ki unase mulaaqaat huii', 'year': '-1'}`
- output: `{"pred": "madan mohan", "top3": ["madan mohan", "shankarjaikishan", "r d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='madan mohan' ref='laxmikantpyarelal'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='laxmikantpyarelal' in top3=['madan mohan', 'shankarjaikishan', 'r d burman']

### #303 — PASS

- item: `{'lyrics': ' ajiib daastaan hai ye kahaan shuruu kahaan khatam ye manzilen hai kaun sii na vo samajh sake na ham ajiib daastaanthreedots  ye roshanii ke saath kyon  dhuaan uthaa chiraag se \t2 ye kvaab dekhatii huun main ke jag padii huun kvaab se ajiib daastaanthreedots  kisiikaa pyaar leke tum  nayaa jahaan basaaoge \t2 ye shaam jab bhii aaegii tum hamako yaad aaoge ajiib daastaanthreedots  mubaaraken tumhen ke tum  kisiike nuur ho gae\t\t2 kisiike itane paas ho ke sabase duur ho gae ajiib daastaanthreedots', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'ajiib daastaan hai ye kahaan shuruu kahaan khatam', 'year': '1959'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "annu malik", "s d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='shankarjaikishan' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='shankarjaikishan' in top3=['shankarjaikishan', 'annu malik', 's d burman']

### #304 — FAIL

- item: `{'lyrics': ' jiyaa le gayo jii moraa saanvariyaa laagii man men lagan huii baavariyaa  pa ni ni  ni re re  re ma ma  ma dha pa ma pa re ni re re  re ma ma  ma dha dha  dha saa ni dha ni pa  o papiihe o papiihe tuune papiihe nahiin dekhe more sainyaa dekhe to lelegaa unakii balaiyaan jaa re divaane maar naa taane piyaa kii sun jaake baansuriyaa  saamane aae to main aankhon men chhupaa luun thaamake bainyaa unhen dilamen bithaa luun shaam savere saath ho mere gorii ke sang jaise gaagariyaa  aaj kisii ne mujhe apanaa banaayaa saath rahuungii jaise piyaa kii main chaayaa thandii havaaon tum bhii to gaao priit kii dekho baaje jhaanjhariyaa ', 'correct_label': 'madan mohan', 'label': 5, 'split': 'test', 'title': 'jiyaa le gayo jii moraa saanvariyaa laagii man men lagan', 'year': '1962'}`
- output: `{"pred": "naushad", "top3": ["naushad", "c ramchandra", "madan mohan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='naushad' ref='madan mohan'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='madan mohan' in top3=['naushad', 'c ramchandra', 'madan mohan']

### #305 — PASS

- item: `{'lyrics': ' hu hu hu hu o o o o o o o laa laa la la la laa ho mere yaaraa diladaaraa zaraa sunsun  mere dil kii badalatii dhundhun  dil jhuum ke gaaye gungun  o mere dil ne kisii ko liyaa chunchun  ho hamen to bataao dekho na chhupaao  bolobolo usakaa jo naam hai  ho mere yaaraa diladaaraa zaraa sunsun kyuun dil kii hai badalii dhundhun  kyuun gaataa hai dil teraa gungun  tuune kis ko liyaa hai chunchun  he he hai koii hasiinaa hosh meraa chhiinaa  dinraat usakaa ye kaam hai  dil men jo tere dinraat hai  aisii bhii us men kyaa baat hai  dil men jo tere dinraat hai aisii bhii us men kyaa baat hai merii vo dulaarii hai badii pyaarii  pyaaraa pyaaraa usakaa naam hai  tere dil men hai koii to mere dil men bhii koii hai  ye dil kii lagii hai yaaraa yaa dillagii koii hai  meraa dil hai ik mandir to mohabbat kii vo devii hai  chalo hamanen ye jaanaa kii tumane mohabbat kii hai  hamen to bataao dekho na chhupaao bolo bolo usakaa jo naam hai  hamen to bataao dekho na chhupaao kyaa usakaa naam hai  2  mere yaaraa diladaaraa zaraa sunsun kyuun dil kii hai badalii dhundhun kyuun gaataa hai dil teraa gungun ho tuune kis ko liyaa hai chunchun  he he he hai vo anjaanii koii divaanii dil men jo mere subahoshaam hai o o o o o o o  laa laa la la la laa  tumhaarii hai koii kahaanii tumhaaraa koii afasaanaa  magar tere dil men kyaa hai kisii ne nahiin ye jaanaa  kaii din se mere dil men bhii hai ik sapanaa suhaanaa  vo sapanaa sunaa do hamako ki ik din to hogaa sunaanaa   hamen to bataao dekho naa chhupaao kyaa usakaa naam hai  2  he mere yaaraa diladaaraa zaraa sunsun kyuun dil kii hai badalii dhundhun kyuun gaataa hai dil teraa gungun ho tuune kis ko liyaa hai chunchun  hai vo anjaanaa koii divaanaa duniyaa men badaa badanaam hai  he mere yaaraa diladaaraa zaraa sunsun kyuun dil kii hai badalii dhundhun kyuun gaataa hai dil teraa gungun ho tuune kis ko liyaa hai chunchun  laa laa la la la laa ', 'correct_label': 'a r rahman', 'label': 0, 'split': 'test', 'title': 'mere yaaraa diladaaraa zaraa sunsun', 'year': '1997'}`
- output: `{"pred": "a r rahman", "top3": ["a r rahman", "annu malik", "kalyanjianandji"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='a r rahman' ref='a r rahman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='a r rahman' in top3=['a r rahman', 'annu malik', 'kalyanjianandji']

### #306 — FAIL

- item: `{'lyrics': '  jo guzar rahii hai mujh par use kaise main bataauun 2 vo kushii milii hai mujhako main kushii se mar na jaauun 2  mere dil kii dhadakanon kaa ye salaam tumako pahunche main tumhaaraa hamanashiin huun ye payaam tumako pahunche use bandagii main samajhuun jo tumhaare kaam aauun vo kushii milii hai threedots  mere dil kii mahafilon men vo muqaam hai tumhaaraa ke kudaa ke baad lab par bas naam hai tumhaaraa merii aarazuu yahii hai main tumhaare giit gaauun vo kushii milii hai threedots  merii zindagii men hamadam kabhii gam na tuu uthaanaa kabhii aaen jo andhere mujhe pyaar se bulaanaa main chiraag huun vafaa kaa main andhere jagamagaauun vo kushii milii hai threedots ', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'jo guzar rahii hai mujh par use kaise main bataauun', 'year': '1968'}`
- output: `{"pred": "c ramchandra", "top3": ["c ramchandra", "kalyanjianandji", "madan mohan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='c ramchandra' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='shankarjaikishan' in top3=['c ramchandra', 'kalyanjianandji', 'madan mohan']

### #307 — FAIL

- item: `{'lyrics': '  shyaamal shyaamal baran komal komal charan tere mukhade pe chandaa gagan kaa jadaa bade man se vidhaataa ne tujh ko gadhaa  tere baalon men simatii saavan kii ghataa aa tere gaalon pe chhitakii puunam kii chhataa o puunam kii chhataa tiikhe tiikhe nayan miithe miithe bayan tere angon pe champaa kaa rang chadhaa bade man se vidhaataa ne threedots  o ye umar ye kamar sau sau bal khaa rahii terii tirachhii nazar tiir barasaa rahii naazuk naazuk badan dhiime dhiime chalan terii baankii lachak men hai jaaduu badaa bade man se vidhaataa ne threedots  kis paaras se sonaa ye takaraa gayaa tujhe rach ke chiteraa bhii chakaraa gayaa na idhar jaa sakaa na udhar jaa sakaa dekhataa rah gayaa vo khadaa hii khadaa bade man se vidhaataa ne threedots ', 'correct_label': 'c ramchandra', 'label': 2, 'split': 'test', 'title': 'shyaamal shyaamal baran', 'year': '1959'}`
- output: `{"pred": "s d burman", "top3": ["s d burman", "shankarjaikishan", "madan mohan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='s d burman' ref='c ramchandra'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='c ramchandra' in top3=['s d burman', 'shankarjaikishan', 'madan mohan']

### #308 — FAIL

- item: `{'lyrics': ' ye merii zindagii bejaan laash thii barason se pyaar ko terii talaash thii bas aaj merii khoyii taqadiir mil gayii terii tasaviir mil gayii threedots  ab ke bahaar men is intazaar men dil kaa vo haal thaa mushakil ye saal thaa diivaane ke liye ik zanjiir mil gayii terii tasaviir mil gayii threedots  tasaviir men magar ye kaun hai bataa is ko zaraa uthaa mujhako yahaan bithaa kyaa kaam is kaa raanjhe ko hiir mil gayii terii tasaviir mil gayii threedots  aayii hai tuut kar is par javaaniyaan bachapan kii hai magar saarii nishaaniyaan mere hasiin kvaabon kii taabiir mil gayii terii tasaviir mil gayii threedots', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'terii tasaviir mil gayii', 'year': '1980'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "c ramchandra", "s d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='r d burman' in top3=['laxmikantpyarelal', 'c ramchandra', 's d burman']

### #309 — PASS

- item: `{'lyrics': '   aag lagii tanman men dil ko padaa thaamanaa raam jaane kab hogaa sainyaan jii kaa saamanaa  2 ho  suunii hai aaj piyaa morii atariyaa piyaa morii atariyaa zaraa diijo kabariyaa dil tadape jaise binaa jal kii machhariyaa zaraa liijo kabariyaa suunii hai aaj piyaa morii atariyaa piyaa morii atariyaa dil tadape jaise binaa jal kii machhariyaa zaraa liijo kabariyaa aan pade mushqil to aaye koii kaam naa raam jaane kab hogaa sainyaan jii kaa saamanaa huun  saajan kii yaad mujhe pal pal sataaye mujhe pal pal sataaye dekho nainaa bhar aaye tan kaa singaar mere man ko na bhaaye dekho nainaa bhar aaye saajan kii yaad mujhe pal pal sataaye mujhe pal pal sataaye tan kaa singaar mere man ko na bhaaye dekho nainaa bhar aaye pyaar meraa ho jaaye kahiin badanaam naa raam jaane kab hogaa sainyaan jii kaa saamanaa haay  laagii naa chhuute karuun koii bahaanaa karuun koii bahaanaa aayaa naazuq zamaanaa dil meraa banaa piyaa teraa nishaanaa aayaa naazuq zamaanaa laagii naa chhuute karuun koii bahaanaa karuun koii bahaanaa dil meraa banaa piyaa teraa nishaanaa aayaa naazuq zamaanaa hoye buraa ulfat kaa dekho anjaam naa raam jaane kab hogaa sainyaan jii kaa saamanaa ', 'correct_label': 'naushad', 'label': 6, 'split': 'test', 'title': 'aag lagii tanman men dil ko padaa thaamanaa', 'year': '1952'}`
- output: `{"pred": "naushad", "top3": ["naushad", "c ramchandra", "madan mohan"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='naushad' ref='naushad'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='naushad' in top3=['naushad', 'c ramchandra', 'madan mohan']

### #310 — FAIL

- item: `{'lyrics': ' mere dil men aaj kyaa hai tuu kahe to main bataa duun terii zulf phir savaaruun terii maang phir sajaa duun mere dil men threedots  mujhe devataa banaakar terii chaahaton ne puujaa  2 meraa pyaar kah rahaa hai main tujhe khudaa banaa duun terii zulf phir threedots  koi dhuundhne bhii aae to hamen naa dhuundh paae  2 tuu mujhe kahiin chhupaa de main tujhe kahiin chhupaa duun terii zulf phir threedots  mere baazuon me aakar teraa dard chain paae  2 tere gesuon me chhupakar main jahaan ke gam bhulaa duun terii zulf phir threedots', 'correct_label': 'laxmikantpyarelal', 'label': 4, 'split': 'test', 'title': 'mere dil men aaj kyaa hai tuu kahe to main bataa duun', 'year': '1973'}`
- output: `{"pred": "madan mohan", "top3": ["madan mohan", "laxmikantpyarelal", "c ramchandra"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='madan mohan' ref='laxmikantpyarelal'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='laxmikantpyarelal' in top3=['madan mohan', 'laxmikantpyarelal', 'c ramchandra']

### #311 — PASS

- item: `{'lyrics': '  mu \ttum pyaar se dekho ham pyaar se dekhen \tjiivan ke andhere men bikhar jaae ujaalaa shaa \ttum pyaar se dekho threedots  mu \tham tum par jo bhaarii the vo din biit gae hain \tmatavaalii dagar pe jo mile miit nae hain shaa \tkushiyon kii lahar aur chaand jod gaii hai \tham pyaar karane vaalon kii duniyaa hii naii hai 2 mu \ttum pyaar se dekho shaa \tham pyaar se dekhen do \tjiivan ke andhere threedots ko \ttum pyaar se dekho threedots  mu \tphir aaj dhadakataa huaa dil bol rahaa hai \tphir se kahiin ud jaane ko par khol rahaa hai shaa \tnagarii javaan aramaanon kii ye premanagar hai \thar dil uchhal rahaa hai mohabbat kaa asar hai mu \ttum pyaar se dekho shaa \tham pyaar se dekhen do \tjiivan ke andhere threedots ko \ttum pyaar se dekho threedots ', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'tum pyaar se dekho ham pyaar se dekhen', 'year': '1968'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "laxmikantpyarelal", "kalyanjianandji"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='shankarjaikishan' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='shankarjaikishan' in top3=['shankarjaikishan', 'laxmikantpyarelal', 'kalyanjianandji']

### #312 — PASS

- item: `{'lyrics': '  o ho o ho ho ho ho o o ho ek aag hai dahakataa raag hai  jawaanii merii jawaanii merii jawaanii merii jal jaayenge agar paas aayenge jalaane waale  are re re re re re re re re haay re dil paaq hai nazar bebaaq hai dar kisakaa mujhe dar kisakaa mujhe dar kisakaa pachhataayenge agar takaraayenge zamaane waale ho  aa haay ek aag hai dahakataa raag hai  jawaanii merii jawaanii merii jawaanii merii jal jaayenge agar paas aayenge jalaane waale ho o ho ', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'ek aag hai dahakataa raag hai', 'year': '1951'}`
- output: `{"pred": "s d burman", "top3": ["s d burman", "c ramchandra", "r d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='s d burman' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='s d burman' in top3=['s d burman', 'c ramchandra', 'r d burman']

### #313 — PASS

- item: `{'lyrics': ' rag rag men is tarah tuu samaane lagaa jaise mujhii ko mujhase churaane lagaa o dil meraa le gayaa luut ke chorii chorii chupake chupake  rag rag men is tarah tuu samaane lagii jaise mujhii ko mujhase churaane lagii dil meraa le gaii luut ke chorii chorii chupake chupake  tuune dil ko dhadakanaa sikhaayaa sanam pyaar kyaa hai mujhe ye bataayaa sanam saari rasmon ko kasamon ko tod duun tuu kahe to ye duniyaa bhii main chhod duun ho ab na jaanaa kabhii ruuth ke chorii chorii chupake chupake threedots  maine sab kuchh tere pyaar ko de diyaa tujhape rab se bhii jyaadaa bharosaa kiyaa tujhako palakon men apanii sajaa ke rakhuun tere sapanon kaa motii chhupaa ke rakhuun main karuungii vafaa tuutake chorii chorii chupake chupake threedots ', 'correct_label': 'annu malik', 'label': 1, 'split': 'test', 'title': 'rag rag men is tarah  chorii chorii chupake chupake', 'year': '2000'}`
- output: `{"pred": "annu malik", "top3": ["annu malik", "s d burman", "c ramchandra"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='annu malik' ref='annu malik'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='annu malik' in top3=['annu malik', 's d burman', 'c ramchandra']

### #314 — FAIL

- item: `{'lyrics': '  pyaase nainon kii pyaas bujhaa le bholebhaale o raahii matavaale  main to kheton se hokar aaii re motii shabanam ke chunakar laaii re meraa mukhadaa phuhaar mere nayan kataar ik baar karejavaa pe khaa le pyaase nainon kii threedots  main to barakhaa kii alabelii raanii pyaase dil kii naa jaanuun kahaanii chal baadal ke paar leke man kaa sitaar koii giit kushii ke gaa le pyaase nainon kii threedots  main to nadiyaa kii ik lahariyaa morii sabase niraalii dagariyaa main huun jalatarang meraa goraa hai rang mere mukhade se nainaa hataa le pyaase nainon kii threedots ', 'correct_label': 'madan mohan', 'label': 5, 'split': 'test', 'title': 'pyaase nainon kii pyaas bujhaa le', 'year': '1956'}`
- output: `{"pred": "naushad", "top3": ["naushad", "s d burman", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='naushad' ref='madan mohan'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='madan mohan' in top3=['naushad', 's d burman', 'shankarjaikishan']

### #315 — PASS

- item: `{'lyrics': ' na shikawaa hai koii na koii gilaa hai na shikawaa hai koii na koii gilaa hai 2 salaamat rahe tuu ye merii duaa hai na shikawaa hai koii bahut hii kathin hain muhabbat kii raahen 2 zaraa bach ke chalanaa zamaanaa buraa hai na shikawaa hai koii  ajab terii mahafil men dekhaa tamaashaa kahiin roshanii hai kahiin hai andheraa 2 kahiin hai andheraa muqaddar chiraagon ke badale hue hain 2 koii bujh rahaa hai koii jal rahaa hai na shikawaa hai koii  mubaarak tujhe ho tere dil kii duniyaa merii zindagii kaa koii gam na karanaa 2 koii gam na karanaa ye sab gardishen hain nasiibon kii pyaare 2 na merii kataa hai na terii kataa hai na shikawaa hai koii ', 'correct_label': 'naushad', 'label': 6, 'split': 'test', 'title': 'na shikawaa hai koii', 'year': '1954'}`
- output: `{"pred": "naushad", "top3": ["naushad", "laxmikantpyarelal", "c ramchandra"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='naushad' ref='naushad'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='naushad' in top3=['naushad', 'laxmikantpyarelal', 'c ramchandra']

### #316 — PASS

- item: `{'lyrics': '  ku \the he he he he a \tla la la la la la aa aa aa aa \tchot dil pe lagii pyaar hone lagaa 2 \tvo ajanabii mere dil ko bhalaabhalaa saa lagaa 2 ku \tham diivaanon kii to ab yahii hai duaa 2 \tsaarii umar chaahaton kaa chalataa rahe silasilaa 2  a \tjab huaa saamanaa ham dil de baithen \tishq kii bekudii ham to le baithen \thaan jab huaa saamanaa threedots ham to le baithen ku \tpalakon ke piichhe se tuune kyaa kah daalaa \tdiivaanaa main banaa a \tvo meraa mastaanaa aashiq kuchh manachalaa saa lagaa ku \tsaarii umar chaahaton kaa chalataa rahe silasilaa a \t\tchot dil pe lagii pyaar hone lagaa \tvo ajanabii mere dil ko bhalaabhalaa saa lagaa ku \tsaarii umar chaahaton kaa chalataa rahe silasilaa  a \tniind men kvaab men chupake se aataa hai \thar ghadii vo meraa chain churaataa hai \thuun niind men kvaab men threedots chain churaataa hai ku \tbaanhon ke ghere men ab mujhako rahane de \tchhune de lab zaraa a \tye beqararii kaa mausam dhuaandhuaan saa lagaa ku \thaan saarii umar chaahaton kaa chalataa rahe silasilaa a \t\tchot dil pe lagii pyaar hone lagaa 2 \tvo ajanabii mere dil ko bhalaabhalaa saa lagaa ku \thaan saarii umar chaahaton kaa chalataa rahe silasilaa ', 'correct_label': 'annu malik', 'label': 1, 'split': 'test', 'title': 'chot dil pe lagii pyaar hone lagaa', 'year': '2003'}`
- output: `{"pred": "annu malik", "top3": ["annu malik", "r d burman", "kalyanjianandji"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='annu malik' ref='annu malik'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='annu malik' in top3=['annu malik', 'r d burman', 'kalyanjianandji']

### #317 — PASS

- item: `{'lyrics': ' spoken shukriyaa karam maharbaanii doston zindagii hasiin hai lekin sirf unake lie jinhon ne pyaar kiyaa hai kyonki sifr pyaar karane vaale jaanate hain ki aan baan aur shaan se jiinaa kise kahate hain hai na  aashaa pyaar karane vaale pyaar karate hain shaan se jiite hain shaan se marate hain shaan se  ho lete hain kisiikaa jo naam unako hazaaron salaam kabhii rukate nahiin kabhii jhukate nahiin chaahe jo bhii ho anjaam yaar kii galii se guzarate hain shaan se jiite hain shaan se marate hain shaan se  ho rastaa nahiin aasaan denaa padataa hai imtehaan ye hai dil kii lagii ye nahiin dillagii aate hain kaii tuufaan   ubharate hain shaan se jiite hain shaan se marate hain shaan se', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'pyaar karane vaale pyaar karate hain shaan se', 'year': '1980'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "annu malik", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='r d burman' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='r d burman' in top3=['r d burman', 'annu malik', 'laxmikantpyarelal']

### #318 — FAIL

- item: `{'lyrics': '  kah ke bhii na aaye tum ab chhupane lage taare dil le ke tumhiin jiite dil de ke hamiin haare  ham aas kiye jaate tum paas nahiin aate jaanaa thaa chale jaate milane to chale aate  kah ke bhii na aaye tum ab chhupane lage taare dil le ke tumhiin jiite dil de ke hamiin haare  hamane thaa tumhen maanaa tumane hii naa pahachaanaa jab honaa thaa begaanaa tab kyon kiyaa diiwaanaa  kah ke bhii na aaye tum ab chhupane lage taare dil le ke tumhiin jiite dil de ke hamiin haare  sunasaan huiin galiyaan sab suukh gaiin kaliyaan ab biit chaliin ghadiyaan par jaag rahiin ankhiyaan  kah ke bhii na aaye tum ab chhupane lage taare dil le ke tumhiin jiite dil de ke hamiin haare ', 'correct_label': 'c ramchandra', 'label': 2, 'split': 'test', 'title': 'kah ke bhii na aaye tum', 'year': '1946'}`
- output: `{"pred": "naushad", "top3": ["naushad", "c ramchandra", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='naushad' ref='c ramchandra'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='c ramchandra' in top3=['naushad', 'c ramchandra', 'shankarjaikishan']

### #319 — PASS

- item: `{'lyrics': ' lataa dil todane vaale tujhe dil dhuundh rahaa hai tujhe dil dhuundh rahaa hai aavaaz de tuu kaun sii nagarii men chhupaa hai dil todane vaale threedots  tuu ham ko jo mil jaae to haal apanaa sunaaen kud roen kabhii aur kabhii tujhe rulaaen vo daag dikhaaen jo hamen tuune diyaa hai  rafii ai dil ke sahaare tujhe dil dhuundh rahaa hai tujhe dil dhuundh rahaa hai siine men terii yaad kaa tuufaan uthaa hai ai dil ke sahaare  dil men to ye hasarat hai tere paas main aauun nazaron se giraa huun to nazar kaise milaauun nazar kaise milaauun badanaam huun naakaam huun kyaa mujh men rahaa hai ai dil ke sahaare tujhe dil dhuundh rahaa hai tujhe dil dhuundh rahaa hai  lataa dikhalaa ke kinaaraa mujhe mallaah ne luutaa kashtii bhii gaii haath se patavaar bhii chhuutaa patavaar bhii chhuutaa ab aur na jaane merii taqadiir men kyaa hai dil todane vaale tujhe dil dhuundh rahaa hai tujhe dil dhuundh rahaa hai  rafii bechain udhar tuu hai to majabuur idhar ham baithe hain chhupaae hue ashqon men teraa gam ashqon men teraa gam har chot ubhar aaii hai har zakm haraa hai  lataa dil todane vaale tujhe dil dhuundh rahaa hai tujhe dil dhuundh rahaa hai ', 'correct_label': 'naushad', 'label': 6, 'split': 'test', 'title': 'dil todane vaale tujhe dil dhuundh rahaa hai', 'year': '1962'}`
- output: `{"pred": "naushad", "top3": ["naushad", "madan mohan", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='naushad' ref='naushad'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='naushad' in top3=['naushad', 'madan mohan', 'shankarjaikishan']

### #320 — FAIL

- item: `{'lyrics': ' ra o aajaa panchhi akela hai  aa o so jaa nindiyaa ki bela hai   2 ra o aajaa panchhi akela hai   ra ud gai nind yahan mere nain se  aa bas karo yunhi pade raho chain se   2 ra laage re dar mohe laage re  aa o ye kya darane kii bela hai  ra o aajaa panchhi akela hai threedots  ra oho kitani ghuti si hai ye fizaa  aa aha kitani suhaani hai ye hava   2 ra mar gaye ham nikala dam mar gaye ham  aa mausam kitana alabela hai  ra o aajaa panchhi akela hai threedots  ra bin tere kaisii andheri ye raat hai  aa dil mera dhadakan merii tere sath hai   2 ra tanha hai phir bhi dil tanha hai  aa laagaa sapanon ka mela hai  ra o aajaa panchhi akela hai threedots', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'o aajaa panchhii akelaa hai', 'year': '-1'}`
- output: `{"pred": "madan mohan", "top3": ["madan mohan", "s d burman", "kalyanjianandji"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='madan mohan' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='s d burman' in top3=['madan mohan', 's d burman', 'kalyanjianandji']

### #321 — FAIL

- item: `{'lyrics': ' m0k0 kahiin na aisii subah dekhii la aaaa jaise baalak kii muskaan m0k0 yaa phir duur kahiin gaae la halkiisii muralii kii taan m0k0 gurabaanii gurudwaare men la to masjid se uthatii aazaan m0k0 la aatmaa aur paramaatmaa milen jahaan yahii hai wo sthaan  ko dholii dhol bajaanaa taal se taal milaanaa     dholii dholaa dholii dholaa dholii dhol bajaanaa     taathaa thaiyyaa taktak thaiyyaa taal se taal milaanaa  la puravaa suhaanii aaii re puravaa 2     rituon kii raanii aaii re puravaa     mere ruke nahiin paanv naach utthaa saaraa gaanv     priit pe jawaanii chhaaii re puravaa     puravaa suhaanii aaii re puravaa  m0k0 mausam kaa musaafir khadaa raste men la laa laa laa laalaa lalaa lalaa m0k0 mausam kaa musaafir khadaa raste men la usake haathon sab kuchh lutaa saste men la chhotii sii umariyaa hai ma0ka0 lambii sii dagariyaa re la jiivan hai parachhaanii re puravaa     puravaa suhaanii aaii re puravaa ko hoe dholii dhol bajaanaa bajaanaa     hoe taal se taal milaanaa milaanaa  la kar le kar bhii le pyaar kii puujaa     naa naa naa naanaa nanaa nanaa la kar le kar bhii le pyaar kii puujaa     pyaar ke rang pe chadhe na rang duujaa     chaahe koii sapanaa hai mere liye apanaa hai     baat merii ban aaii re     puravaa suhaanii aaii re puravaa  man ho miiraa sii diiwaanii re naache mastaanii 2 la honthon pe hai saragam to aankhon men paanii     ghungharuu diiwaane hue man rishte puraane hue la giit men kahaanii gaaii re puravaa     puravaa suhaanii aaii re puravaa     rituon kii raanii aaii re puravaa     mere ruke nahiin paanv naach uthaa saaraa gaanv     priit pe jawaanii chaaii re puravaa     puravaa suhaanii aaii re puravaa ko hoe dholii dhol bajaanaa bajaanaa     hoe taal se taal milaanaa milaanaa     dholii dhol bajaanaa taal se taal milaanaa 2 la o threedots', 'correct_label': 'kalyanjianandji', 'label': 3, 'split': 'test', 'title': 'puravaa suhaanii aayii re', 'year': '1970'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "kalyanjianandji", "r d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='kalyanjianandji'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='kalyanjianandji' in top3=['laxmikantpyarelal', 'kalyanjianandji', 'r d burman']

### #322 — FAIL

- item: `{'lyrics': '  he ham tum jiit gae dushman haar gae khule maidaan men ham baazii maar gae o ghungharuu naach uthe baaj uthe jhuumate ham  chha na na na na  4 ham tum jiit gae threedots  daulat nahiin kaam aaii chaahat ne jiitii ladaaii dhadakanon se duur rahe ham bade majabuur rahe apanaa sir na jhukaa hamane sahe laakh sitam is kushii ke bahaane tuu chhed mujhako diivaane pyaar men takaraar na kar ahaa aaj tuu o inkaar na kar 2 o ho aanchal chhod meraa dekhate hain logbaag chha na na na na threedots  chalatii hai tuu le ke thumake haayhaay hoyhoy thumake ke gaaen gazal tere jhumake o kaisaa beiimaan hai tuu phir bhii merii jaan hai tuu tere dam se merii zindagii hai terii qasam chha na na na na threedots ', 'correct_label': 'laxmikantpyarelal', 'label': 4, 'split': 'test', 'title': 'he ham tum jiit gae dushman haar gae', 'year': '1979'}`
- output: `{"pred": "s d burman", "top3": ["s d burman", "naushad", "kalyanjianandji"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='s d burman' ref='laxmikantpyarelal'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='laxmikantpyarelal' in top3=['s d burman', 'naushad', 'kalyanjianandji']

### #323 — PASS

- item: `{'lyrics': ' rangiilaarangiilaa angang hai rangiilaa dhakdhak dil naa dhadakaanaa  rasiilaarasiilaa angang hai rasiilaa dil deke dil naa tarasaanaa  mere dil kii mainaa mujhako karake diivaanaa  dhakdhak dil naa dhadakaanaa  jaan bhii merii hai terii ye shaan bhii merii hai terii  chahen jo bhii ho na chhoduungaa daaman o jaanaan  rangiilaarangiilaa ye rang hai rangiilaa dil deke dil naa tarasaanaa mere dil kii mainaa tuu karake diivaanaa dhakdhak dil naa dhadakaanaa  sun mere pyaare mohan main terii pyaasii  mujhako banaale apanii charanon kii daasii  ankhiyon men rahatii hain ye ankhiyaan tumhaarii  duniyaa men tere jaisii koii naa pyaarii  tere dil ke aangan men rahataa hai meraa man  tere hii kayaalon men rahataa hai meraa man  pyaariipyaarii baanhon men chhupataa hai meraa man  duubaa huaa hai haradam tujhamen hii meraa man  terii panaahon men rahataa hai meraa man  rangiilaarangiilaa ye rang hai rangiilaa dil deke dil naa tarasaanaa mere dil kii mainaa tuu karake diivaanaa dhakdhak dil naa dhadakaanaa jaan bhii merii hai terii ye shaan bhii merii hai terii chahen jo bhii ho na chhoduungii daaman o jaanaan  goregore chehare hazaaron yahaan hain  saanvare se kaise tuune ankhiyaan ladaaiin  teraa pyaar bhaayaa mujhako mere saanvariyaa  isiilie tumase mainne ankhiyaan ladaaiin  madiraa binaa aankhen kyuun laal hotii hain  mehandii binaa hathelii kyuun laal hotii hai  matavaalii ye aankhen madahosh karatii hain  tere binaa jiinaa bhii dushvaar hotaa hai  jabjab dekhuun tumhen bahut pyaar hotaa hai  rangiilaarangiilaa angang hai rangiilaa dhakdhak dil naa dhadakaanaa rasiilaarasiilaa angang hai rasiilaa dil deke dil naa tarasaanaa mere dil kii mainaa mujhako kar ke diiwaanaa dhakdhak dil naa dhadakaanaa jaan bhii merii hai terii ye shaan bhii merii hai terii chahen jo bhii ho na chhoduungaa daaman o jaanaan  rangiilaarangiilaa ye rang hai rangiilaa dil deke dil naa tarasaanaa mere dil kii mainaa tuu karake diivaanaa dhakdhak dil naa dhadakaanaa dhakdhak dil na dhadakaanaa 2 ', 'correct_label': 'a r rahman', 'label': 0, 'split': 'test', 'title': 'rangiilaarangiilaa angang hai rangiilaa', 'year': '2001'}`
- output: `{"pred": "a r rahman", "top3": ["a r rahman", "annu malik", "s d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='a r rahman' ref='a r rahman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='a r rahman' in top3=['a r rahman', 'annu malik', 's d burman']

### #324 — PASS

- item: `{'lyrics': ' aayaa naa karo gudiyaa mere paas dukh meraa sunake tum ho jaaogii udaas sthaayii  main to wo huun ki duniyaa men aaye hain jo aansuu piine ke liye meraa jiinaa kyaa jiinaa ki jiitii huun main yuun hii jiine ke liye sapanaa koii naa koii aas 1  mujhako mamataa kii pyaasii tumhaarii nazar kar detii hai beqaraar maan ke aanchal kaa saayaa main de na sakuun itanaa chaahuun baarbaar kuchh bhii nahiin hai mere paas 2', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'aayaa naa karo gudiyaa mere paas', 'year': '1979'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "kalyanjianandji", "s d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='r d burman' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='r d burman' in top3=['r d burman', 'kalyanjianandji', 's d burman']

### #325 — PASS

- item: `{'lyrics': ' \thamthreedots aathreedots chale gaye \tham bekhudii men tumako pukaare chale gaye\t \thamthreedots \tham bekhudii men tumako pukaare chale gaye         saagar men zindagi ko utaare chale gaye \thamthreedots \t \tdekhaa kiye tumhen ham banake diivaana  2 \tutaraa jo nashaa to hamane ye jaanaa \tsaare vo zindagi ke sahaare chale gaye \tham bekhudii men tumako pukaare chale gaye \thamthreedots \t \ttum to naa kaho ham khud hii se khele  2 \tduube nahiin ham hii yuun nashe men akele \tshiishe men aapako bhii utaare chale gaye \tham bekhudii men tumako pukaare chale gaye \tsaagar men zindagi ko utaare chale gaye \thamthreedots', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'ham bekhudii men tumako pukaare chale gae', 'year': '0'}`
- output: `{"pred": "s d burman", "top3": ["s d burman", "naushad", "a r rahman"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='s d burman' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='s d burman' in top3=['s d burman', 'naushad', 'a r rahman']

### #326 — PASS

- item: `{'lyrics': ' yaad aayii aadhii raat ko kal raat kii taubaa dil puuchhataa hai jhuum ke kis baat kii taubaa taubaa yaad aayii aadhii raat ko  chaahat men vafaa aur vo mar mitane kii qasamen kyaa baat hai bahake hue jazabaat kii taubaa taubaa yaad aayii aadhii raat ko  saaqi mujhe batalaa to de muunh pher ke mat hans piine men agar thiik to kis baat kii taubaa taubaa yaad aayii aadhii raat ko  marane bhii na denge mujhe dushaman merii jaan ke har baat pe kahate hain ki kis baat kii taubaa taubaa yaad aayii aadhii raat ko', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'yaad aayii aadhii raat ko', 'year': '1959'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "c ramchandra", "a r rahman"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='shankarjaikishan' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='shankarjaikishan' in top3=['shankarjaikishan', 'c ramchandra', 'a r rahman']

### #327 — FAIL

- item: `{'lyrics': ' jiivan se bharii terii aankhen majabuur kare jiine ke liye saagar bhii tarasate rahate hain tere ruup kaa ras piine ke liye jiivan se bharii terii aankhen threedots  tasviir banaaye kyaa koii kyaa koii likhe tujhape kavitaa rangon chhandon men samaaegii kis tarah se itanii sundarataa ek dhadakan hai tuu dil ke liye ek jaan hai tuu jiine ke liye jiivan se bharii terii aankhen threedots  madhuban ki sugandh hai saanson men baahon men kanval kii komalataa kiranon kaa tej hai chehare pe hiranon kii hai tujh men chanchalataa aanchal kaa tere ek taar bahut koi chhaak jigar siine ke liye jiivan se bharii terii aankhen threedots', 'correct_label': 'kalyanjianandji', 'label': 3, 'split': 'test', 'title': 'jiivan se bharii terii aankhen', 'year': '-1'}`
- output: `{"pred": "s d burman", "top3": ["s d burman", "r d burman", "kalyanjianandji"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='s d burman' ref='kalyanjianandji'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='kalyanjianandji' in top3=['s d burman', 'r d burman', 'kalyanjianandji']

### #328 — FAIL

- item: `{'lyrics': '    dhiith langar natakhat harajaaii tohe laaj na aae hoa ek to man kaa dhiiraj luute duuje jiyaa jalaae hoa dhiith langar hoa dhiith langar natakhat harajaaii tohe laaj na aae  aate jaate bainyaan pakade 2 roke baat hamaarii kankad maare gagariyaa phode 2 vaah re priit tihaarii nit nit kii ye raar kanhaaii ham se kahii na jaae hoa  dhiith langar natakhat harajaaii tohe laaj na aae  baansuriyaa kii ter sunaakar 2 hamako paas bulaae ham aaen to auron ke sang 2 hil mil raas rachaae bebas kaa man bas men karake chaturaaii dikhalaae hoa  dhiith langar natakhat harajaaii tohe laaj na aae hoa ek to man kaa dhiiraj luute duuje jiyaa jaalaae hoa dhiith langar hoa dhiith langar natakhat harajaaii tohe laaj na aae ', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'dhiith langar natakhat harajaaii', 'year': '1954'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "naushad", "s d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='s d burman' in top3=['laxmikantpyarelal', 'naushad', 's d burman']

### #329 — PASS

- item: `{'lyrics': ' ho tum se achchhaa kaun hai dil lo jigar lo jaan lo ham tumhare hain sanama tum hame pahachaana lo   2 \t main huun vo jhonkaa masta havaakaa sanga tumhaare chalataa rahuungaa jaba se huii hai tum se mohabbata milataa rahaa huun milataa rahuungaa   2 huthreedots tum se achchhaa kauna hai threedots \t siine men dila hai dila men tumhii ho tuma men hamaarii chhotii sii jaana hain tuma ho salaamata ham ko nahiin gama tum se hamaarii duniyaa javaana hain   2 huthreedots tum se achchhaa kauna hai threedots \t mara ke bhii dekhaa mar naa sake ham dilakii lagii ne hamako bachaayaa terii nazara kaa jaaduu hai shaayada jisane hame phira zindaa banaayaa huthreedots tum se achchhaa kauna hai threedots \t ho tum se achchhaa kaun hai dila lo jigara lo jaana lo ham tumhaare hain sanama tuma hame pahachaana lo', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'tum se achchhaa kaun hai dil lo jigar lo jaan lo', 'year': '1965'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "r d burman", "annu malik"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='shankarjaikishan' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='shankarjaikishan' in top3=['shankarjaikishan', 'r d burman', 'annu malik']

### #330 — FAIL

- item: `{'lyrics': '  duniyaa kyaa jaane meraa afasaanaa kyuun gaaye dil ulafat kaa taraanaa  2 duniyaa kyaa jaane  ho o o  niind na aaye dil bas men nahiin tuu hai kahiin to piyaa main huun kahiin  2 o saajanawaa re o baalamawaa re chaandanii raaten aur ye samaan rut bhii anokhii main bhii jawaan main bhii diiwaanii tuu bhii diiwaanaa phir kaise biite mausam suhaanaa  ho o   raat kate na bin tere piyaa aajaa akele nahiin laage jiyaa  2 o saajanawaa re o baalamawaa re jhilamil taare mast havaa chhed de muralii aa ke zaraa ho o tere sang gaauun main kyaa gaanaa sunsun ke jisako naache zamaanaa  duniyaa kyaa jaane meraa afasaanaa kyuun gaaye dil ulafat kaa taraanaa duniyaa kyaa jaane ', 'correct_label': 'naushad', 'label': 6, 'split': 'test', 'title': 'duniyaa kyaa jaane meraa afasaanaa', 'year': '1949'}`
- output: `{"pred": "s d burman", "top3": ["s d burman", "naushad", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='s d burman' ref='naushad'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='naushad' in top3=['s d burman', 'naushad', 'shankarjaikishan']

### #331 — FAIL

- item: `{'lyrics': ' ud gayaa bhanvaraa ud gayaa bhanvaraakalii udaas kalii udaaskalii udaas kyuun bhanvare ne priit lagaaiikaahe chhod gayaa harajaaii 2 lagii bujhii na thiiman kii pyaas ud gayaa bhanvaraa threedots  daal gale men sundar baahen  gaye dil men angaare2 chhod gaye mujhe sab kii paas ud gayaa bhanvaraa threedots  bujh gayaa diipak jalate jalateruk gaii naiyyaa chalate chalate2 ro ro pukaarii kisii pumaar  ud gayaa bhanvaraa threedots  bachane se pahale ujad gaii mainujad gaii mainujad gaii milake piyaa se bichhad gaii mainbichhad gaii mainbichhad gaii bichhade jaise phuulon se baag ud gayaa bhanvaraa threedots', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'ud gayaa bhanvaraa', 'year': '-1'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "madan mohan", "s d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='s d burman' in top3=['laxmikantpyarelal', 'madan mohan', 's d burman']

### #332 — FAIL

- item: `{'lyrics': ' lataa lukaachhupii bahut huii saamane aajaa naa kahaankahaan dhuundhaa tujhe thak gai hai ab terii maan aajaa saanjh huii mujhe terii fikar dhundhalaa gai dekh merii nazar aajaa naa  rahamaan kyaa bataauun maan kahaan huun main yahaan udane ko mere khulaa aasamaan hai tere qisson jaisaa bholaa  salonaa jahaan hai yahaan sapanon waalaa merii patang ho befikar ud rahii hai maan dor koii luute nahiin biich se kaate naa  lataa terii raah taken ankhiyaan jaane kaisaakaisaa hoye jiyaa dhiiredhiire aakar utare andheraa  teraa diip kahaan dhal ke suuraj kare ishaaraa chandaa tuu hai kahaan mere chandaa tuu hai kahaan  rahamaan kaise tujhako dikhaauun yahaan hai kyaa mainne jharane se paanii maan tod ke piyaa hai guchchhaaguchchhaa kaii kwaabon kaa uchhal ke chhuaa hai chhaayaa lie bhalii dhuup yahaan hai nayaanayaa saa hai ruup yahaan yahaan sab kuchh hai maan phir bhii lage bin tere mujhako akelaa', 'correct_label': 'a r rahman', 'label': 0, 'split': 'test', 'title': 'lukaachhupii bahut huii', 'year': '2006'}`
- output: `{"pred": "s d burman", "top3": ["s d burman", "a r rahman", "naushad"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='s d burman' ref='a r rahman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='a r rahman' in top3=['s d burman', 'a r rahman', 'naushad']

### #333 — FAIL

- item: `{'lyrics': ' khaaii hai re hamane qasam sang rahane kii aayegaa re udake meraa hans paradesii  pahalaa milan mose nahiin re sajan kaa rahegaa sadaa milanaa dharatii gagan kaa yug se vo hai meraa main usakii re khaaii  hai re hamane qasam sang rahane kii aayegaa re udake meraa hans paradesii  aise to nahiin usake rang men dhalii main piyaa ang lag lag ke bhaii saanvalii main mere tan pe chhaanv hai usii kii re khaaii  hai re hamane qasam sang rahane kii aayegaa re udake meraa hans paradesii meraa hans paradesii hun hun hun hun hun hun hun hun  hans paradesii ', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'khaaii  hai re hamane qasam', 'year': '1969'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "shankarjaikishan", "kalyanjianandji"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='r d burman' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='s d burman' in top3=['r d burman', 'shankarjaikishan', 'kalyanjianandji']

### #334 — FAIL

- item: `{'lyrics': ' chhotii sii kahaanii se baarishon kii paanii se saarii vaadii bhar gayii na jaane kyon dil bhar gayaa na jaane kyon aankh bhar gayii  rukatii hai chalatii hai kabhii barasatii hai baadal pe paanv rakh ke baarish machalatii hai aa aa la laa chhotii sii kahaanii se   threedots  shaakon pe patte the patton men buunde thiin buundon men paanii thaa paanii men aansuu thaa aa aa la laa chhotii sii kahaanii se   threedots  pahale mile bhii the dil men gile bhii the mil ke paraaye the do hamsaaye the aa aa la laa chhotii sii kahaanii se   threedots', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'chhotii sii kahaanii se baarishon kii paanii se', 'year': '-1'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "c ramchandra", "r d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='shankarjaikishan' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='r d burman' in top3=['shankarjaikishan', 'c ramchandra', 'r d burman']

### #335 — FAIL

- item: `{'lyrics': ' iid aaii meraa yaar nii aayaa 2  tainuun vekhane daa jaa paayaa ve sajanaa   iid aaii meraa yaar nii aayaa  kar thaiyaa thaiyaa thaiyaa thaiyaa 2  thaiyaa thaiyaa thaiyaa thaiyaa kar thaiyaa thaiyaa thaiyaa thaiyaa  thaiyaa thaiyaa thaiyaa thaiyaa kar thaiyaa thaiyaa thaiyaa 2  ho  tere ishq nachaayaa kar thaiyaa thaiyaa tere ishq nachaayaa kar thaiyaa 2  thaiyaa thaiyaa thaiyaa thaiyaa kar thaiyaa thaiyaa thaiyaa  kar thaiyaa thaiyaa thaiyaa thaiyaa kar thaiyaa thaiyaa thaiyaa thaiyaa    ishq deraa mere andar kiitaa par ke prempayaalaa piitaa   aajaa sajanaa aajaa sajanaa naii te main mar gaiyaan gaiyaan   kar thaiyaa thaiyaa thaiyaa thaiyaa kar thaiyaa thaiyaa thaiyaa  kar thaiyaa thaiyaa thaiyaa thaiyaa thaiyaa thaiyaa thaiyaa thaiyaa   ishq deraa mere andar kiitaa parake prem payaalaa piitaa  aajaa sajanaa aajaa sajanaa naii te main mar gaiyaan gaiyaan   kar thaiyaa thaiyaa thaiyaa thaiyaa kar thaiyaa thaiyaa thaiyaa  kar thaiyaa thaiyaa thaiyaa thaiyaa thaiyaa thaiyaa thaiyaa thaiyaa    merii nazaron men mere nainon men merii zulfon men mere baalon men   bas pyaar tere dii laganlagan bas aganagan bas agan   merii dhadakan men mere dil men mere jism men mere siine men   bas pyaar tere dii laganlagan bas aganagan bas agan  ishq deraa mere andar kiitaa par ke prempayaalaa piitaa  aajaa sajanaa aajaa sajanaa naii te main mar gaiyaan gaiyaan  tere ishq nachaayaa kar thaiyaa thaiyaa tere ishq nachaayaa kar thaiyaa 2  kar thaiyaa thaiyaa thaiyaa thaiyaa kar thaiyaa thaiyaa thaiyaa thaiyaa thaiyaa thaiyaa thaiyaa thaiyaa kar thaiyaa thaiyaa thaiyaa thaiyaa  4 ', 'correct_label': 'a r rahman', 'label': 0, 'split': 'test', 'title': 'iid aaii meraa yaar nii aayaa  kar thaiyaa thaiyaa', 'year': '1998'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "kalyanjianandji", "madan mohan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='a r rahman'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='a r rahman' in top3=['laxmikantpyarelal', 'kalyanjianandji', 'madan mohan']

### #336 — FAIL

- item: `{'lyrics': ' koras o la la laa a o la la laa a o o o la laa  giitaa suno gajar kyaa gaae samay guzarataa jaae o re jiine vaale o re bhole bhaale sonaa naa khonaa naa  koras suno gajar kyaa gaae samay guzarataa jaae o la la laa a o la la laa a o o o la laa  giitaa ginechune pal hain tere jiivan ke dhuum machaa le abhii din hain milan ke o re jiine vaale threedots koras suno gajar kyaa gaae samay guzarataa jaae  giitaa o re jiine vaale o re bhole bhaale sonaa naa khonaa naa koras o la la laa a o la la laa a o o o la laa giitaa husn bhii faanii aur ishq bhii faanii hai hans ke bitaa le do ghadii kii javaanii hai o re jiine vaale threedots  giitaa bichhadaa zamaanaa kabhii haath naa aaegaa dosh naa denaa mujhe phir pachhataaegaa o re jiine vaale threedots  koras suno gajar kyaa gaae giitaa sonaa naa koras samay guzarataa jaae giitaa khonaa naa', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'suno gajar kyaa gaae samay guzarataa jaae', 'year': '1951'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "kalyanjianandji", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='r d burman' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='s d burman' in top3=['r d burman', 'kalyanjianandji', 'laxmikantpyarelal']

### #337 — PASS

- item: `{'lyrics': '     ko \tek do tiin chaar pachaakaa chikaa chhum 4  sha \truup kii dushman paapii duniyaa maare mohe akhiyaan \tho main kyaa jaanuun raam \tmain kyaa jaanuun raam kisii ke lobhii man kii batiyaan \t maare akhiyaan ko \tpachaakaa chikaa chhum  2  sha \tek ruup ke laakh pujaarii gore kaale halake bhaarii \tkisii ko kyaa maaluum ladii hai kis baalam se aankh hamaarii \tladii hai kis baalam se aankh e jii hamase sha \tnahiin nahiin nahiin nahiin inase \tlambii naak hai inakii aankhon pe tishamaa sawaar hai kaa hamase sha \tare nahiin nahiin nahiin nahiin inase \tsuukhe gaal hain inake suurat bhii kaalaa bukhaar hai \tsuurat bhii kaalaa bukhaar hai o jii gorii hamase oh ho sha \tare chhii chhii chhii  \tmain kyaa jaanuun raam kisii ke lobhii man kii batiyaan \tmaare akhiyaan ko \tpachaakaa chikaa chhum sha \tmaare akhiyaan \truup kii dushman paapii duniyaa maare mohe akhiyaan \tho main kyaa jaanuun raam  sha \tchhailchhabiilaa hai baankaa baalam ho \tbanii huun main jinakii diiwaanii \tpiyaa hii jaane bhed jiyaa kaa \tkisako sunaauun pyaar kii baanii kisako sunaauun main ajii hamako sha \tnahiin nahiin nahiin nahiin unako \tbhengii aankh hai jinakii muuchhon par chhaaii bahaar hai kaa hamako sha \tare nahiin nahiin nahiin nahiin are unako \tmukhadaa chaand hai jinakaa nainon men jinake kumaar hai \tnainon men jinake kumaar hai kaun wo sipahiyaa aur ham sha \tare jaa jaa jaa \t \tmain kyaa jaanuun raam kisii ke lobhii man kii batiyaan \tmaare akhiyaan ko \tpachaakaa chikaa chhum sha \tmaare akhiyaan \truup kii dushman paapii duniyaa maare mohe akhiyaan \tho main kyaa jaanuun raam ', 'correct_label': 'naushad', 'label': 6, 'split': 'test', 'title': 'ek do tiin chaar  ruup kii dushman paapii duniyaa', 'year': '1951'}`
- output: `{"pred": "naushad", "top3": ["naushad", "s d burman", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='naushad' ref='naushad'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='naushad' in top3=['naushad', 's d burman', 'laxmikantpyarelal']

### #338 — FAIL

- item: `{'lyrics': ' vo hai zindaa josh men jo aae chaand ko bhii vo zamiin pe laae vo bhanvar men jo kabhii ghir jaae ek din kaa aadamii ban jaae ye abhii jiitaa nahiin hai yaaron main abhii haaraa nahiin huun yaaron jiinaa kyaa jiivan se haar ke jiinaa kyaa threedots  jo har saans jii gayaa marane kaa usako gam nahiin kahatii hai dharaa kahataa hai gagan kahataa hai ye man jisamen hai lagan dil tuutanen pe bhii nagamen gaaen pyaar ke jiinaa kyaa threedots  kaalii ghanerii raat men chaandanii khil jaaegii tujhe andheron men kahiin roshanii mil jaaegii rahataa nahiin saarii umar saathii ye gardish kaa khabar detii hai manzil kaa pataa kaanton bharii mushkil dagar hogaa kal kyaa sochanaa jo bhii hai bas aaj hai kab kahaan jaae badal vaqt kaa ye mizaaj hai kyaa hai sukh aur duhkh hai kyaa chaar din kii baat hai dard men aaraam hai aansuu hansii ke saath hai jiinaa kyaa threedots ', 'correct_label': 'annu malik', 'label': 1, 'split': 'test', 'title': 'vo hai zindaa  jiinaa kyaa jiivan se haar ke', 'year': '2002'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "annu malik", "r d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='shankarjaikishan' ref='annu malik'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='annu malik' in top3=['shankarjaikishan', 'annu malik', 'r d burman']

### #339 — FAIL

- item: `{'lyrics': ' chi vo ham se chup hain ham unase chup hain   l manaane vale manaa rahen hain  chi vo ham se chup hain ham unase chup hain  l manaane vale manaa rahen hain    chi nigaahen uth uthake jhuk rahi hain  2 l maze muhabbat ke aa rahen hain  dono vo ham se chup hain threedots  chi ye jhuuthi aahen ye jhuuthe aansuu  2 jhalak rahen hain jo har palak men  l bataa rahen hain  bataa rahen hain ke tuute dil do  hazaaron sadame uthaa rahen hain  dono maze muhabbat ke aa rahen hain  vo hamase chup hain threedots   l ghadii men bigade ghadii men jhagade  2 hain baithe phir bhi aisi ada se aisi ada se  chi dabaa ke apane honthon ko dono  hansii ko apanii chhipaa rahen   dono  maze muhabbat ke aa rahen hain  vo hamase chup hain threedots', 'correct_label': 'c ramchandra', 'label': 2, 'split': 'test', 'title': 'vo ham se chup hain ham un se chup hain manaane vale manaa rahen hain', 'year': '1950'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "madan mohan", "c ramchandra"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='c ramchandra'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='c ramchandra' in top3=['laxmikantpyarelal', 'madan mohan', 'c ramchandra']

### #340 — PASS

- item: `{'lyrics': ' chandaa kii chaandanii kaa jaaduu ye raat ye samaa ulfat kii mauj le chalii hai mujhako na jaane kahaan  puuchho na hai mere dil men kyaa jo mere saath ho tum apanaa bhii main pataa kyaa jaanuun huun main to pyaar men gum dil pe nahiin hai aaj qaabuu khulatii nahiin zubaan ulfat kii mauj le chalii hai mujhako na jaane kahaan chandaa kii chaandanii kaa jaaduu   main nadiyaa tuu meraa saagar hai o man ke miit mere jhuume jaa tuu yuun hii laharon men sun sunake giit mere bhiigii ye raat aur main tuu mausam javaan javaan ulfat kii mauj le chalii hai mujhako na jaane kahaan chandaa kii chaandanii kaa jaaduu  ', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'chandaa kii chaandanii kaa jaaduu', 'year': '1958'}`
- output: `{"pred": "s d burman", "top3": ["s d burman", "naushad", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='s d burman' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='s d burman' in top3=['s d burman', 'naushad', 'shankarjaikishan']

### #341 — FAIL

- item: `{'lyrics': '     o ho aa  dupattaa meraa malamal kaa rang saletii halakaa haa \tdupattaa meraa malamal kaa rang saletii halakaa gii \tzamaanaa lut jaayegaa oy sar se agar dhalakaa 2  aa \tbatan mere kurte ke haay chanave \tbatan mere kurte ke sitaare aasamaanii sajanaa gii  hoy isii liye dekhaa naa andheraa kabhii tere anganaa 2  aa  o tumasaa bhii koii naa haay chanave \to tumasaa bhii koii naa zamaane men nidar hogaa gii \twahiin pe dam todenge jahaan pe teraa dar hogaa \thaay wahiin pe dam todenge jahaan pe teraa dar hogaa  aa \tdupattaa meraa malamal kaa rang saletii halakaa gii \tzamaanaa lut jaayegaa o sar se agar dhalakaa 2 ', 'correct_label': 'madan mohan', 'label': 5, 'split': 'test', 'title': 'dupattaa meraa malamal kaa rang saletii halakaa', 'year': '1958'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "s d burman", "naushad"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='shankarjaikishan' ref='madan mohan'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='madan mohan' in top3=['shankarjaikishan', 's d burman', 'naushad']

### #342 — FAIL

- item: `{'lyrics': ' buundaniyaan barasana laagii re kaahe shor machaaye re papiiharaa buundaniyaan barasana laagii re  dhun aisii gaaye man agan lagaaye tan tharak tharak rah jaaye soye dard jagaaye bairii baaz na aaye haay kaun ise samajhaaye buundaniyaan barasana laagii re  pa ga ma re saa re ni saa re saa saa re ni saa re ga ga ma re saa pa ma dha ni saa ni pa ni ma pa ga ma re sa re ni sa re ga ga ma re ni saa  tore paiyaan paduun main o papiiharaa jaa re jaa re jalaa na moraa jiyaraa tohe taras na aaye kaahe raar machaaye  jale aap mujhe bhii jalaaye buundaniyaan barasana laagii re', 'correct_label': 'madan mohan', 'label': 5, 'split': 'test', 'title': 'buundaniyaan barasana laagii re', 'year': '1958'}`
- output: `{"pred": "s d burman", "top3": ["s d burman", "c ramchandra", "a r rahman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='s d burman' ref='madan mohan'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='madan mohan' in top3=['s d burman', 'c ramchandra', 'a r rahman']

### #343 — FAIL

- item: `{'lyrics': ' man re tuu hii bataa kyaa gaauun kah duun apane dil ke dukhade yaa aansuu pii jaauun  jis ne barabas baandh liyaa hai is pinjare men qaid kiyaa hai kab tak main us patthar dil kaa jii bahalaatii jaauun man re three dots  neend men jab ye jag sotaa hai main rotii huun dil rotaa hai mukh pe jhoothii muskaanon ke kab tak rang chadhaauun man re three dots', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'man re tuu hii bataa kyaa gaauun', 'year': '1963'}`
- output: `{"pred": "s d burman", "top3": ["s d burman", "c ramchandra", "a r rahman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='s d burman' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='shankarjaikishan' in top3=['s d burman', 'c ramchandra', 'a r rahman']

### #344 — FAIL

- item: `{'lyrics': ' hain sabase madhur vo git jinhen ham dadr ke sur men gate hain  jab had se guzar jati hai khushi ansu bhi chhalakate aate hain  hain sabase madhur vo git  pahalu men paraaye dard basake hansana hansana sikh zaraa  tu hansana hansaana sikh zaraa   2 tufan se kah de ghir ke uthe ham pyaar ke dip jalaate hain  ham pyaar ke dip jalaate hain hain sabase madhur vo git threedots  kanton men khile hain phul hamaare rang bhare aramanon ke  rang bhare aramaanon ke   2 nadan hain jo in kanton se daaman ko bachaaye jaate hain  daaman ko bachaaye jaate hain hain sabase madhur vo git threedots  jab gam ka andhera ghir aaye samajho ke savera dur nahiin  samajho ke savera dur nahin   2 har rat ki hai saugat yahi tare bhi yahi doharate hain tare bhi yahi doharate hain hain sabase madhur vo git threedots', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'hain sabase madhur vo giit jinhen ham dard ke sur men gaate hain', 'year': '0'}`
- output: `{"pred": "naushad", "top3": ["naushad", "laxmikantpyarelal", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='naushad' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='shankarjaikishan' in top3=['naushad', 'laxmikantpyarelal', 'shankarjaikishan']

### #345 — FAIL

- item: `{'lyrics': '  hansii hansii na rahii aur kushii kushii na rahii main zindagii jise samajhuun vo zindagii na rahii  jiyuun to kisake lie aur maruun to kisake lie jo ek aas bandhii thii vo aas hii na rahii  kuchh aa ke gam ke andhere ne aisaa gher liyaa chiraag jalate rahe aur roshanii na rahii  andherii raat hai ab aur bujhaa saa dil kaa diyaa jo chaar din ke lie thii vo chaandanii na rahii hansii hansii na rahii threedots ', 'correct_label': 'c ramchandra', 'label': 2, 'split': 'test', 'title': 'hansii hansii na rahii aur kushii kushii na rahii', 'year': '1949'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "madan mohan", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='shankarjaikishan' ref='c ramchandra'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='c ramchandra' in top3=['shankarjaikishan', 'madan mohan', 'laxmikantpyarelal']

### #346 — FAIL

- item: `{'lyrics': ' r  chal shuruu hojaa  ki  uhun uhun khaansataa hai hai haa hai haa galaa thiik karataa hai  saa aa a aa aa aa  r  are  bas bas bas bas  saa pe ruk gayaa  aage badh  ki  re r  re ke aage kya hai  ki  gaa r  are vaah vaah vaah vaah kya gale men taasiir hai ki  ye baat hai  to maa r  chal vaapas aajaa apanii jagah pe  ki  saa re gaa maa  r  aahaa  ki  maa saa re gaa r  vaah vaah  ki  gaa saa re maa  r  oho  ki  maa gaa re saa  r  oh oh oh   ki  saa re gaa maa maa saa re gaa gaa saa re maa maa gaa re saa  r  pa dha pa maa maa pa maa ga ra pa maa maa ga re saa  dono  saa re gaa maa maa saa re gaa gaa saa re maa maa gaa re saa   ki  giit pahale bana tha ya banii thi ye saragam  ek hii saath hua tha do dilon ka ye sangam   2 r  pyaar ka ye taraanaa zamaanaa sun le  saa re gaa maa  dono  saa re gaa maa maa saa re gaa gaa saa re maa maa gaa re saa   ki  jaise dil milaten hain vaise sur khilaten hain dhiime  jaise dil milaten hain vaise sur khilaten hain tej  r  phuul kab giiton ke honthon pe khilaten hain  ki  tuum tanaanaa dhin tanaanaa zamaanaa sun le  r  saa re gaa maa  ki  saa re gaa maa  r  maa saa re gaa ki  gaa saa re maa  r  maa gaa re saa   dono  maa gaa re saa at least 56 times from loud to slow ', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'saa re gaa maa maa saa re gaa gaa saa re maa maa gaa re saa', 'year': '1975'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "s d burman", "a r rahman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='s d burman' in top3=['laxmikantpyarelal', 's d burman', 'a r rahman']

### #347 — PASS

- item: `{'lyrics': ' gariibon par jo hotii hain jafaaen kaun sunataa hai zamaane  men dukhe dil kii sadaaen  kaun sunataa hai   gam kaa fasaanaa kisako sunaaen tuutaa huaa dil kaise dikhaaen  teraa bhalaa ho tadapaane vaale dil de rahaa hai tujhako duaaen gam kaa fasaanaa threedots  hansatii hai qisamat kahatii hai duniyaa aapas men do dil milane naa paaen gam kaa fasaanaa threedots  tujhako qasam hai aise me aa jaa phir ye zamaane shaayad naa aaen gam kaa fasaanaa threedots', 'correct_label': 'naushad', 'label': 6, 'split': 'test', 'title': 'gariibon par jo hotii hain  gam kaa fasaanaa kisako sunaaen', 'year': '1948'}`
- output: `{"pred": "naushad", "top3": ["naushad", "c ramchandra", "s d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='naushad' ref='naushad'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='naushad' in top3=['naushad', 'c ramchandra', 's d burman']

### #348 — FAIL

- item: `{'lyrics': '  sanam raah bhuule yahaan aateaate 2 bhalaa rah gae vo kahaan aateaate sanam raah bhuule threedots  dil kii baaten to chhupii sii rahatii hain 2 vo kyaa jaane jo nigaahen kahatii hain unhen aaegii ye zubaan aateaate sanam raah bhuule threedots  rotii aankhon ko hansaanaa mushkil hai 2 is bechainii ko chhupaanaa mushkil hai na len vo meraa imtihaan aateaate sanam raah bhuule threedots  mujhase jhuuthii vo qasam naa khaaenge 2 unakaa vaadaa hai yahaan vo aaenge magar jaaegii merii jaan aateaate sanam raah bhuule threedots ', 'correct_label': 'laxmikantpyarelal', 'label': 4, 'split': 'test', 'title': 'sanam raah bhuule yahaan aateaate', 'year': '1965'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "kalyanjianandji", "annu malik"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='shankarjaikishan' ref='laxmikantpyarelal'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='laxmikantpyarelal' in top3=['shankarjaikishan', 'kalyanjianandji', 'annu malik']

### #349 — FAIL

- item: `{'lyrics': ' jalate hain jisake liye terii aankhon ke diye dhuundh laayaa huun vahii giit main tere liye jalate hain jisake liye  dard banake jo mere dil men rahaa dhal naa sakaa jaaduu banake terii aankhon men rukaa chal naa sakaa aaj laayaa huun vahii giit main tere liye jalate hain jisake liye  dil men rakh lenaa ise haathon se ye chhuute na kahiin giit naazuk hai meraa shiishe se bhii tuute na kahiin gunagunaauungaa yahii giit main tere liye jalate hain jisake liye  jab talak naa ye tere ras ke bhare honthon se mile yuun hii aavaaraa phiregaa ye terii zulfon ke tale gaaye jaauungaa yahii giit main tere liye jalate hain jisake liye', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'jalate hain jis ke liye terii aankhon ke diye', 'year': '-1'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "madan mohan", "s d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='r d burman' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='s d burman' in top3=['r d burman', 'madan mohan', 's d burman']

### #350 — FAIL

- item: `{'lyrics': ' aashaa \thaal kaisaa hai janaab kaa kishor         kyaa khayaal hai aap kaa  aashaa \ttum to machal gaye ho ho ho kishor \tyuunhii fisal gaye haa haa haa yodell   kishor \tbahakii bahakii chale hai pavan jo ude hai teraa aanchal aashaa \tchhodo chhodo dekho dekho gore gore kaale kaale baadal kishor \tkabhii kuchh kahatii hai kabhii kuchh kahatii hai  \t\t     zaraa nazar ko sanbhaalanaa aashaa \thaal kaisaa hai janaab kaa kishor         haay kyaa khayaal hai aap kaa  aashaa \thoy tum to machal gaye ho ho ho kishor \thmm hmm yuunhii fisal gaye haa haa haa yodell   kishor \tpagalii aashaa \ta kishor \tpagalii kabhii tuune sochaa raste men gaye mil kyon aashaa \tpagale kishor \than aashaa \tpagale kishor \te aashaa \tterii baaton baaton men dhadakataa hai dil kyon  kishor \tkabhii kuchh kahatii hai kabhii kuchh kahatii hai \t\t     zaraa nazar ko sanbhaalanaa aashaa \taa aa haal kaisaa hai janaab kaa kishor         haay kyaa khayaal hai aap kaa aashaa \ttum to machal gaye ho ho ho kishor \tyuunhii fisal gaye haa haa haa yodell  aashaa \tkaho jii kaho jii roz tere sang yuunhii  \t     \tdil bahalaayen kyaa kishor \taha suno jii suno jii samajh sako to khud samajho \t\tbataaen kyaa  \t\t     kabhii kuchh kahatii hai kabhii kuchh kahatii hai \t\t     zaraa nazar ko sambhaalanaa  \t aashaa \thaay haal kaisaa hai janaab kaa  kishor         kyaa khayaal hai aap kaa  aashaa \ttum to machal gaye ho ho ho kishor \tyuunhii fisal gaye haa haa haa  \t', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'haal kaisaa hai janaab kaa kyaa khayaal hai aap kaa', 'year': '1958'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "s d burman", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='r d burman' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='s d burman' in top3=['r d burman', 's d burman', 'shankarjaikishan']

### #351 — FAIL

- item: `{'lyrics': '   talat tum apanii yaad bhii dil se bhulaa jaate to achchhaa thaa lataa ye do aansuu lagii dil kii bujhaa jaate to achchhaa thaa   talat mere aramaan bhii le jaate merii hasarat bhii le jaate 2 nazar se chiin kar apanii hasiin suurat bhii le jaate andhere aur in aankhon men chhaa jaate to achchhaa thaa tum apanii yaad bhii  threedots  lataa mere dil kii muhabbat kaa yaqiin kab tum ko aayaa thaa 2 jahaan sau zulm dhaaye the jahaan dil ko mitaayaa thaa mujhe bhii apane haathon se mitaa jaate to achchhaa thaa ye do aansuu lagii dil kii  threedots   talat meraa dil pher de merii nishaanii pherane vaale 2 lataa jo mumakin ho to lautaa do merii aahen mere naale 2 ham apane dil kaa khoyaa chain paa jaate to achchhaa thaa ye do aansuu lagii dil kii  threedots  ', 'correct_label': 'c ramchandra', 'label': 2, 'split': 'test', 'title': 'tum apanii yaad bhii dil se', 'year': '1955'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "c ramchandra", "madan mohan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='shankarjaikishan' ref='c ramchandra'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='c ramchandra' in top3=['shankarjaikishan', 'c ramchandra', 'madan mohan']

### #352 — FAIL

- item: `{'lyrics': ' sochsamajhakar dil ko lagaanaa dekho buraa hai zamaanaa bholii suurat kaa dhokhaa na khaanaa dekho buraa hai zamaanaa sochsamajhakar dil ko lagaanaa dekho buraa hai zamaanaa dhokhaa na khaanaa dhokhaa na khaanaa dhokhaa na khaanaa naa naa naa naa naa  pyaar kii galii men dilavaalo jaanaa zaraa sanbhalsanbhalake phirate hain chorlutere raste men bhes badalake dhokhaa na khaanaa jii dhokhaa na khaanaa dekho buraa hai zamaanaa sochsamajhakar dil ko lagaanaa dekho buraa hai zamaanaa dhokhaa na khaanaa dhokhaa na khaanaa dhokhaa na khaanaa naa naa naa naa naa  duniyaa ke is baazaar men tan kii hai man kii pyaas nahiin husn ke is gulazaar men rang hii rang hai baas nahiin dhokhaa na khaanaa jii dhokhaa na khaanaa dekho buraa hai zamaanaa sochsamajhakar dil ko lagaanaa dekho buraa hai zamaanaa dhokhaa na khaanaa dhokhaa na khaanaa dhokhaa na khaanaa naa naa naa naa naa  priit hai kaanch kii chuudii thes lagii aur chuur huii shart vafaa kii is jag men kisako bhalaa manzuur huii dhokhaa na khaanaa jii dhokhaa na khaanaa dekho buraa hai zamaanaa sochsamajhakar dil ko lagaanaa dekho buraa hai zamaanaa bholii suurat kaa dhokhaa na khaanaa dekho buraa hai zamaanaa', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'sochsamajhakar dil ko lagaanaa', 'year': '1952'}`
- output: `{"pred": "naushad", "top3": ["naushad", "c ramchandra", "s d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='naushad' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='s d burman' in top3=['naushad', 'c ramchandra', 's d burman']

### #353 — FAIL

- item: `{'lyrics': '  ki \tdekh ke tumako dil dolaa hai \tgod promise ham sach bolaa hai \to hamako tumase ho gayaa hai pyaar kyaa karen \tbolo to jien bolo to mar jaaen 2 la \to hamako tumase threedots  ki \tkabhii boluun main kabhii bole tuu i love you la \tlove you \tmaine tumape tumane mujh pe kar diyaa jaaduu  \ti love you ki \tlove you ki \tab tak chhupaae rakhaa sholaa dabaae rakhaa aa \tab tak chhupaae threedots ki \traaz ye hamane ab kholaa hai \tgod promise ham threedots \to hamako tumase threedots do \thamako tumase threedots  la \tkaise main boluun tere sang main doluun mu \ttere sang jiivan kii dor bandhii hai \tmain sapanon kaa saagar tuu prem nadii hai \tab tak chhupaae threedots aa \tab tak chhupaae threedots mu \tchaandchakorii jyuun duniyaa men \traam qasam tuu rahe jiyaa men \thamako tumase threedots do \tbolo to jien threedots \thamako tumase threedots  ra \tdil men dilabar tuu rahataa hai \tkudaa gavaah ham sach kahataa hai \thamako tumase threedots  \tek to akabar kaa salaam usamen shaamil teraa naam \tdo lafzon men kahataa huun mukh se kissaa tamaam \tmain shaayar huun meraa hai vaastaa hasiinon se \tterii furqat men soyaa nahiin mahiinon se la \tnahiin karate ye baaten paradaanashiinon se \tsarebaazaar chhodo chhed mahazabiinon se ra \tab tak chhupaae threedots aa \tab tak chhupaae threedots ra \thusn hameshaa ruuthaa rahataa hai \tkudaa gavaah ham threedots ', 'correct_label': 'laxmikantpyarelal', 'label': 4, 'split': 'test', 'title': 'dekh ke tumako  o hamako tumase ho gayaa hai pyaar', 'year': '1977'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "laxmikantpyarelal", "kalyanjianandji"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='r d burman' ref='laxmikantpyarelal'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='laxmikantpyarelal' in top3=['r d burman', 'laxmikantpyarelal', 'kalyanjianandji']

### #354 — PASS

- item: `{'lyrics': '  o jaane vaale jaao na ghar apanaa chhod ke maataa bulaa rahii hai tumhen haath jod ke  ham sabako chhodakar ab jaate ho tum kahaan ujadii hai laakh phir bhii hai dharatii tumhaarii maan duniyaa men sukh na paaoge dil maan kaa tod ke o jaane vaalon threedots  thaharo pukaaratii hai tumhaarii zamiin tumhen laut aao maan kii haay lage naa kahiin tumhen ruk jaao maan kii haay lage naa kahiin tumhen ', 'correct_label': 'naushad', 'label': 6, 'split': 'test', 'title': 'o jaane vaale jaao na ghar apanaa chhod ke', 'year': '1957'}`
- output: `{"pred": "naushad", "top3": ["naushad", "shankarjaikishan", "s d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='naushad' ref='naushad'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='naushad' in top3=['naushad', 'shankarjaikishan', 's d burman']

### #355 — FAIL

- item: `{'lyrics': ' bhuul ho gayii jaane de sajanaa mar jaauungii maan jaa maan jaa maan jaa   threedots  sazaa de in aankhon ko ki ye hai kataa inakii kaahe na pahachaanaa tujhe  cho chhod gussaa jaane de sajanaa mar jaauungii maan jaa maan jaa maan jaa   threedots  tujhe main na chaahuungii to kaise na chaahuungii main to diivaanii yaar kii gile jo bhii hain dil ke mitaa le gale mil ke tujh ko qasam hai pyaar kii are maan bhii ja ab jaane de sajanaa mar jaauungii maan jaa maan jaa maan jaa   threedots  haan chalo maaf karataa huun kahaa to kahaa tumane aage na kahanaa phir kabhii chalaa jaauungaa varanaa kahiin tum se itanii duur dhuundhogii saarii zindagii ho aur phir pukaarogii sajanaa mar jaauungii maan jaa maan jaa maan jaa   threedots ', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'bhuul ho gayii jaane de sajanaa', 'year': '1985'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "naushad", "s d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='r d burman' in top3=['laxmikantpyarelal', 'naushad', 's d burman']

### #356 — PASS

- item: `{'lyrics': ' he he he he threedots laa laa laa threedots kal kyaa hogaa kisako pataa abhii zindagii kaa le lo mazaa 2  he dilawaalo duniyaa kii aisii taisii har pal apanaa hai din kaisaa raat kaisii he aish karo naacho gaao khaao piyo he jiinaa hai to mastii men rahake jiyo he he he he threedots laa laa laa threedots kal kyaa hogaa threedots  he ham jahaan hallaa gullaa hogaa wahiin ham se duniyaa hai duniyaa se ham nahiin he jab tak dam men hai dam pyaare he tab tak kaahe kaa hai gam pyaare he he he he threedots laa laa laa threedots kal kyaa hogaa threedots', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'kal kyaa hogaa kisako pataa', 'year': '1978'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "kalyanjianandji", "annu malik"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='r d burman' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='r d burman' in top3=['r d burman', 'kalyanjianandji', 'annu malik']

### #357 — PASS

- item: `{'lyrics': '  faujii gayaa jab gaanv men 2 pahan ke rangaruut ful buut paanv men faujii gayaa jab threedots  pahale logon ne rakhaa thaa meraa naam nikhattuu do din men jag aise ghuumaa jaise ghuumaa lattuu bharatii ho ke karanailaa karanail sinh ban baithaa meraa baapuu saath mere jaranail sinh ban baithaa aate dekhaa mujhako to karane lage salaamii aagepiichhe daude chaachaachaachii maamaamaamii yaaron ne saamaan uthaa kar rakhaa apane sar pe daravaaje par baithe the sab jab main pahunchaa ghar pe kas kar puure jor se phir maine sailyuut jo maaraa sabakii chhuttii ho gaii phir maine buut jo maaraa faujii gayaa jab threedots  ghar ke andar jaa kar phir jab maine kholaa baksaa dekh rahe the sab dekhen jag kaa nakshaa sabako thaa maaluum shaam ko khulegii ram kii botal sab aa baithe ghar par mere ghar meraa ban gayaa hotal biich men baithaa thaa main sab baithe the aajuubaajuu itane men banduuk chalii bhaii gaanv men aae daakuu utar gaii thii sabakii chhup gae saare dar ke maare main ghar se nikalaa sab meraa naam pukaaren maar ke laathii zamiin pe jhat se daakuon ko lalakaaraa ve the chaar akelaa main maine chaaron ko maaraa faujii gayaa jab threedots  chhod ke apane ghode daakuu jaan bachaa kar bhaage merii vaahvaah karate subah niind se log jaage main kheton kii sair ko nikalaa mausam thaa mastaanaa raste men vo milii meraa jisase thaa ishq puraanaa kuub sune aur kuub sunaae kisse agalepichhale nikalaa chaand to ham donon bhii khet se baahar nikale haayhaay mach gayaa shor saare gaanv men faujii gayaa jab threedots ', 'correct_label': 'laxmikantpyarelal', 'label': 4, 'split': 'test', 'title': 'faujii gayaa jab gaanv men', 'year': '1975'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "r d burman", "madan mohan"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='laxmikantpyarelal' ref='laxmikantpyarelal'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='laxmikantpyarelal' in top3=['laxmikantpyarelal', 'r d burman', 'madan mohan']

### #358 — FAIL

- item: `{'lyrics': ' ai dil dil kii duniyaa men aisaa haal bhii hotaa hai baahar koii hansataa hai andar koii rotaa hai ai dil koii pahachaanaa nahiin kisii ne ye maanaa nahiin kisii ne ye jaanaa nahiin kisii ko bataanaa nahiin dard chhupaa hai kahaan ai dil dil kii duniyaa threedots  tuune mujhase vafaa nahiin kii tujhako kaise vafaa milegii tuune mujhako dard diyaa hai tujhako kaise davaa milegii siine men uthate hain aramaan aise dariyaa men aate hain tuufaan jaise kabhii kabhii khud hii maajhii kashtii ko dubotaa hai ai dil dil kii duniyaa threedots  kaante chunakar teraa daaman phuulon se main bhar jaauungaa isase badii sazaa kyaa hogii maaf tujhe main kar jaauungaa ai aa hogii kisii ko pahachaan kaise pyaar men hote hain qurbaan kaise hamako ye maaluum na thaa pyaar bhii ik samajhautaa hai ai dil dil kii duniyaa threedots ', 'correct_label': 'annu malik', 'label': 1, 'split': 'test', 'title': 'ai dil dil kii duniyaa men aisaa haal bhii', 'year': '2001'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "shankarjaikishan", "annu malik"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='annu malik'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='annu malik' in top3=['laxmikantpyarelal', 'shankarjaikishan', 'annu malik']

### #359 — FAIL

- item: `{'lyrics': ' m aathreedots gunagunaa rahe hain bhanvare  khil rahii hain kalii kalii    2 l galii galii m kalii kalii l gunagunaa rahiithreedots  l zaraa dekho sajan beiimaan bhanvaraa kaise musakaaye m haay kalii yuun sharamaaye ghuunghat men jaise koii chhup jaaye l haay zaraathreedots m haay kaliithreedots l ritu aisii haae kaisii ye pavan chalii galii galii gunagunaa rahiithreedots m galii galii l kalii kalii m gunagunaa rahiithreedots  m kisii ko kyaa kahen ham dono bhii hain dekho kuchh khoye l khoye huaa kyaa oe oe jaage jiyaa men aramaan soye  m soye kisii kothreedots l khoye huaa kyaathreedots m ritu aisii haae kaisii ye pavan chalii galii galii gunagunaa rahiithreedots l galii galii m kalii kalii l gunagunaa rahiithreedots aathreedots  l suno paas na aao kaliyon ke bahaane pyaar na jataao m jaao chalo baat na banaao bhanvare ke bahaane aankh na ladaao l jaao suno paasthreedots m jaao chalo baatthreedots l ritu aisii haae kaisii ye pavan chalii galii galii gunagunaa rahiithreedots m gunagunaa rahiithreedots l galii galii m kalii kalii threedots', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'gunagunaa rahe hain bhanvare khil rahii hai kalii kalii', 'year': '0'}`
- output: `{"pred": "c ramchandra", "top3": ["c ramchandra", "s d burman", "a r rahman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='c ramchandra' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='s d burman' in top3=['c ramchandra', 's d burman', 'a r rahman']

### #360 — FAIL

- item: `{'lyrics': ' aa a a  na phuulon kii duniyaa na taaron kii duniyaa ye hai bas kayaalebahaaron kii duniyaa  yahaan mast nazaren bahakane ko tarase umangon bhare dil dhadakane ko tarase ye hai pyaar ke besahaaron kii duniyaa  yahaan gam hai laakhon masarrat nahiin hai tadapane kii lekin ijaazat nahiin hai ye hai ishq ke beqaraaron kii duniyaa  na phuulon kii duniyaa na taaron kii duniyaa ye hai bas kayaalebahaaron kii duniyaa  aa a a  paayaliyaa baavarii baaje paayaliyaa morii jhanana jhanana jhana jhananana baaje a a paayaliyaa baavarii baaje threedots  aa a a  aaj sakhii more pii ghar aaye aa a  a aaj sakhii more pii ghar aaye dekhdekh chhab jiyaraa jaaye baar baar moraa man laharaaye paayaliyaa baavarii baaje threedots  saat suron ke diip jalaake aa a a saat suron ke diip jalaake prem biin kii dhun par gaake aaj naachuun main piyaa ko paake paayaliyaa baavarii baaje threedots  aa a a', 'correct_label': 'naushad', 'label': 6, 'split': 'test', 'title': 'na phuulon kii duniyaa  paayaliyaa baavarii baaje', 'year': '1966'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "naushad", "c ramchandra"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='shankarjaikishan' ref='naushad'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='naushad' in top3=['shankarjaikishan', 'naushad', 'c ramchandra']

### #361 — PASS

- item: `{'lyrics': ' yaaron ne baahen jo daale gale to dekhane vaale jale kyon jale kyon yaaron ne baahen jo daale gale to dekhane vaale jale kyon jale jale kyon jale kyon jale kyon jale2 jale jale yaaron ne baahen jo daale gale to dekhane vaale jale kyon jale  ye mahakii fizaa hai qayaamat qayaamat ye bahakii havaa hai qayaamat qayaamat2 ishaare yahaan hai aur nazaren kahiin hai ye kaisii adaa hai qayaamat qayaamat qayaamat men donon jo dil se mile to dekhane vaale jale kyon jale threedots  idhar dil men mere muhabbat muhabbat udhar dil men tere muhabbat muhabbat2 jidhar dekhate hain yahii dekhate hain hai aalam ko gheere muhabbat muhabbat muhabbat men donon jo dil se mile to dekhane vaale jale kyon jale threedots', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'yaaron ne baahen jo daale gale', 'year': '1954'}`
- output: `{"pred": "s d burman", "top3": ["s d burman", "shankarjaikishan", "c ramchandra"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='s d burman' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='s d burman' in top3=['s d burman', 'shankarjaikishan', 'c ramchandra']

### #362 — FAIL

- item: `{'lyrics': '     ham unake paas aate hain wo hamase duur jaate hain tadap kar daastaan apanii bahaaron ko sunaate hain bahaaron ko sunaate hain ham unake paas aate hain  jabase hamako pyaar huaa hai jiinaa bhii dushwaar huaa hai 2 sahaare jab na paate hain to phir ghabaraa hii jaate hain  tadap kar daastaan apanii bahaaron ko sunaate hain bahaaron ko sunaate hain ham unake paas aate hain  bin tere viiraan rahaa hai gulashan kaa har phuul kizaan hai 2 tujhe aramaan bulaate hain naye tuufaan uthaate hain  tadap kar daastaan apanii bahaaron ko sunaate hain bahaaron ko sunaate hain ham unake paas aate hain  dard men duubii shaam na puuchho aahon kaa anjaam na puuchho 2 shamaa gam kii jalaate hain andhere badhate jaate hain  tadap kar daastaan apanii bahaaron ko sunaate hain bahaaron ko sunaate hain ham unake paas aate hain ', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'ham unake paas aate hain', 'year': '1953'}`
- output: `{"pred": "madan mohan", "top3": ["madan mohan", "shankarjaikishan", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='madan mohan' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='shankarjaikishan' in top3=['madan mohan', 'shankarjaikishan', 'laxmikantpyarelal']

### #363 — FAIL

- item: `{'lyrics': ' su \t haay ye tuune kyaa kiyaa mujhe phir ye kyaa bataa diyaa \tdard jo miithaamiithaa thaa aur use badhaa diyaa \thaay ye tuune kyaa kiyaa  2  ra \thamane to dil lutaa diyaa hamane to sar jhukaa diyaa 2 \tab to jo ho huaa kare 2 \thamane to ghar jalaa diyaa \tdard jo miithaamiithaa thaa aur use badhaa diyaa \thaay ye tuune kyaa kiyaa  su \thaay ye tuune kyaa kiyaa mujhe phir ye kyaa bataa diyaa \tdard jo miithaamiithaa thaa aur use badhaa diyaa \thaay ye tuune kyaa kiyaa  su \tdil se jo dil ko raah thii kab wo chhupaaye chhup sakii 2 \thonthon ne rok lii hansii aankhon ne muskuraa diyaa 2 \tdard jo miithaamiithaa thaa aur use badhaa diyaa \thaay ye tuune kyaa kiyaa  \thaay ye tuune kyaa kiyaa mujhe phir ye kyaa bataa diyaa \tdard jo miithaamiithaa thaa aur use badhaa diyaa \thaay ye tuune kyaa kiyaa ', 'correct_label': 'c ramchandra', 'label': 2, 'split': 'test', 'title': 'haay ye tuune kyaa kiyaa', 'year': '1949'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "annu malik", "s d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='shankarjaikishan' ref='c ramchandra'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='c ramchandra' in top3=['shankarjaikishan', 'annu malik', 's d burman']

### #364 — FAIL

- item: `{'lyrics': ' saathii na koii manzil diyaa hai na koii mahafil chalaa mujhe leke ai dil akelaa kahaan threedots  hamadam mile koii kahiin aise nasiib hii nahiin bedard hai zamiin duur aasamaan threedots  galiyaan hain apane desh kii phir bhii hain jaise ajanabii kisako kahe koii apanaa yahaan threedots  patthar ke inasaan mile patthar ke devataa mile shiishe kaa dil liye jaauun kahaan threedots', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'saathii na koii manzil diyaa hai na koii mahafil', 'year': '-1'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "laxmikantpyarelal", "kalyanjianandji"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='r d burman' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='s d burman' in top3=['r d burman', 'laxmikantpyarelal', 'kalyanjianandji']

### #365 — FAIL

- item: `{'lyrics': '  gaanv men piipal piipal kii chhainyaa chhainyaa men panaghat panaghat men paanii paanii men aag lagaae raanii terii javaanii gaanv men piipal threedots  nikalii nahaa ke gorii taalaab se kuchh aise saavan ke baadalon se nikalaa ho chaand jaise 2 kaanon men jhumake mukhade pe aanchal aankhon men kajaraa paanv men paayal paayal ke giit sunaae o raanii terii javaanii gaanv men piipal threedots  ye ruup hai yaa sholaa ye rang hai ke jaaduu ye nain hain ke jhuule ye zulf hai ki baadal haay teraa kyaa kahanaa dekhe jo nainaa to saarii rainaa jaage ye nainaa nainon se niind churaae o raanii terii javaanii gaanv men piipal threedots ', 'correct_label': 'laxmikantpyarelal', 'label': 4, 'split': 'test', 'title': 'gaanv men piipal  paanii men aag lagaae raanii terii javaanii', 'year': '1973'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "shankarjaikishan", "annu malik"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='r d burman' ref='laxmikantpyarelal'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='laxmikantpyarelal' in top3=['r d burman', 'shankarjaikishan', 'annu malik']

### #366 — PASS

- item: `{'lyrics': '  la \tbaagon men phuul kisane khilaae hain ra \tmaine to nahiin maine to nahiin  la \tchor kaun taare kisane churaae hain ra \tmaine to nahiin maine to nahiin taubaa  la \ttaubaa kaa savaal kyaa taubaa maine kii nahiin ra \tkaisaa ye suruur hai maine pii hai jii nahiin \tphir mere hosh kisane udaae hain ra \tmaine to nahiin maine to nahiin  la \taakir is jahaan men hotii hai ye baat kyon \tdo aur do jamaa karen to banate nahiin paanch kyon \tdo aur do chaar kisane banaae hain ra \tmaine to nahiin maine to nahiin  la \tye jo dil ke saaz the vo to beaavaaz the \ttere mere pyaar ke afasaane to raaz the \traaz sabako ye kisane bataae hain \ttuune to nahiin tuune to nahiin ra \tmaine to nahiin maine to nahiin ', 'correct_label': 'laxmikantpyarelal', 'label': 4, 'split': 'test', 'title': 'baagon men phuul kisane khilaae hain maine to nahiin', 'year': '1967'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "annu malik", "kalyanjianandji"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='laxmikantpyarelal' ref='laxmikantpyarelal'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='laxmikantpyarelal' in top3=['laxmikantpyarelal', 'annu malik', 'kalyanjianandji']

### #367 — FAIL

- item: `{'lyrics': '  tanman tere rangranguungii chhaayaa banakar sang chaluungii sevaa karuungii ang laguungii archanaa main terii saajanaa tanman tere threedots  janmjanm tere binaa nainaa nahiin soe ghadiighadii sapane tere palakon ne piroe tuu hai mere jiivan kii saadhanaa tanman tere threedots  pyaar teraa kumakum hai baanhen terii maalaa praan meraa pujaarii teraa man hai shivaalaa zindagii hai terii praarthanaa tanman tere threedots  jhuum uthaa anganaa meraa padii nazar terii raam kare laage tujhe saarii umar merii duniyaa ruuthe tuu naa ruuthanaa tanman tere threedots ', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'tanman tere rangranguungii', 'year': '1973'}`
- output: `{"pred": "s d burman", "top3": ["s d burman", "kalyanjianandji", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='s d burman' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='shankarjaikishan' in top3=['s d burman', 'kalyanjianandji', 'shankarjaikishan']

### #368 — FAIL

- item: `{'lyrics': ' dil kaanton men ulajhaayaa hai ik dushman pe pyaar aayaa hai 2 sholaa shabanam men laharaayaa hai ik dushman pe pyaar aayaa hai dil kaanton men  jaaduu saa chalane lagaa hai mausam badalane lagaa hai 2 lagataa hai mere siine se dil baahar nikalane lagaa hai shiishaa pathhar se takaraayaa hai ik dushman pe pyaar aayaa hai  dil kaanton men ulajhaayaa hai ik dushman pe pyaar aayaa hai dil kaanton men threedots  na paas aane diyaa hai na duur hone diyaa hai 2 na honthon ko hansane diyaa hai na aankhon ko rone diyaa hai badaa zaalim ne tadapaayaa hai ik dushman pe pyaar aayaa hai  dil kaanton men ulajhaayaa hai ik dushman pe pyaar aayaa hai dil kaanton men threedots  aisaa sitam karane se sainyyaan banaa re na jaane jab tak ho sakaa ye hamase ham ruuthe rahe nahiin maane yahii gussaa ye rang laayaa hai ik dushman pe pyaar aayaa hai  dil kaanton men ulajhaayaa hai ik dushman pe pyaar aayaa hai sholaa shabanam men laharaayaa hai ik dushman pe pyaar aayaa hai dil kaanton men threedots ', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'dil kaanton men ulajhaayaa hai', 'year': '1976'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "annu malik", "c ramchandra"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='r d burman' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='s d burman' in top3=['r d burman', 'annu malik', 'c ramchandra']

### #369 — FAIL

- item: `{'lyrics': ' vaarii jaavaan vaarii jaavaan vaarii jaavaan sau sau baarii sau sau baarii vaarii jaavaan  solah singaar karake godii bharaaii ve sainyaan sainyaan sainyaan sainyaan sainyaan se khele bahut ab chhotuu ko khilaaii le solah singaar karake threedots vaarii jaavaan threedots  chhotuu jo aave ghar men chhotuu jo aave ghar men oy hoy hoy hoy oy hoy hoy hoy chhotuu jo aave ghar men naanii bahalaae paayal pahan ke naanii naach dikhaave vaarii jaavaan threedots  haan chhotuu jo aave ghar men chhotuu jo aave ghar men hoy hoy oy chhotuu jo aave ghar men maasii ko bulaave  chhotuu jo aave ghar men aave unake maamaa maamaa yaa chaachaa an chaachaa chhotuu jo aave ghar men aave unake maamaa daanton se naadaa pakade haathon se pajaamaa ho terii hansii bhar bhar ke ghar men chhidakaave ho solah singaar karake threedots ', 'correct_label': 'annu malik', 'label': 1, 'split': 'test', 'title': 'vaarii jaavaan  solah singaar karake godii bharaaii ve', 'year': '2002'}`
- output: `{"pred": "madan mohan", "top3": ["madan mohan", "annu malik", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='madan mohan' ref='annu malik'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='annu malik' in top3=['madan mohan', 'annu malik', 'shankarjaikishan']

### #370 — FAIL

- item: `{'lyrics': '  mu \tpyaar kaa bandhan kuun kaa rishtaa chhuute se naa chhuute do \tdil se dil kii dor bandhii jo tuute se naa tuute \tpyaar kaa bandhan threedots  la \tlage rahen aur bhare rahenge pyaar bhare ye mele \tho pyaar bhare ye mele mu \tkushiyon kaa jhuulaa jhuulenge bhaaiibahan alabele \tho bhaaiibahan alabele \tsun le daataa inakaa naataa janamjanam naa chhuute do \tdil se dil kii threedots  mu \tjagamagjagamag aae diivaalii laxmii dhan barasaae \tho laxmii dhan barasaae la \trangbirange dhaage lekar raakhii kaa din aae \tho raakhii kaa din aae \tin dhaagon kaa rang ho gaharaa chhuute se naa chhuute do \tdil se dil kii threedots ', 'correct_label': 'kalyanjianandji', 'label': 3, 'split': 'test', 'title': 'pyaar kaa bandhan kuun kaa rishtaa', 'year': '1977'}`
- output: `{"pred": "naushad", "top3": ["naushad", "kalyanjianandji", "r d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='naushad' ref='kalyanjianandji'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='kalyanjianandji' in top3=['naushad', 'kalyanjianandji', 'r d burman']

### #371 — FAIL

- item: `{'lyrics': ' lataa o o o bakshii oo o oo  bakshii baagon men bahaar aaii honthon pe pukaar aaii aajaa aajaa aajaa aajaa merii raanii lataa rut beqaraar aaii rut beqaraar aaii dolii men sawaar aaii aajaa aajaa aajaa aajaa mere raajaa bakshii baagon men bahaar aaii honthon pe pukaar aaii aajaa aajaa aajaa aajaa merii raanii  bakshii phuulon kii galii men aaiin bhanvaron kii toliyaan bhanvaron kii toliyaan diye se patangaa khele aankhmichauliyaan bole aisii boliyaan ki pyaar jaagaa jag so gayaa lataa rut beqaraar aaii dolii men sawaar aaii aajaa aajaa aajaa aajaa mere raajaa bakshii baagon men bahaar aaii  lataa sapanaa to sapanon kii baat hai pyaar men baat hai pyaar men niind nahiin aatii sainyaa tere intazaar men hoke beqaraar tujhe dhuundhuun main tuu kahaan kho gayaa bakshii baagon men bahaar aaii honthon pe pukaar aaii aajaa aajaa aajaa aajaa merii raanii lataa aajaa mere raajaa  bakshii lambiilambii baaten chheden chhotiisii raat men chhotiisii raat men lataa saarii baaten kaisii hongii ik mulaaqaat men ek hii baat men lo dekh lo saveraa ho gayaa bakshii baagon men bahaar aaii honthon pe pukaar aaii aajaa aajaa aajaa aajaa merii raanii lataa rut beqaraar aaii dolii men sawaar aaii aajaa aajaa aajaa aajaa mere raajaa bakshii aajaa merii raanii lataa aajaa mere raajaa', 'correct_label': 'laxmikantpyarelal', 'label': 4, 'split': 'test', 'title': 'baagon men bahaar aaii  honthon pe pukaar aaii', 'year': '1972'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "laxmikantpyarelal", "c ramchandra"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='r d burman' ref='laxmikantpyarelal'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='laxmikantpyarelal' in top3=['r d burman', 'laxmikantpyarelal', 'c ramchandra']

### #372 — FAIL

- item: `{'lyrics': '  he he he ik din kisii faqiir ne ik baat kahii thii ab jaa ke dil ne maanaa maanaa vo baat sahii thii  jisakaa koii nahiin usakaa to kudaa hai yaaron 2  main nahiin kahataa  2 kitaabon men likhaa hai yaaron jisakaa koii nahiin threedots   ham to kyaa hain  2 vo farishton ko aajamaataa hai 2 banaakar hamako mitaataa hai phir banaataa hai  aadamii tuut ke  2 sau baar judaa hai yaaron jisakaa koii nahiin threedots  imtahaanon kaa yahaan daur yuun hii chalataa hai 2 aandhiyon men bhii ummiidon kaa diyaa jalataa hai  kal kii ummiid pe  2 insaan jiyaa hai yaaron jisakaa koii nahiin threedots   kab talak hamase  2 taqadiir bhalaa ruuthegii 2 in andheron se ujaale kii kiran phuutegii  gam ke daaman men  2 kahiin chain chhupaa hai yaaron jisakaa koii nahiin threedots ', 'correct_label': 'kalyanjianandji', 'label': 3, 'split': 'test', 'title': 'he ik din kisii faqiir ne  jisakaa koii nahiin usakaa to', 'year': '1981'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "kalyanjianandji", "annu malik"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='r d burman' ref='kalyanjianandji'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='kalyanjianandji' in top3=['r d burman', 'kalyanjianandji', 'annu malik']

### #373 — PASS

- item: `{'lyrics': ' hu le le aa aa aa merii saarii subahon men shaamon men tuu hii tuu  mere din ke har pal men raaton men tuu hii tuu  tuu hii merii niindon men kaabon men tuu hii tuu  tuu mere kayaalon men yaadon men tuu hii tuu  merii saarii subahon men shaamon men tuu hii tuu mere din ke har pal men raaton men tuu hii tuu   tuu hii meraa saagar aur tuu hii meraa saahil  aa aa aa aa  tuu hii mera rahabar aur tuu hii merii manzil  aa aa aa aa  bas tuu hii tuu hai raahon men bas tuu hii tuu nigaahon men  hai zindagii tuu hii merii tujhase kaise ye main kahuun  tuu hii tuu nazaaron men aankhon men tuu hii tuu  merii  merii saarii subahon men shaamon men tuu hii tuu mere din ke har pal men raaton men tuu hii tuu tuu hii merii niindon men kaabon men tuu hii tuu tuu mere kayaalon men yaadon men tuu hii tuu hu le le aa aa aa  tuu hii hai meraa dil aur tuu hii meraa aramaan  nii dhaa saa maa gaa re saa re gaa maa maa re saa re tuu hii merii mahafil aur tuu hii meraa mahamaan  aa aa aa aa  bas tuu hii tuu hai dhadakan men bas tuu hii tuu mere man men  tere sivaa tuu hii bataa ik pal bhii kaise main rahuun  tuu hii tuu hai saanson men aahon men tuu hii tuu  merii saarii subahon men shaamon men tuu hii tuu mere din ke har pal men raaton men tuu hii tuu tuu hii merii niindon men kaabon men tuu hii tuu tuu mere kayaalon men yaadon men tuu hii tuu hu le le aa aa aa ', 'correct_label': 'a r rahman', 'label': 0, 'split': 'test', 'title': 'merii saarii subahon men shaamon men tuu hii tuu', 'year': '1997'}`
- output: `{"pred": "a r rahman", "top3": ["a r rahman", "s d burman", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='a r rahman' ref='a r rahman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='a r rahman' in top3=['a r rahman', 's d burman', 'laxmikantpyarelal']

### #374 — PASS

- item: `{'lyrics': ' ham aj kahin dil kho baithe yun samajho kisi ke ho baithe  ham aj kahin threedots   haradam jo koi pas ane laga bhed ulfat ke samajhane laga  nazaron se nazar kaa takarana tha dil ke liye ik afasana  ham hathon se dil ko ganva baithe ham aj kahin threedots   ankhon men samaya koi magar kaun aya kisi ko kya ye khabar  puchho to yahi hai usaka pata chanchal naina aur shokh ada  ham dil ki naiyya dubo baithe ham aj kahin threedots ', 'correct_label': 'naushad', 'label': 6, 'split': 'test', 'title': 'ham aaj kahiin dil kho baithe yuun samajho kisii ke ho baithe', 'year': '1949'}`
- output: `{"pred": "naushad", "top3": ["naushad", "madan mohan", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='naushad' ref='naushad'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='naushad' in top3=['naushad', 'madan mohan', 'shankarjaikishan']

### #375 — PASS

- item: `{'lyrics': '   motii jaisaa rang ang men  2 ras kaa saagar laharaae tere ruup kii aanch lage to patthar dil bhii pighal jaae motii jaisaa rang threedots  nainon men hai tere jaise kiranon kaa baseraa nikharaa teraa yauvan jaisaa bikharaa ho saveraa suuraj tere darshan ko har din aaejaae motii jaisaa rang threedots  hogaa vo bhii sundar jisape hogii terii chhaayaa hogaa vo bhii mohit jisane tujhako hai banaayaa jiivan kar de roshan tuu jo muskaraae motii jaisaa rang threedots ', 'correct_label': 'kalyanjianandji', 'label': 3, 'split': 'test', 'title': 'motii jaisaa rang ang men ras kaa saagar laharaae', 'year': '1970'}`
- output: `{"pred": "kalyanjianandji", "top3": ["kalyanjianandji", "laxmikantpyarelal", "a r rahman"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='kalyanjianandji' ref='kalyanjianandji'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='kalyanjianandji' in top3=['kalyanjianandji', 'laxmikantpyarelal', 'a r rahman']

### #376 — FAIL

- item: `{'lyrics': '  la \tpatajhar saavan basant bahaar 2 \tek baras ke  mausam chaar  2 \tpaanchavaan mausam pyaar kaa intazaar kaa 2 \tpatajhar saavan threedots  \tkoyal kuuke kuu kuu kuu \tkoyal kuuke bulabul gaae \thar ek mausam aaejaae a \tlekin pyaar kaa mausam aae 2 \tsaare jiivan men  ek baar  2 \tpatajhar saavan threedots la \tpatajhar saavan threedots do \tpatajhar saavan threedots  a \trangon kaa melaa ye jag saaraa la \trangon kaa melaa ye jag saaraa a \trang badalatii jiivan dhaaraa la \trang badalatii jiivan dhaaraa a \tpyaar kaa rang hai sabase pyaaraa la \tpyaar kaa rang hai sabase pyaaraa do \trangbirange  rang hazaar  2 \tpatajhar saavan threedots \tpatajhar saavan basant bahaar 2 \tek baras ke  mausam chaar  2 \tpaanchavaan mausam pyaar kaa intazaar kaa 2 \tpatajhar saavan threedots  \tphuul khile na baadal barase \tpyaar ke mausam men dil tarase \tho mere gale men apanii nazar se \tdaal do tum baanhon ke haar \tpatajhar saavan threedots ', 'correct_label': 'laxmikantpyarelal', 'label': 4, 'split': 'test', 'title': 'patajhar saavan basant bahaar', 'year': '1987'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "kalyanjianandji", "r d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='shankarjaikishan' ref='laxmikantpyarelal'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='laxmikantpyarelal' in top3=['shankarjaikishan', 'kalyanjianandji', 'r d burman']

### #377 — FAIL

- item: `{'lyrics': ' jab se chale gaye hain wo zindagii zindagii nahiin saaz hai aur sadaa nahiin shammaa hai roshanii nahiin  chhod ke mujhako chal diye ye bhii nahiin kiyaa kayaal unake siwaa jahaan men aur meraa koii nahiin jab se chale gaye hain wo zindagii zindagii nahiin  saare jahaan kii raunaken jaise kisii ne luut liin phuul hai taazagii nahiin chaand hai chaandanii nahiin jab se chale gaye hain wo zindagii zindagii nahiin  jiine ko jii rahii huun main unake bagair bhii agar zindagii kah sakuun jise aisii to zindagii nahiin jab se chale gaye hain wo zindagii zindagii nahiin saaz hai aur sadaa nahiin shammaa hai roshanii nahiin ', 'correct_label': 'naushad', 'label': 6, 'split': 'test', 'title': 'jab se chale gaye hain wo zindagii zindagii nahiin', 'year': '1947'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "shankarjaikishan", "r d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='naushad'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='naushad' in top3=['laxmikantpyarelal', 'shankarjaikishan', 'r d burman']

### #378 — FAIL

- item: `{'lyrics': '  ra \tdil shaad thaa ke phuul khilenge bahaar men \tmaaraa gayaa gariib isii aitabaar men  la \tmujhe terii mohabbat kaa sahaaraa mil gayaa hotaa 2 \tagar tuufaan nahiin aataa kinaaraa mil gayaa hotaa ra \tmujhe terii mohabbat threedots  la \tna thaa manzuur qismat ko na thii marzii bahaaron kii \t nahiin to is gulistaan men  2 kamii thii kyaa nazaaron kii \tmerii nazaron ko bhii koii nazaaraa mil gayaa hotaa \tagar tuufaan nahiin threedots ra \tmujhe terii mohabbat threedots  ra \tkushii se apanii aankhon ko main ashqon se bhigo letaa \t mere badale tuu hans letii  2 tere badale main ro letaa \tmujhe ai kaash teraa dard saaraa mil gayaa hotaa \tagar tuufaan nahiin threedots la \tmujhe terii mohabbat threedots  \tmilii hai chaandanii jinako ye unakii apanii qismat hai \t mujhe apane muqaddar se  2 faqat itanii shikaayat hai \tmujhe tuutaa huaa koii sitaaraa mil gayaa hotaa \tagar tuufaan nahiin threedots ra \tmujhe terii mohabbat threedots ', 'correct_label': 'laxmikantpyarelal', 'label': 4, 'split': 'test', 'title': 'dil shaad thaa ke phuul  mujhe terii mohabbat kaa', 'year': '1971'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "madan mohan", "kalyanjianandji"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='shankarjaikishan' ref='laxmikantpyarelal'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='laxmikantpyarelal' in top3=['shankarjaikishan', 'madan mohan', 'kalyanjianandji']

### #379 — FAIL

- item: `{'lyrics': ' chhotii sii zindagii men 2 kyaa pyaar muskuraaye puurii na ho kahaanii 2 aankhon ko niind aaye  chhotii sii zindagii men kyaa pyaar muskuraaye   chalataa rahaa musaafir manzil magar na aaii  2  ham kho gaye kushii se apanii kabar na aaii  2 phuulon kii aarazuu men 2 kaante gale lagaaye  chhotii sii zindagii men kyaa pyaar muskuraaye   aansuu bahaa ke dekhaa rone se faayadaa kyaa  2  roro ke daag dil ke dhone se faayadaa kyaa  2 kushiyon kii hasaraton men 2 kyaakyaa fareb khaaye  chhotii sii zindagii men kyaa pyaar muskuraaye ', 'correct_label': 'c ramchandra', 'label': 2, 'split': 'test', 'title': 'chhotii sii zindagii men kyaa pyaar muskuraaye', 'year': '1954'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "c ramchandra", "madan mohan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='shankarjaikishan' ref='c ramchandra'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='c ramchandra' in top3=['shankarjaikishan', 'c ramchandra', 'madan mohan']

### #380 — FAIL

- item: `{'lyrics': ' teraa gamakvaar huun lekin main tujh tak aa nahiin sakataa main apane naam terii bekasii likhavaa nahiin sakataa  terii aankh ke aansuu pii jaauun aisii merii taqadiir kahaan tere gam men tujhako bahalaauun aisii merii taqadiir kahaan  ai kaash jo mil kar rote kuchh dard to halake hote bekaar na jaate aansuu kuchh daag jigar ke dhote phir ranj na hotaa itanaa hai tanahaai men jitanaa ab jaane ye rastaa gam kaa hai aur bhii lambaa kitanaa haalaat kii ulajhan sulajhaauun aisii merii taqadiir kahaan terii aankh ke aansuu pii jaauun  kyaa terii zulf kaa leharaa hai ab tak vohii sunaharaa kyaa ab tak tere dar pe detii hen havaaen paharaa lekin hai ye khaamokhayaalii terii zulf banii hai savaalii mohataaj hai ek kalii kii ik roz thii phuulon vaalii vo zulfen pareshaan mahakaauun aisii merii taqadiir kahaan terii aankh ke aansuu pii jaauun', 'correct_label': 'madan mohan', 'label': 5, 'split': 'test', 'title': 'terii aankh ke aansuu pii jaauun aisii merii taqadiir kahaan', 'year': '1964'}`
- output: `{"pred": "s d burman", "top3": ["s d burman", "madan mohan", "c ramchandra"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='s d burman' ref='madan mohan'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='madan mohan' in top3=['s d burman', 'madan mohan', 'c ramchandra']

### #381 — PASS

- item: `{'lyrics': '  aa aah jaa re jaa bewafaa nahiin tujhako pataa jaa re jaa bewafaa nahiin tujhako pataa yah sharaafat hai kyaa yah muhabbat hai kyaa jhuuthaa hai teraa pyaar teraa kyaa aitabaar kabhii is pe nazar kabhii us pe nazar jaa re jaa beqadar nahiin tujhako kabar kaise lete hain dil yah badaa hai mushkil2  kishor o sanam tere sar kii qasam bekabar huun zaruur bevafaa main nahiin kar mujh pe yaqiin tuu aise naa jalaa dil   donon laa laa laa threedots   kishor  o sanam tere sar kii qasam bekabar huun zaruur bewafaa main nahiin kar mujh pe yaqiin tuu aise naa jalaa dil  aashaa ye badaa hai mushkil jaa re jaa beimaan jaane saaraa jahaan ye bahaane hain khuub afasaane hain khuub tuu patangaa nahiin parawaanaa nahiin tuu hai koii bhanwar paanii jaisii nazar kabhii is daal par kabhii us daal par jaa re jaa sangadil yah badaa hai mushkil jaa re jaa beimaan jaane saaraa jahaan  kishor aa yahaan tuu hai kyon badgumaan aazamaa ke to dekh dil lagaa ke to dekh hai tuu hii meraa jiivan merii manzil  donon laa laa laa threedots  kishor aa yahaan tuu hain kyon badgumaan aazamaa ke to dekh dil lagaa ke to dekh hai tuu hii meraa jiivan merii manzil  aashaa yah badaa hai mushkil jaa re jaa bewafaa nahiin tujhako pataa jaa re jaa bewafaa nahiin tujhako pataa yah sharaafat hai kyaa yah muhabbat hai kyaa jhuuthaa hai teraa pyaar teraa kyaa aitabaar kabhii is pe nazar kabhii us pe nazar jaa re jaa beqadar nahiin tujhako kabar kaise lete hain dil yah badaa hai mushkil laa laa laa laa laa  kishor laa laa laa laa laa aashaa laa laa laa laa laa kishor laa laa laa laa laa ', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'jaa re jaa bewafaa', 'year': '1974'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "shankarjaikishan", "naushad"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='r d burman' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='r d burman' in top3=['r d burman', 'shankarjaikishan', 'naushad']

### #382 — PASS

- item: `{'lyrics': ' terii aankhon kii chaahat men to main sab kuchh lutaa duungaa muhabbat kaise kii jaatii muhabbat kaise kii jaatii haan duniyaa ko dikhaa duungaa terii aankhon kii chaahat men threedots  tere naazuq hasiin qadamon ke niiche hamasafar mere\t2 are o hamasafar mere jahaan hogaa koii kaantaa jahaan hogaa koii kaantaa vahaan main dil bichhaa duungaa terii aankhon kii chaahat men threedots  tamannaa hai ke roshan ho terii duniyaa terii mahafil 2 terii duniyaa terii mahafil ujaalaa mil sake tujhako ujaalaa mil sake tujhako to main ghar bhii jalaa duungaa terii aankhon kii chaahat men threedots  bahaaron chiiz kyaa hai phuul kaliyaan kisako kahate hain\t2 ke kaliyaan kisako kahate hain lo meraa salaam to main lo meraa salaam to main teraa jiivan sajaa duungaa  terii aankhon kii chaahat men to main sab kuchh lutaa duungaa muhabbat kaise kii jaatii muhabbat kaise kii jaatii haan duniyaa ko dikhaa duungaa terii aankhon kii chaahat men threedots', 'correct_label': 'laxmikantpyarelal', 'label': 4, 'split': 'test', 'title': 'terii aankhon kii chaahat men to main sab kuchh lutaa duungaa', 'year': '-1'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "annu malik", "r d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='laxmikantpyarelal' ref='laxmikantpyarelal'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='laxmikantpyarelal' in top3=['laxmikantpyarelal', 'annu malik', 'r d burman']

### #383 — PASS

- item: `{'lyrics': '    mere piyaa to basen parades re haae basant rut kyon aaii tuu pawan naa kar athakeliyaan mere dil kii kalii murajhaaii  mere piyaa to basen threedots  piyaa piyaa papiihaa gaataa hai dil gam men duubaa jaataa hai praanon ko lage hai thes re haae basant rut kyon aaii mere piyaa to basen threedots  sanwariyaa naataa tod gaye ik dard saa dil men chhod gaye bhejhaa naa koii sandes re haae basant rut kyon aaii mere piyaa to basen threedots  phir phuul phuul musakaane lagaa mujhe apanaa phuul yaad aane laga phuulon kaa badal kar bhes re haae basant rut kyon aaii mere piyaa to basen threedots  bagiyaa men kisii kii bansii na bajii raajaa na aaye raanii na sajii bansii na bajii raanii na sajii ujadaa mere man kaa des re haae basant rut kyon aaii mere piyaa to basen threedots  ', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'mere piyaa to basen parades re', 'year': '1947'}`
- output: `{"pred": "s d burman", "top3": ["s d burman", "naushad", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='s d burman' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='s d burman' in top3=['s d burman', 'naushad', 'laxmikantpyarelal']

### #384 — PASS

- item: `{'lyrics': ' kamoshiyaan gunagunaane lagiin tanhaaiyaan muskuraane lagiin 3  saragoshii kare havaa chupake se mujhe kahaa  dil kaa haal bataa dilabar se na chhupaa  sun ke baat ye sharm se merii aankhen jhuk jaane lagiin  kamoshiyaan gunagunaane lagiin tanhaaiyaan muskuraane lagiin saragoshii kare havaa chupake se mujhe kahaa dil kaa haal bataa dilabar se naa chhupaa sun ke baat ye sharm se merii aankhen jhuk jaane lagiin  jaag uthaa hai sapanaa kisakaa merii in aankhon men  ek naii zindagii shaamil ho rahii saanson men  kisii kii aatii hai sadaa havaaon men  kisii kii baaten hain dabii sii honthon men  raatdin merii aankhon men koii parachhaaiin laharaane lagii  kamoshiyaan gunagunaane lagiin tanhaaiyaan muskuraane lagiin   dil kaa ye kaaravaan yuun hii thaa ravaanravaan  manzil na hamasafar lekin naye meharabaan  terii vo ek nazar kar gaii asar duniyaa sanvar jaane lagii  kamoshiyaan gunagunaane lagiin tanhaaiyaan muskuraane lagiin  sharmohayaa se kah do kudaahaafiz o merii jaanaa  hai ghadii milan kii kudaaraa laut ke na aanaa  raat kaa pardaa hamaarii hii kaatir  saje hain ham bhii to tumhaarii hii kaatir  jaisejaise tum paas aate ho saansen ruk jaane lagiin  kamoshiyaan gunagunaane lagiin 2 tanhaaiyaan muskuraane lagiin 2  dil kaa ye kaaravaan yuun hii thaa ravaanravaan manzil na hamasafar lekin naye meharabaan terii vo ek nazar kar gaii asar duniyaa sanvar jaane lagii  kamoshiyaan gunagunaane lagiin tanhaaiyaan muskuraane lagiin   kamoshiyaan gunagunaane lagiin tanhaaiyaan muskuraane lagiin 2  kamoshiyaan gunagunaane lagiin tanhaaiyaan muskuraane lagiin saragoshii kare havaa chupake se mujhe kahaa dil kaa haal bataa dilabar se naa chhupaa sun ke baat ye sharm se merii aankhen jhuk jaane lagiin  2  jaag uthaa hai sapanaa kisakaa merii in aankhon men ek naii zindagii shaamil ho rahii saanson men kisii kii aatii hai sadaa havaaon men kisii kii baaten hain dabii sii honthon men raatdin merii aankhon men koii parachhaaiin laharaane lagii  kamoshiyaan gunagunaane lagiin tanhaaiyaan muskuraane lagiin dil kaa ye kaaravaan yuun hii thaa ravaanravaan manzil na hamasafar lekin naye meharabaan terii vo ek nazar kar gaii asar duniyaa sanvar jaane lagii  bekayaalii men bhii aataa hai kayaal teraa  beqaraarii merii karatii hai savaal teraa  terii vafaaon kii ummiid hai mujhako terii nigaahon kii panaah de mujhako  sun ai hamanashiin aas ye terii mujhako tadapaane lagii  kamoshiyaan gunagunaane lagiin kamoshiyaan gunagunaane lagiin tanhaaiyaan muskuraane lagiin tanhaaiyaan muskuraane lagiin  dil kaa ye kaaravaan yuun hii thaa ravaanravaan manzil na hamasafar lekin naye meharabaan terii vo ek nazar kar gaii asar duniyaa sanvar jaane lagii  kamoshiyaan gunagunaane lagiin tanhaaiyaan muskuraane lagiin ', 'correct_label': 'a r rahman', 'label': 0, 'split': 'test', 'title': 'kamoshiyaan gunagunaane lagiin', 'year': '2001'}`
- output: `{"pred": "a r rahman", "top3": ["a r rahman", "kalyanjianandji", "madan mohan"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='a r rahman' ref='a r rahman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='a r rahman' in top3=['a r rahman', 'kalyanjianandji', 'madan mohan']

### #385 — PASS

- item: `{'lyrics': '     arrr chhaii la la la laa sharamaaye kaahe  sharamaaye kaahe ghabaraaye kaahe  sun mere raajaa o raajaa aajaa aajaa  2 sharamaaye kaahe  o kuchh na soch matawaale o matawaale dil kii maan dilawaale o matawaale o dilawaale  duniyaa ke gam karataa hai kyuun milane kii raaten hain darataa hai kyuun  2 milane kii raaten hain darataa hai kyuun  sharamaaye kaahe aay dekho sharamaaye kaahe ghabaraaye kaahe  sun mere raajaa o raajaa aajaa aajaa sharamaaye kaahe  o kuchh na soch matawaale o matawaale dil kii maan dilawaale o matawaale o dilawaale  aankhon kaa ras pii le zaraa zulfon ke saaye men jii le zaraa  2 zulfon ke saaye men jii le zaraa   sharamaaye kaahe aay dekho sharamaaye kaahe ghabaraaye kaahe  sun mere raajaa o raajaa aajaa aajaa sharamaaye kaahe  o kuchh na soch matawaale o matawaale dil kii maan dilawaale o matawaale o dilawaale jaake ye din aane nahiin aa tujhako de duun main jannat yahiin  la la la laa  sharamaaye kaahe ghabaraaye kaahe  sun mere raajaa o raajaa aajaa aajaa sharamaaye kaahe sharamaaye kaahe ghabaraaye kaahe 2 sharamaaye kaahe ', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'sharamaaye kaahe ghabaraaye kaahe sun more raajaa', 'year': '1951'}`
- output: `{"pred": "s d burman", "top3": ["s d burman", "laxmikantpyarelal", "r d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='s d burman' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='s d burman' in top3=['s d burman', 'laxmikantpyarelal', 'r d burman']

### #386 — FAIL

- item: `{'lyrics': '  aa tiin kanastar piitpiit kar galaa phaad kar chillaanaa yaar mere mat buraa maan ye gaanaa hai na bajaanaa hai tiin kanastar piitpiit kar threedots  naach ke badale kamar nachaanaa uchhal ke sarkas dikhalaanaa bhuul hai terii tuu samajhaa hai duniyaa paagalakhaanaa hai tiin kanastar piitpiit kar threedots  udhar se lekar idhar jamaa kar kab tak kaam chalaaoge kisakaa rahaa zamaanaa ik din mahafil se uth jaaoge 2 nakal kaa dhandhaa chal nahiin sakataa ik din to pachhataanaa hai yaar mere mat buraa threedots  bhuul gayaa tuu taanasen kii taan yahii par guunjii thii sur ke jaaduugar baijuu kii shaan yahiin par guunjii thii mar ke amar hai sahagal usakaa har koii diivaanaa hai har koii diivaanaa hai mar ke amar hai sahagal usakaa yaar mere mat buraa threedots ', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'aa tiin kanastar piitpiit kar galaa phaad kar chillaanaa', 'year': '1959'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "shankarjaikishan", "naushad"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='shankarjaikishan' in top3=['laxmikantpyarelal', 'shankarjaikishan', 'naushad']

### #387 — FAIL

- item: `{'lyrics': '  ra \tna ruutho na ruutho na ruutho merii jaan \tisii bahaane aaj teriimerii ho gaii pahachaan aa \tmain ruuthuungii tumase ruuthuungii main ruuthuungii tumase \tmeraa dil chhiinakar bhii banate ho jaise koii anajaan ra \tna ruutho threedots aa \tmain ruuthuungii threedots  ra \ttumhaare ruuthane se zindagaanii ruuth jaaegii \tna phir aisaa samaan hogaa na qismat jagamagaaegii \tzaraa sii baat kaa aakir banaatii ho kyon afasaanaa \tye dil kaa raaz hai dil men rakho mere dilabar jaanaan 2 \tna ruutho threedots aa \tmain ruuthuungii threedots  \tchhupaayaa raazedil mujhase mujhe tumase shiqaayat hai \ttumhen usakii kabar kyaa hai ki jo kuchh dil kii haalat hai \ttumhaarii berukii ne haay mujhako maar daalaa hai \tbadii mushqil se maine ye dilenaadaan sambhaalaa hai 2 ra \tna ruutho threedots aa \tmain ruuthuungii threedots  ra \tchalo achchhaa huaa ulajhan dilon kii rang le aaii \tkushii aankhon men chamakii hai hansii honthon pe laharaaii aa \tladaaii aisii achchhii hai ki jisamen pyaar ho jaae \tumar bhar saath rahane kaa abhii ikaraar ho jaae 2 ra \tna ruutho threedots aa \tmain ruuthuungii threedots ', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'na ruutho merii jaan  main ruuthuungii tumase', 'year': '1971'}`
- output: `{"pred": "kalyanjianandji", "top3": ["kalyanjianandji", "laxmikantpyarelal", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='kalyanjianandji' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='shankarjaikishan' in top3=['kalyanjianandji', 'laxmikantpyarelal', 'shankarjaikishan']

### #388 — PASS

- item: `{'lyrics': '  nashiilii raat hai saare chiraag gul kar do kushii kii raat men kyaa kaam jalane vaalon kaa  lo aayii milan kii raat suhaanii raat 2 nainon se kisii ke nain mile haathon men kisii kaa haath lo aayii milan kii threedots  dene ko mubaarakabaad tumhen ye chaandanii dar par aa hii gaii honthon pe vafaa ke giit lie ik chandra kiran sharamaa hii gaii jiivan men kitane rang bhare ye mehandii vaale haath lo aayii milan kii threedots  duniyaa ne to kyaakyaa nazar diyaa dulhan ko chamakataa nazaraanaa ham dil kaa shaguufaa laae hain anamol hai ye to diivaanaa kar liijie qubuul is dil ko rah jaaegii apanii baat lo aayii milan kii threedots ', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'nashiilii raat hai  lo aayii milan kii raat suhaanii raat', 'year': '1962'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "naushad", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='shankarjaikishan' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='shankarjaikishan' in top3=['shankarjaikishan', 'naushad', 'laxmikantpyarelal']

### #389 — PASS

- item: `{'lyrics': ' ho o o o  tum itane din baad mile tum itane din kahaan rahe jaanake jo anajaan bane koii husn kyaa kahe tumane jaanaa nahiin hamen pahachaanaa nahiin laa laa laa laa laa laa laa laa 2  bade afasos kii hai baat tumane to milaayaa bhii nahiin haath  bade afasos kii hai baat tumane to milaayaa nahiin haath  2 baithe ho aankh churaake dekho to aankh milaake hamako hai kyaa shikaayat ho puuchho to paas bulaake puuchh bhii lo naa are tumane jaanaa nahiin hamen pahachaanaa nahiin laa laa laa laa laa laa laa laa  tum itane din baad mile tum itane din kahaan rahe jaanake jo anjaan bane koii husn kyaa kahe are tumane hai jaanaa nahiin hamen pahachaanaa nahiin laa laa laa laa laa laa laa laa  koii nahiin thaa wo tum hii the koii nahiin thaa wo ham hii the he he koii nahiin thaa wo tum the koii nahiin thaa wo ham the ham tum men dostii thii siine men aag uthii thii jaane wo dillagii thii yaa dil kii lagii thii tumane hai jaanaa nahiin hamen pahachaanaa nahiin laa laa laa laa laa laa laa laa  tum itane din baad mile tum itane din kahaan rahe jaanake jo anjaan bane koii husn kyaa kahe are tumane jaanaa nahiin hamen pahachaanaa nahiin laa laa laa laa laa laa laa laa ', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'tum itane din baad mile', 'year': '1979'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "kalyanjianandji", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='r d burman' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='r d burman' in top3=['r d burman', 'kalyanjianandji', 'shankarjaikishan']

### #390 — FAIL

- item: `{'lyrics': '  mu  qismat men bichhadanaa thaa       huii kyon unase mulaaqaat re  gii na rukati mujhase pyaar ke       mera dil nahiin mere haath re  mu  qismat men bichhadana tha huii kyon unase mulaaqaat re   gii tuu kaun hai ye maaluum nahiin      tuu kaun hai ye maaluum nahiin       phir dil kyon tujhe bulaataa hai       taqadiir ne chhodaa saath magar       tuu chhod na meraa saath re  mu  qismat men bichhadanaa thaa huii kyon unase mulaaqaat re   mu  main apanaa sab kuchh kho baithaa      main apanaa sab kuchh kho baithaa       kyaa pyaar men teraa bicchadaa re  gii tuu aake dekh ik baar hai merii       aankhon men barasaat re mu  qismat men bichhadanaa thaa huii kyon unase mulaaqaat re   mu  yaad aake na rastaa rok meraa      yaad aake na rastaa rok meraa       mujhe jaane de mujhe jaane de gii ik baar laut ke aa thaam le       aakar meraa haath re mu  qismat men bichhadanaa thaa huii kyon unase mulaaqaat re   ', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'qismat men bichhadanaa thaa', 'year': '1949'}`
- output: `{"pred": "c ramchandra", "top3": ["c ramchandra", "madan mohan", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='c ramchandra' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='s d burman' in top3=['c ramchandra', 'madan mohan', 'laxmikantpyarelal']

### #391 — FAIL

- item: `{'lyrics': '     na sochaa thaa ye 2 dil lagaane se pahale 2 ke tuutegaa dil 2 muskuraane se pahale 2  ummidon kaa suuraj 2 naa chamakaa naa duubaa 2 gahan pad gayaa 2 jagamagaane se pahale 2  na sochaa thaa ye 2 dil lagaane se pahale 2  agar gam uthaanaa 2 thaa qisamat men apanii 2 kushii kyuun milii 2 gam uthaane se pahale 2  na sochaa thaa ye 2 dil lagaane se pahale 2  kaho bijaliyon se 2 na dil ko jalaayen 2 mujhe phuunk den 2 ghar jalaane se pahale 2  na sochaa thaa ye 2 dil lagaane se pahale 2 ', 'correct_label': 'naushad', 'label': 6, 'split': 'test', 'title': 'na sochaa thaa ye dil lagaane ke pahale', 'year': '1950'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "c ramchandra", "naushad"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='naushad'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='naushad' in top3=['laxmikantpyarelal', 'c ramchandra', 'naushad']

### #392 — PASS

- item: `{'lyrics': '  ko \t chaandanii raat hai \thaay kyaa baat hai \tdekho jii dekho jii dekhodekho jii  3 u \tho  u \tmere bhole piyaa \to mere bhole piyaa \to bhuul jaiyo na priit lagaa ke ko \tmere bhole piyaa \to mere bhole piyaa \to bhuul jaiyo na priit lagaa ke  u \thai ye duniyaa paapii ko \thai ye duniyaa paapii u \tro ke kahe ye moraa jii ko \tro ke kahe ye moraa jii \tmoraa jii u \tkahiin nagarii naa dil kii ujad na jaaye merii \tjaavo naa aankh churaa ke ko \tkahiin nagarii naa dil kii ujad na jaaye merii \tjaavo naa aankh churaa ke  ko \t chaandanii raat hai \thaay kyaa baat hai \tdekho jii dekho jii dekhodekho jii  2 u \tho  u \tmaano merii baat balam ko \tmaano merii baat balam u \tdekho nikal jaaye na dam ko \tdekho nikal jaaye na dam u \taaj mere nanhen se dil pe nahiin dhaavo sitam \tbirahaa ke tiir chalaa ke ko \to \taaj mere nanhen se dil pe nahiin dhaavo sitam \tbirahaa ke tiir chalaa ke  u \tmere bhole piyaa \to mere bhole piyaa \to bhuul jaiyo na priit lagaa ke ko \tmere bhole piyaa \to mere bhole piyaa \to bhuul jaiyo na priit lagaa ke  ko \t chaandanii raat hai \thaay kyaa baat hai \tdekho jii dekho jii dekhodekho jii  3 u \tho ', 'correct_label': 'naushad', 'label': 6, 'split': 'test', 'title': 'chaandanii raat hai haay kyaa baat hai  mere bhole piyaa', 'year': '1949'}`
- output: `{"pred": "naushad", "top3": ["naushad", "c ramchandra", "s d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='naushad' ref='naushad'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='naushad' in top3=['naushad', 'c ramchandra', 's d burman']

### #393 — FAIL

- item: `{'lyrics': ' tujhase naaraaz nahiin zindagii hairaan huun main o hairaan huun main tere maasuum savaalon se pareshaan huun main o pareshaan huun main  jiine ke liye sochaa hii na thaa dard sambhaalane honge muskuraauun to muskuraane ke karz uthaane honge muskuraauun kabhii to lagataa hai jaise honthon pe karz rakhaa hai tujhase threedots  aaj agar bhar aaii hain buunden baras jaayengii kal kyaa pataa inake liye aankhen taras jaayengii jaane kahaan gum kahaan khoyaa ek aansuu chhupaake rakhaa thaa tujhase threedots  zindagii tere gam ne hamen rishte naye samajhaaye mile jo hamen dhuup men mile chhaanv ke thande saaye o tujhase threedots', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'tujhase naaraaz nahiin zindagii hairaan huun main', 'year': '1986'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "madan mohan", "r d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='r d burman' in top3=['laxmikantpyarelal', 'madan mohan', 'r d burman']

### #394 — FAIL

- item: `{'lyrics': '  jab ham javaan honge jaane kahaan honge lekin jahaan honge vahaan par yaad karenge tujhe yaad karenge threedots  ye bachapan kaa pyaar agar kho jaayegaa dil kitanaa khaaliikhaalii ho jaayegaa tere kayaalon se ise aabaad karenge tujhe yaad karenge threedots  aise hansatii thii vo aise chalatii thii chaand ke jaise chhupatii aur nikalatii thii sab se terii baaten tere baad karenge tujhe yaad karenge threedots  tere shabanamii kvaabon kii tasaviiron se terii reshamii zulfon kii zanjiiron se kaise ham apane aap ko aazaad karenge tujhe yaad karenge threedots  zahar judaaii kaa piinaa pad jaaye to bichhad ke bhii ham ko jiinaa pad jaaye to saarii javaanii bas yuun hii barbaad karenge tujhe yaad karenge threedots ', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'jab ham javaan honge', 'year': '1980'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "r d burman", "madan mohan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='r d burman' in top3=['laxmikantpyarelal', 'r d burman', 'madan mohan']

### #395 — FAIL

- item: `{'lyrics': '     bade suuramaa ban ke nikale the ghar se ke bijalii giraa denge guzaren jidhar se o shekhii rahii wo naa daavaa rahaa wo are ulajhe pade hain kisii kii nazar se  kahiye kaise hain mizaaj kahiye kaise hain mizaaj  kaise hain mizaaj kahiye kaise hain mizaaj bade kushanasiib ham hain aap aaye aaj jo aap aaye aaj  2  ye aap hii kaa ghar hai ghabaraaiye nahiin e jii ghabaraaiye nahiin sharm burii chiiz hai sharamaaiye nahiin e jii sharamaaiye nahiin le liijiye jo chaahiye aap hii kaa raaj 2  bade kushanasiib ham hain aap aaye aaj jo aap aaye aaj kaise hain mizaaj kahiye kaise hain mizaaj bade kushanasiib ham hain aap aaye aaj jo aap aaye aaj  kaatiir karuun kyaa aap kii batalaaiye huzuur e jii batalaaiye huzuur main to paa ke hain aap mujhase duur hain aap mujhase duur main aap kii is bedilii kaa kyaa karuun ilaaj 2  bade kushanasiib ham hain aap aaye aaj jo aap aaye aaj kaise hain mizaaj kahiye kaise hain mizaaj bade kushanasiib ham hain aap aaye aaj jo aap aaye aaj ', 'correct_label': 'c ramchandra', 'label': 2, 'split': 'test', 'title': 'bade suuramaa ban ke  kaise hain mizaaj kahiye', 'year': '1952'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "a r rahman", "r d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='c ramchandra'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='c ramchandra' in top3=['laxmikantpyarelal', 'a r rahman', 'r d burman']

### #396 — PASS

- item: `{'lyrics': ' ghaayal niraniyaa main banban doluun kisakaa lagaa baan 2 mukh se na boluun ghaayal hiraniyaa threedots  mud ke jo dekhuun to bachapan bulaae bulaae threedots mud ke jo dekhuun to bachapan bulaae palakon men lekin koii muskuraae jii ko dukhaauun ke pii sang ho luun ghaayal hiraniyaa main banban doluun  aa aa aa aa ho ho ho ho mm mm mm mm la la la laa  paa paa nii paa paa saa paa paa re maa dhaa paa saa dhaa re shh maa paa saa saa saa saa saa gaa re saa gaa re saa gaa re maa gaa re saa nii dhaa paa maa gaa gaa threedots re saa nii dhaa paa maa gaa re maa dhaa nii saa gaa re saa  jab se ye nainaa balam sang laage  jab se ye nainaa threedots balam sang laage  jab se ye nainaa balam sang laage  dukhsukh mere man men ik saath jaage pal men hansuun pal men nainaa bhigo luun ghaayal hiraniyaa main banban doluun  ghaa ghaa ghaa ghaa ghaa ghaa ghaa ghaa ghaayal hiraniyaa ban ban ban ban ban doluun na na na na na na na na na na na na boluun na doluun na boluun na daa daa daa daa daa daa daa daa daa daa daa daa doluun aa aa aa threedots ', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'ghaayal hiraniyaa main banban doluun', 'year': '0'}`
- output: `{"pred": "s d burman", "top3": ["s d burman", "annu malik", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='s d burman' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='s d burman' in top3=['s d burman', 'annu malik', 'laxmikantpyarelal']

### #397 — FAIL

- item: `{'lyrics': '  mahabuubaa terii tasviir kis tarah main banaauun 2 terii zulfon kii daastaan kis tarah main sunaauun mahabuubaa terii tasviir threedots  tere lie kahuun koii baat tere lie sochuun koii naam main to bas diivaanaa ho gayaa nahiin mere bas kaa ye kaam tere jaisaa koii kahiin dekhaa naa sunaa hai mahabuubaa threedots  dhaare maujen rut aur jaam nagmen paimaane but aur phuul sab terii raahon kii kaaq sab tere qadamon kii dhuul tere jaisaa koii kahiin dekhaa naa sunaa hai mahabuubaa threedots  nazaron ne dekhaa hai tujhe aataa nahiin phir bhii yaqiin kyonki merii duniyaa ke log hote nahiin itane hasiin tere jaisaa koii kahiin dekhaa naa sunaa hai mahabuubaa threedots ', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'mahabuubaa terii tasviir kis tarah main banaauun', 'year': '1970'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "r d burman", "kalyanjianandji"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='s d burman' in top3=['laxmikantpyarelal', 'r d burman', 'kalyanjianandji']

### #398 — FAIL

- item: `{'lyrics': ' arii o shokh kaliyon muskuraa denaa vo jab aaye  vo jab aaye adab se daaliyaan phuulon kii jhuk jaaye vo jab guzare chaman se qaafile bhanvaron ke ruk jaaye suno phuulon mahak apanii lutaa denaa vo jab aaye arii o shokh kaliyon muskuraa denaa   threedots  bahut taariif karatii hain ye kaliyaan baar baar usakii tamannaa hai ki main bhii dekh luun rangiin bahaar usakii havaaon tum naqaab usakii uthaa denaa vo jab aaye arii o shokh kaliyon muskuraa denaa   threedots  bagair usakii muhabbat ke main zindaa rah na paauungaa magar ye baat dil kii man kisii se kah na paauungaa nigaahon haaledil usako sunaa denaa vo jab aaye arii o shokh kaliyon muskuraa denaa   threedots ', 'correct_label': 'madan mohan', 'label': 5, 'split': 'test', 'title': 'arii o shokh kaliyon muskuraa denaa vo jab aaye', 'year': '1967'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "c ramchandra", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='shankarjaikishan' ref='madan mohan'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='madan mohan' in top3=['shankarjaikishan', 'c ramchandra', 'laxmikantpyarelal']

### #399 — PASS

- item: `{'lyrics': '      aisaa ho to kaisaa hogaa aap ho paas to din dhale paas ho aap to din chale  kisii din aisaa bhii to ho raat kii subah hii na ho  2 raat ke baad bhii raat ho aap ho aap ho paas to din dhale  kisii din honthon se kaho phuulon se jo kahaa tumane  2 aaj to phuulon kii raat ho aap ho aap ho paas to din dhale ', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'aisaa ho to kaisaa hogaa', 'year': '1979'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "a r rahman", "s d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='r d burman' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='r d burman' in top3=['r d burman', 'a r rahman', 's d burman']

### #400 — PASS

- item: `{'lyrics': '     ma \te jii o o \tkuchh to bolo \titanii kyuun hamase naaraaz ho aa \tmain tumhen jaan gaii \thato pahachaan gaii \tjaao jaao jii tum ho bade wo  ma  aisaa kyaa kasuur huaa gorii taabedaar se 2 aa  gairon se milate ho jii tum to bade pyaar se 2 ma  zaraa sii ye galatii hai \tajii ye to chalatii hai \tab to mem saab maaf kar do  aa \tmain tumhen jaan gaii \thato pahachaan gaii \tjaao jaao jii tum ho bade wo ma \te jii o o \tkuchh to bolo \titanii kyuun hamase naaraaz ho aa \tmain tumhen jaan gaii \thato pahachaan gaii \tjaao jaao jii tum ho bade wo  ma  jaise bhii ham hai tumhaare hain raanii 2 aa  haath meraa chhodiye jii badii meharabaanii 2 ma \tchhodo ye gussaa chhodo \tpuraanaa qissaa chhodo \te jii dil todo naa musakaraa do  aa \tmain tumhen jaan gaii \thato pahachaan gaii \tjaao jaao jii tum ho bade wo ma \te jii o o \tkuchh to bolo \titanii kyuun hamase naaraaz ho aa \tmain tumhen jaan gaii \thato pahachaan gaii \tjaao jaao jii tum ho bade wo  aa \tnaazuk hai dil meraa ab naa dukhaanaa 2 \twaranaa padegaa tumhen jii baad men pachhataanaa 2 ma \ttodenge naa pyaarii \tham to wafaadaarii \tjab bhii jii chaahe aazamaa lo  aa \tmain tumhen jaan gaii \thato pahachaan gaii \tjaao jaao jii tum ho bade wo ma \te jii o o \tkuchh to bolo \titanii kyuun hamase naaraaz ho aa \tmain tumhen jaan gaii \thato pahachaan gaii \tjaao jaao jii tum ho bade wo ', 'correct_label': 'c ramchandra', 'label': 2, 'split': 'test', 'title': 'e jii o o kuchh to bolo itanii kyuun hamase naaraaz ho', 'year': '1960'}`
- output: `{"pred": "c ramchandra", "top3": ["c ramchandra", "shankarjaikishan", "r d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='c ramchandra' ref='c ramchandra'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='c ramchandra' in top3=['c ramchandra', 'shankarjaikishan', 'r d burman']

### #401 — FAIL

- item: `{'lyrics': ' paisaa are money money lagataa hai apanaa bhii time fine hai bhaaii not pe not chhap rahele hain khushiyon kii baaraat hai paison kii barasaat hai sachche ho gae saare sapane khule nasiibaa yaar ke dene vaalaa jab bhii detaa detaa chhappar phaad ke kitii kitii kitanaa kitii kitii kitanaa dik taanaa dik taanaa tikanaa tikanaa  sab kahate hain hello hello saath hamaare chalo chalo sabako mujhase kaam hai duniyaa bhar men naam hai bangalaa bhii hai gaadii bhii hai mahakii mahakii baadii bhii hai dene vaalaa jab bhii threedots  miithaa hai jal jog kaa khaanaa chhappan bhog kaa saakii miinaa jaam hai pistaa hai baadaam hai sej sajii hai phuulon vaalii aane vaalii hai nakharaalii dene vaalaa jab bhii threedots  haan apanaa bhii style hai are haathon men mobile hai ha haa mujhako pakaden are mujhako chuumen aage piichhe pariyaan ghuumen dene vaalaa jab bhii threedots ', 'correct_label': 'annu malik', 'label': 1, 'split': 'test', 'title': 'khushiyon kii baaraat hai  dene vaalaa jab bhii detaa', 'year': '2000'}`
- output: `{"pred": "a r rahman", "top3": ["a r rahman", "annu malik", "madan mohan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='a r rahman' ref='annu malik'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='annu malik' in top3=['a r rahman', 'annu malik', 'madan mohan']

### #402 — FAIL

- item: `{'lyrics': ' sunii jo unake aane kii aahat gariibakaanaa sajaayaa hamane qadam mubaarak hamaare dar pe nasiib apanaa jagaayaa hamane  huii hai aamad kushaamadiidam ye kahanaa dil ko sikhaayaa hamane khile hain aashaa ke phuul man men ye raaz unase chhupaayaa hamane  vo apane netaa ham unakii janataa hameshaa naataa nibhaayaa hamane ye terii rahamat ai mere maalik gumaan nahiin thaa vo paayaa hamane  sunii jo unake threedots', 'correct_label': 'laxmikantpyarelal', 'label': 4, 'split': 'test', 'title': 'sunii jo unake aane kii aahat', 'year': '1978'}`
- output: `{"pred": "kalyanjianandji", "top3": ["kalyanjianandji", "shankarjaikishan", "madan mohan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='kalyanjianandji' ref='laxmikantpyarelal'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='laxmikantpyarelal' in top3=['kalyanjianandji', 'shankarjaikishan', 'madan mohan']

### #403 — FAIL

- item: `{'lyrics': ' laagaa gorii gujariyaa se nehaa hamaar hoi gavaa saaraa chaupat moraa rojagaar o  nain lad jainhe to manavaa men kasak hoibe karii prem kaa chhuti hai pataakhaa to dhamak hoibe karii nain lad jainhe   threedots  ruup ko manamaa basaibaa to buraa kaa hoii hai tohuu se priit lagaibaa to buraa kaa hoii hai prem kii nagarii ma kuchh hamaraa bhii haq hoibe karii nain lad jainhe   threedots  hoii gavaa man maa more tichhrii najar kaa hallaa gorii ko dekhe binaa nindiyaa na aavai hamakaa phaans lagii hai to karejavaa ma khatak hoibe karii nain lad jainhe   threedots  thaik thaik thai thai thai dhaak dhinak dhin taak tinak tin dhaak dhinak dhin dhaak dhinak dhin dhaa  aankh mil gayii hai sajaniyaa se to naachan lagii hai pyaar kii miithii gajal manavaa bhii gaavan lagii hai jhaanjh bajii hai to kamariyaa ma lachak hoibe karii nain lad jainhe   threedots  nainaa jab ladii hai to bhaiyyaa man men kasak hoibe karii thaik thaik tik thaa  hoy hoy hoy  man le gayii re dhobaniyaa raamaa kaisaa jaaduu daar ke kaisaa jaaduu daar ke re kaisaa tonaa daar ke man le gayii re dhobaniyaa raamaa kaisaa jaaduu daar ke man le gayii re dhobaniyaa raamaa kaisaa jaaduu daar ke ', 'correct_label': 'naushad', 'label': 6, 'split': 'test', 'title': 'nain lad jaii hai', 'year': '1961'}`
- output: `{"pred": "s d burman", "top3": ["s d burman", "shankarjaikishan", "madan mohan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='s d burman' ref='naushad'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='naushad' in top3=['s d burman', 'shankarjaikishan', 'madan mohan']

### #404 — PASS

- item: `{'lyrics': '  daaruu kii botal men saaheb paanii bharataa hai phir naa kahanaa michal daaruu pii kar dangaa karataa hai  shii shiish e kaisaa karataa aisaa kaahe ko hotaa dekh le jis din michal ko raat ko seth nahiin sotaa kud chorii karataa hai lekin chor se darataa hai phir naa kahanaa threedots  jangal men hain mor bade shahar men hain chor bade apane bhii ustaad yahaan pade hue aur bade phir naa kahanaa threedots  saalmahiine ke lie khaanepiine ke lie kitanaa paisaa chaahie aakir jiine ke lie log diivaane hain jo is paise pe marataa hai phir naa kahanaa threedots ', 'correct_label': 'laxmikantpyarelal', 'label': 4, 'split': 'test', 'title': 'daaruu kii botal men  phir naa kahanaa michal daaruu', 'year': '1974'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "annu malik", "r d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='laxmikantpyarelal' ref='laxmikantpyarelal'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='laxmikantpyarelal' in top3=['laxmikantpyarelal', 'annu malik', 'r d burman']

### #405 — PASS

- item: `{'lyrics': ' ye raat ye chaandanii phir kahaan sun jaa dil kii daastaan ye raatthreedots  pedon kii shaakhon pe soii soii chaandanii tere khayaalon men khoii khoii chaandanii aur thodii der men thak ke laut jaaegii raat ye bahaar kii phir kabhii na aaegii do ek pal aur hai ye samaa sun jaathreedots  laharon ke honthon pe dhiimaa dhiimaa raag hai bhiigii havaaon men thandii thandii aag hai is hasiin aag men tuu bhii jalake dekhale zindagii ke giit kii dhun badal ke dekhale khulane de ab dhadakanon kii zubaan sun jaathreedots  jaatii bahaaren hain uthatii javaaniyaan taaron ke chhaaon men pahale kahaaniyaan ek baar chal diye gar tujhe pukaarake lautakar na aaenge qaafile bahaar ke aajaa abhii zindagii hai javaan sun jaathreedots', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'ye raat ye chaandanii phir kahaan sun jaa dil kii daastaan', 'year': '-1'}`
- output: `{"pred": "s d burman", "top3": ["s d burman", "madan mohan", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='s d burman' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='s d burman' in top3=['s d burman', 'madan mohan', 'laxmikantpyarelal']

### #406 — FAIL

- item: `{'lyrics': ' tum hamase milo ham tumase milen logon ko manzuur nahiin manzuur nahiin  wo baat bhalaa phir kaise ho jo duniyaa kaa dastuur nahiin dastuur nahiin  honthon pe hansii laake apane ashqon ko chhupaayaa hai hamane aankhen bhii churaayii hai hamane daaman bhii bachaayaa hai hamane o  ye yaad rahe lekin tumako  majabuur hai ham magaruur nahiin  magaruur nahiin  tum hamase  duniyaa kii diivaaren lekin ye ulfat todake detii hai ye tuute dil tuute rishte ye qismat jod bhii detii hai o  jis din ham tum mil jaayenge  wo din shaayad ab duur nahiin duur nahiin  tum hamase ', 'correct_label': 'kalyanjianandji', 'label': 3, 'split': 'test', 'title': 'tum hamase milo ham tumase milen', 'year': '1970'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "r d burman", "kalyanjianandji"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='kalyanjianandji'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='kalyanjianandji' in top3=['laxmikantpyarelal', 'r d burman', 'kalyanjianandji']

### #407 — FAIL

- item: `{'lyrics': '   mere dil ko ye kyaa ho gayaa main naa jaanuun kahaan kho gayaa kyon lage din men bhii raat hai dhuup men jaise barasaat hai aisaa kyon hotaa hai baarbaar kyaa isako hii kahate hain pyaar  2  aa aa aa aa aa  ho sapane nae sajane lage duniyaa naii lagane lagii pahale kabhii aisaa naa huaa kyaa pyaas ye jagane lagii madahoshiyon kaa hai samaa vo jhukane lagaa aasamaan kaamoshii banii hai zubaan chhede hai koii daastaan dhadakan pe bhii chhaayaa hai kumaar aisaa kyon hotaa hai baarbaar  ho aaiine men jo dekhaa tujhako aaii sharam aankhen jhukiin dhak se meraa dhadakaa jiyaa ek pal ko ye saansen rukiin ab chuudii sataane lagii raaton ko jagaane lagii main yuunhii machalane lagii kuchhkuchh badalane lagii jaane rahatii huun kyon beqaraar aisaa kyon hotaa hai baarbaar  mere dil ko ye kyaa ho gayaa threedots kahate hain pyaar aisaa kyon hotaa hai baarbaar kyaa isako hii kahate hain pyaar ', 'correct_label': 'annu malik', 'label': 1, 'split': 'test', 'title': 'mere dil ko ye kyaa ho gayaa  aisaa kyon hotaa hai baarbaar', 'year': '2003'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "kalyanjianandji", "annu malik"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='annu malik'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='annu malik' in top3=['laxmikantpyarelal', 'kalyanjianandji', 'annu malik']

### #408 — PASS

- item: `{'lyrics': '  ki \tsultaanaa sultaanaa tuu na ghabaraanaa \tteremere pyaar ko kyaa rokegaa zamaanaa \ttod ke sab diivaaren tujhako le jaaegaa diivaanaa la \tsulemaan sulemaan tuu na ghabaraanaa \tteremere pyaar ko kyaa rokegaa zamaanaa \tshamaa usii mahafil men jalegii jisamen hogaa paravaanaa  \tterii ho jaauun main daudii chalii aauun \tmeraa naam le ke pukaaro to zaraa ki \tmain teraa ho jaauun jaanodil lutaauun \tkabhii apanii zulfen sanvaaro to zaraa la \tjab ye zulfen ki \tlaharaaen la \tkaale baadal ki \tchhaa jaaen la \ttaubaa ban jaae afasaanaa ki \tsultaanaa sultaanaa threedots  \tkyaa chup rahenge bhalaa ye kab kahenge \tke honthon pe apane rukii hai koii baat la \tduniyaa ne haay pahare hain lagaae \tabhii to hai mushkil hamaarii mulaakaat ki \tdushman mere la \tso jaaen ki \tjab andhere la \tho jaaen ki \tmere kvaabon men aa jaanaa \tsultaanaa sultaanaa threedots ', 'correct_label': 'laxmikantpyarelal', 'label': 4, 'split': 'test', 'title': 'sultaanaa sultaanaa tuu na ghabaraanaa  sulemaan sulemaan', 'year': '1965'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "kalyanjianandji", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='laxmikantpyarelal' ref='laxmikantpyarelal'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='laxmikantpyarelal' in top3=['laxmikantpyarelal', 'kalyanjianandji', 'shankarjaikishan']

### #409 — FAIL

- item: `{'lyrics': '     ketakii gulaab juuhii champakaban phuule 2 ritu basant apano kant godii garawaa lagaay jhulanaa men baith aaj pii ke sang jhuule ketakii gulaab juuhii champakaban phuule  galgal kuunjkuunj gungun bhanwaron kii guunj raagrang angang chhedat rasiyaa anang kuuyal kii pancham sun duniyaa dukh bhuule bhuule bhuule ketakii gulaab juuhii champakaban phuule ketakii gulaab juuhii ketakii gulaab juuhii champakaban phuule 2  ketakii gulaab juuhii champakaban phuule 2 ritu basant apano kant godii garawaa lagaay jhulanaa men baith aaj pii ke sang jhuule pii ke sang jhuule ketakii gulaab juuhii champakaban phuule  madhurmadhur thoriithorii miithii batiyon se gorii madhurmadhur thoriithorii madhurmadhur thoriithorii miithii batiyon se gorii chit churaaye hansat jaay 2 chorii kar sir jhukaaye siish jhukaaye chanchal lat gaalan ko chhuu le 2 ketakii gulaab juuhii champakaban phuule 2 ketakii gulaab juuhii  ketakii gulaab juuhii  ketakii gulaab juuhii ketakii ketakii ketakii ', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'ketakii gulaab juuhii champakaban phuule', 'year': '1956'}`
- output: `{"pred": "a r rahman", "top3": ["a r rahman", "madan mohan", "kalyanjianandji"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='a r rahman' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='shankarjaikishan' in top3=['a r rahman', 'madan mohan', 'kalyanjianandji']

### #410 — FAIL

- item: `{'lyrics': ' main ladakii po po po tuu ladakaa po po po ham donon milen po po po ab aage hogaa kyaa kuchh nahiin hogaa kuchh nahiin hogaa ham donon men bas ye hogaa  po po paa po po paa po po paa po po paa po po paa po po paa po po  main ladakaa po po po tuu ladakii po po po ham donon milen po po po ab aage hogaa kyaa kuchh nahiin hogaa threedots  paagalapan chhod de ye kasamen tod de ab rishtaa jod de yuun na baaten banaa kuchh aisaa soch naa jaaneman tok na raahon men rok naa aise mujhe naa phansaa main diivaanii terii dilajaanii nazar se nazar milaa jaa anjaanii na kar naadaanii na aise kariib aa dil de de po po po dil le le po po po kyuun bhaage po po po koii kaaran batalaa dil nahiin lenaa po po po dil nahiin denaa po po po bas yuun hii karate rahanaa po po po po po po   mastaanii shaam hai mastii kaa jaam hai kuchh tujhase kaam hai aa naa zaraa paas aa yuun jhuuthii baat men aauun naa ghaat men main tere haath men samajhuun iraadaa teraa he kuchh kar jaauun ke main mar jaauun samandar men kuud ke o jaanejaanaan na der lagaanaa mazaa to le duub ke main aauun po po po main jaauun po po po maan bhii jaa po po po ab aise naa tadapaa achchhaa baabaa maan gayaa main ruuth ke ab to aise naa jaa po po po po po po  main ladakaa threedots ', 'correct_label': 'annu malik', 'label': 1, 'split': 'test', 'title': 'main ladakii po po po tuu ladakaa  kuchh nahiin hogaa', 'year': '2000'}`
- output: `{"pred": "a r rahman", "top3": ["a r rahman", "annu malik", "s d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='a r rahman' ref='annu malik'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='annu malik' in top3=['a r rahman', 'annu malik', 's d burman']

### #411 — FAIL

- item: `{'lyrics': '  idhar to haath laa pyaare dikhaauun din ko bhii taare likhaa hai kyaa lakiiron men faqiiron se sun jaa re  likhaa hai tujhako to kisii se ulfat hai magar us zaalim ko tujhase nafarat hai vo chaahe auron ko ye terii qismat hai ye zaalim pyaar dikhalaataa hai kyaakyaa nazaare idhar to haath laa threedots  lakiiren kahatii hain ye tere haathon men ki teraa man ulajhaa hai aisii baaton men ki sonaa mushkil hai tujhe ab raaton men ye saare bhed khole hain lakiiron ne pyaare idhar to haath laa threedots  kiyaa hai jo tuune vahii paaegaa tuu burii hogii betaa jo chhipaaegaa tuu faqiiron se bach ke kahaan jaaegaa tuu terii qismat kii chaabii hai mere haathon men pyaare idhar to haath laa threedots ', 'correct_label': 'madan mohan', 'label': 5, 'split': 'test', 'title': 'idhar to haath laa pyaare dikhalaauun din ko bhii taare', 'year': '1958'}`
- output: `{"pred": "s d burman", "top3": ["s d burman", "naushad", "c ramchandra"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='s d burman' ref='madan mohan'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='madan mohan' in top3=['s d burman', 'naushad', 'c ramchandra']

### #412 — FAIL

- item: `{'lyrics': ' suno bhaaii hamane pii lii hai thodii 2 duniyaa kii baaton kii parawaa chhodii chaand aur taaron se mastii nichodii suno bhaaii hamane pii lii hai thodii 2  rahate hain ham to aazaad gam se 2 duniyaa waale darate hain ham se maanaa bure hain par dil to badaa hai hamane gariibon se taqadiir jodii suno bhaaii hamane pii lii hai thodii suno bhaaii hamane thodii sii pii hai  gaataa hai gaane dil kaa ye baajaa haa haa haa haa hii hii hii hii gaataa hai gaane dil kaa ye baajaa apanii hii dhun ke ham to hain raajaa laakhon tuufaan takaraae hamase jiine kii phir bhii aas na chhodii  suno bhaaii hamane pii lii hai thodii 2 duniyaa kii baaton kii parawaa chhodii chaand aur taaron se mastii nichodii suno bhaaii hamane pii lii hai thodii 2 ', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'suno bhaaii hamane pii lii hai thodii', 'year': '1961'}`
- output: `{"pred": "s d burman", "top3": ["s d burman", "a r rahman", "madan mohan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='s d burman' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='shankarjaikishan' in top3=['s d burman', 'a r rahman', 'madan mohan']

### #413 — PASS

- item: `{'lyrics': ' gaae jaa giit milan ke tuu apane lagan ke sajan ghar jaanaa hai  kaahe chhalake nainon kii gagarii kaahe barase jal tum bin suunii saajan kii nagarii paradesiyaa ghar chal pyaase hain diip nayan ke tere darshan ke sajan gharthreedots  lut na jaae jiivan kaa dheraa mujhako hai ye gam ham akele ye jag luteraa bichhaden na milake ham bigade nasiib na banake ye din jiivan ke sajan gharthreedots  dole nayanaa priitam ke dvaare milane kii ye dhun baalam teraa tujhako pukaare yaad aanevaale sun saathii milenge bachapan ke khilenge phuul man ke sajan gharthreedots', 'correct_label': 'naushad', 'label': 6, 'split': 'test', 'title': 'gaae jaa giit milan ke tuu apanii lagan ke sajan ghar jaanaa hai', 'year': '1948'}`
- output: `{"pred": "naushad", "top3": ["naushad", "s d burman", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='naushad' ref='naushad'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='naushad' in top3=['naushad', 's d burman', 'shankarjaikishan']

### #414 — FAIL

- item: `{'lyrics': '  zo \tudankhatole pe ud jaauun \ttere haath naa aauun \thaan aan aan \ttere haath naa aauun sha \tudankhatole pe ud jaauun \ttere haath naa aauun \thaan aan aan \ttere haath naa aauun  \tduurduur se karuun ishaare \taur tujhako tarasaauun \tchandaa kii khidakii se jhaakuun \tjhaakuun aur chhip jaauun do \tudankhatole pe ud jaauun \ttere haath naa aauun \thaan aan aan \ttere haath naa aauun  zo \tho o o o \taayen \taayen aur guzaratii jaayen \tlambiiuunchiiniichii raahen \tgaliyaan aur baazaar \thaan aan aan \tgaliyaan aur baazaar \tmeraa paiyaa \tmeraa paiyaa aise bhaage \tjaise motarkaar do \tbhaage sab sansaar 2  sha \tsuuraj bhaage chandaa bhaage \tandhiyaaraa ujiyaaraa bhaage \tdharatii daude piichhe ko \tmain aage badhatii jaauun zo \tteraa haath pakad ke tujhako \tduur kahiin le jaauun sha \tmain phir bhii haath na aauun  \tphir bhii haath na aauun  do \tudankhatole pe ud jaauun \ttere haath naa aauun \thaan aan aan \ttere haath naa aauun ', 'correct_label': 'naushad', 'label': 6, 'split': 'test', 'title': 'udankhatole pe ud jaauun', 'year': '1946'}`
- output: `{"pred": "madan mohan", "top3": ["madan mohan", "naushad", "r d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='madan mohan' ref='naushad'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='naushad' in top3=['madan mohan', 'naushad', 'r d burman']

### #415 — FAIL

- item: `{'lyrics': '      mere dil kii nagariyaa men aanaa na aa ke jaanaa balam paradesiyaa dil tadpaaye mohe chain na aae mohe ek jhalak dikhalaanaa dikhalaanaa mere dil kii threedots  rut milane kii aaii suhaanii aa jaao to badii maharbaanii gup chup gup chup duniyaa se chhup chhup main to aa gaii kar ke bahaanaa mere dil kii threedots  jis din se huii main tumahaarii miithii miithii sii mujhe beqaraarii pyaarii payaarii sii hai piid jiyaa dhare nahiin dhiir zaraa aa ke ise samajhaanaa mere dil kii threedots  dekho dekho jii hamen na sataao aanaa hai to ab aa jaao hamen badaa intezaar dil badaa beqaraar tumhen hamarii qasam zaraa aanaa mere dil kii threedots ', 'correct_label': 'madan mohan', 'label': 5, 'split': 'test', 'title': 'mere dil kii nagariyaa men aanaa', 'year': '1951'}`
- output: `{"pred": "s d burman", "top3": ["s d burman", "madan mohan", "naushad"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='s d burman' ref='madan mohan'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='madan mohan' in top3=['s d burman', 'madan mohan', 'naushad']

### #416 — FAIL

- item: `{'lyrics': '     gii \tmerii bahakii bahakii chaal \tmere resham se baal \tmerii zulfon ke jaal men naa aanaa naa aanaa ko \tdil ko bachaanaa raajaa dil ko bachaanaa 2  gii \tchandaa kii chaandanii se goraa goraa rang meraa 2 ko \tgoraa goraa rang meraa 2 gii \tkaliyon se naazuk baalamaa ang ang meraa 2 ko \tgoraa goraa rang meraa 2 gii \tmerii palaken zanjiir mere nainaa hain tiir \tmeraa khaalii naa jaaye nishaanaa \tnaa aanaa  ko \tdil ko bachaanaa raajaa dil ko bachaanaa 2 gii \tmerii bahakii bahakii chaal \tmere resham se baal \tmerii zulfon ke jaal men naa aanaa naa aanaa ko \tdil ko bachaanaa raajaa dil ko bachaanaa 2   gii \tpatalii kamar merii daalii gulaab kii 2 ko \tdaalii gulaab kii 2 gii \tchhodo jii chhodo ye baaten hain kwaab kii 2 ko \tbaaten hain kwaab kii 2 gii \tmain chaman kii bahaar thandii thandii phuhaar \tdekho dekho jii haath naa lagaanaa \tnaa aanaa  ko \tdil ko bachaanaa raajaa dil ko bachaanaa 2 gii \tmerii bahakii bahakii chaal \tmere resham se baal \tmerii zulfon ke jaal men naa aanaa naa aanaa ko \tdil ko bachaanaa raajaa dil ko bachaanaa 2 ', 'correct_label': 'c ramchandra', 'label': 2, 'split': 'test', 'title': 'merii bahakii bahakii chaal  dil ko bachaanaa raajaa', 'year': '1953'}`
- output: `{"pred": "s d burman", "top3": ["s d burman", "c ramchandra", "kalyanjianandji"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='s d burman' ref='c ramchandra'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='c ramchandra' in top3=['s d burman', 'c ramchandra', 'kalyanjianandji']

### #417 — FAIL

- item: `{'lyrics': '  kyaa buraa kiyaa hai huzuur maine haan thodii sii pii hai zaruur maine kyaa buraa kiyaa threedots  samajhatii hai duniyaa sharaabii mujhe yah kahatii hai kaanaakaraabii mujhe na jaane kyaa kiyaa qasuur maine haan thodii sii pii threedots  ye thodii sii piinaa balaa ho gayaa zamaanaa bhii mujhape kafaa ho gayaa yah pahalaa kiyaa hai qusuur maine kyaa buraa kiyaa hai threedots  kyaa qusuur kiyaa hai huzuur maine ', 'correct_label': 'kalyanjianandji', 'label': 3, 'split': 'test', 'title': 'kyaa buraa kiyaa hai huzuur maine haan thodii sii pii hai', 'year': '1960'}`
- output: `{"pred": "naushad", "top3": ["naushad", "annu malik", "c ramchandra"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='naushad' ref='kalyanjianandji'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='kalyanjianandji' in top3=['naushad', 'annu malik', 'c ramchandra']

### #418 — PASS

- item: `{'lyrics': '  ki \tmain tujhe pyaar karuungaa to terii yaad aaegii \tterii yaad aaegii to   \tdonon kisii ko nazar nahiin aae \tchal dariyaa men duub jaaen  la \tbaaqii abhii hain kitanii hii batiyaan \tbaith gae kyon pher ke ankhiyaan \thamaare nain milenge to dil dhadakenge \tdil dhadakenge to shole bhadakenge \tshole bhadakenge to aag lag jaaegii \taag lag jaaegii to to to ki \tkaise dilon kii aag bujhaaen \tchal dariyaa men threedots  \ttuune lagaayaa aankh men kajaraa \tkyuun nahiin baandhaa baalon men gajaraa \tterii zulf udegii to ghataa chhaa jaaegii \tghataa chhaa jaaegii to paanii barasegaa \tpaanii barasegaa to man tarasegaa \tman tarasegaa to to to la \tmuft men man ko kyon tadapaaen \tchal dariyaa men threedots do \tchal dariyaa men threedots ', 'correct_label': 'laxmikantpyarelal', 'label': 4, 'split': 'test', 'title': 'main tujhe pyaar karuungaa to  donon kisii ko nazar nahiin aae', 'year': '1975'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "shankarjaikishan", "madan mohan"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='laxmikantpyarelal' ref='laxmikantpyarelal'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='laxmikantpyarelal' in top3=['laxmikantpyarelal', 'shankarjaikishan', 'madan mohan']

### #419 — FAIL

- item: `{'lyrics': ' ho ho\taah haathreedots jiyaa o jiyaa o jiyaa kuchh bol do are o dil kaa pardaa khol do   2 aah haa aathreedots jab pyaar kisii se hotaa hai to dard saa dil men hotaa hai tum ek hasiin ho laakhon men bhalaa paake tume koi khota hai jiyaa o jiyaa o jiyaa kuchha bol do\t  nazaron se kitane tiir chale chalane do jigar par jhelenge in pyaar kii ujalii raahon par ham jaana ki baazii khelenge in do nainon ke saagar men koi dil kii naiyaa dubotaa hai o jiyaa o jiyaa o jiyaa kuchha bol do are o dil ka pardaa khol do threedots  tum bhii to is aag men jalte ho chehare se bayaan ho jaataa hain har baat pe aahen bharate ho har baat pe dil tharraataa hai\t jab dil pe chhuriyaan chalati hain to chain se koi sotaa hai jiyaa o jiyaa o jiyaa kuchha bol do are o dil kaa pardaa khol do', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'jiyaa o jiyaa o jiyaa kuchha bol do', 'year': '0'}`
- output: `{"pred": "naushad", "top3": ["naushad", "shankarjaikishan", "c ramchandra"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='naushad' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='shankarjaikishan' in top3=['naushad', 'shankarjaikishan', 'c ramchandra']

### #420 — FAIL

- item: `{'lyrics': '  kahanaa ik diivaanaa terii yaad men aahen bharataa hai likh kar teraa naam zamiin par us ko sajade karataa hai  shaakh girebaan khaaq basar phirataa hai suunii raahon men saayon ko lipataataa hai aur lailaa lailaa karataa hai  terii ek jhalak kii khaatir jaan aankhon men atakii hai jii kaa aisaa haal huaa hai jiitaa hai na marataa hai  kud ko bhuul gayaa hai lekin terii yaad nahiin bhuulaa dil ke jitane zakm hain un men teraa hii aqs ubharataa hai likh kar teraa naam zamiin par threedots  kahanaa mere diivaane se lailaa terii amaanat hai terii baahon men dam degii tuu jis kaa dam bharataa hai dil ke jitane zakm hain un men teraa hii aqs ubharataa hai  sadake jaauun is qaasid par jis se ye paigaam milaa meraa qaatil meraa masiihaa ab bhii mujh par marataa hai meraa qaatil meraa masiihaa meraa masiihaa meraa qaatil meraa qaatil meraa masiihaa ab bhii mujh par marataa hai  lailaa lailaa lailaa lailaa ', 'correct_label': 'madan mohan', 'label': 5, 'split': 'test', 'title': 'kahanaa ik diivaanaa terii yaad men aahen bharataa hai', 'year': '1976'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "annu malik", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='r d burman' ref='madan mohan'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='madan mohan' in top3=['r d burman', 'annu malik', 'shankarjaikishan']

### #421 — FAIL

- item: `{'lyrics': ' jaa re badaraa bairii jaa re jaa re piyaa kaa sandesavaa laa re laa re laa re jaa re badaraa bairii jaa re jaa re  pii ke daras ko jiyaraa tarase pii kii khabariyaa laa re laa re laa re jaa re   threedots  kahiyo sajan se man kii batiyaa ro ro haal sunaa jaa re   threedots  baat takat morii haarii najariyaa kab aayenge saanvariyaa mohe kyon sataaye paapii shor machaaye jaa re moraa saanvariyaa laa re laa re laa re jaa re   threedots ', 'correct_label': 'madan mohan', 'label': 5, 'split': 'test', 'title': 'jaa re badaraa bairii jaa re', 'year': '1960'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "shankarjaikishan", "naushad"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='r d burman' ref='madan mohan'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='madan mohan' in top3=['r d burman', 'shankarjaikishan', 'naushad']

### #422 — FAIL

- item: `{'lyrics': ' lataa  phuul hai bahaaron kaa baag hai nazaaron kaa aur chaand hotaa hai sitaaron kaa meraa tuu tuu hii tuu  rafii  haan mauj hai kinaaron kii raat beqaraaron kii aur rimajhim saavan kii phuhaaron kii merii tuu tuu hii tuu  kabhii kahiin main kho jaauun kahaan dhuundhe kahaan jaae meraa pataa phir tuu kisase puuchhe  lataa  jisake jii men tuu basaa hai jisake dil men tuu chhupaa hai vo tujhe galiyon men kyuun dhuundhe vo tujhe galiyon men kyuun dhuundhe  rafii  haa haa jaam hai mastaane kaa ishq hai diivaane kaa aur tiir hotaa hai nishaane kaa merii tuu tuu tuu tuu hii tuu  lataa  o diivaane mainne aisaa kyaa kahaa hai kyaa huaa hai tuune dil kyuun thaam liyaa hai  rafii  o hasiinaa kyaa bataauun tere dil ne mere dil ko pyaar bharaa paigaam diyaa hai haa haa  lataa  riit hai zamaane kii baat hai fasaane kii aur shammaa hotii hai paravaane kii meraa tuu tuu hii tuu  rafii   haa mauj hai kinaaron kii threedots  lataa  meraa tuu tuu hii tuu', 'correct_label': 'laxmikantpyarelal', 'label': 4, 'split': 'test', 'title': 'phuul hai bahaaron kaa baag hai nazaaron kaa', 'year': '1969'}`
- output: `{"pred": "kalyanjianandji", "top3": ["kalyanjianandji", "s d burman", "annu malik"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='kalyanjianandji' ref='laxmikantpyarelal'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='laxmikantpyarelal' in top3=['kalyanjianandji', 's d burman', 'annu malik']

### #423 — PASS

- item: `{'lyrics': ' 1 milan  nava madiraa jaisii anchakhii nava madiraa jaisii angiindhaa muurtii jaane kisakii milan raat par chamakegii ye banjyotii aa aa aa  kaun ho tum kaun ho 2 kaun ho  kavi kii madhur kalpanaa ho tum yaa gaayak kii madhurim taan yaa saritaa jal kii tarang ho arun kamal kii madhu muskaan  kaun ho tum kaun ho 2 kaun ho  ritu basant kii pratham kalii ho saavan kii pahalii barasaat yaa chir virahii do hridayon ke madhur milan kii pahalii raat  kaun ho tum kaun ho 2 kaun ho  pranaya giit kii pratham pankti ho yaa manu kii pahalii santaan nav yauvan kii pratham drishtii ho nayanon kii pahalii pahachaan  kaun ho tum kaun ho 2 kaun ho  2 viraha  kaun ho tum kaun ho o o aa aa aa kaun ho tum kaun ho 2 kaun ho  tum ashaadh kii prathama ghataa ho  yaa pahalaa bijalii kaa baan 2 yaa rimajhim pahalii puhaar kii 2 virahii nayan kii ashru samaan  kaun ho tum kaun ho 2 kaun ho  vikal sindhu men karun bindu ho 2 ghan ghuunghat men indu samaan muuk hridaya kii chhupii huuk ho 2 dukhii jagat ke kampit praan  kaun ho tum kaun ho 2 kaun ho', 'correct_label': 'c ramchandra', 'label': 2, 'split': 'test', 'title': 'kaun ho tum kaun ho', 'year': '1961'}`
- output: `{"pred": "c ramchandra", "top3": ["c ramchandra", "s d burman", "a r rahman"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='c ramchandra' ref='c ramchandra'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='c ramchandra' in top3=['c ramchandra', 's d burman', 'a r rahman']

### #424 — PASS

- item: `{'lyrics': ' jogan jogan tuu jogii main huun jogan jogan main tere kaaran tujhape vaaruun main tan man ghuumenge chal ham sang men rang le mujhako apane hii rang men jogan jogan threedots  tuu raajaa main huun raanii tuu mast main mastaanii tuu dilabar main diivaanii tuu kyaa hai main pahachaanii tuu hii dil kii dhadakan hai tuu hii meraa saajan hai man hai meraa terii umang hai rang le mujhako threedots  aajaa re sajanaa tuu more anganaa sulage ye tan chale puravaa vo sanan sanan sun le more sajan paayal kii chhanan chhanan tohe pukaare ye kanganaa bhii khanan khanan maine tere hii lie jog liyaa hai tere lie hii man kaa rog liyaa hai kahataa hai ye paagalapan milake bhii huun main birahan ab thaamaa hai jo daaman aag lagaa de tuu ang ang men rang le mujhako threedots  na mujhase pyaar kar itanaa diivaanii ke ho mashahuur duniyaa men kahaanii ke ik ladakii bhulaa ke apanaa tanaman hai apane ghar se nikalii ban ke jogan mohabbat men vo aisii kho gaii hai ki lailaa se vo majanuu ho gaii hai tuu jogii main huun threedots ', 'correct_label': 'annu malik', 'label': 1, 'split': 'test', 'title': 'jogan jogan tuu jogii main huun jogan', 'year': '2002'}`
- output: `{"pred": "annu malik", "top3": ["annu malik", "laxmikantpyarelal", "naushad"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='annu malik' ref='annu malik'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='annu malik' in top3=['annu malik', 'laxmikantpyarelal', 'naushad']

### #425 — FAIL

- item: `{'lyrics': ' ai mere vatan ke logon tum khuub lagaa lo naaraa ye shubh din hai ham sab kaa laharaa lo tirangaa pyaaraa par mat bhuulo siimaa par viiron ne hai praan ganvaae kuchh yaad unhen bhii kar lo 2 jo laut ke ghar na aaye 2  ai mere vatan ke logon  zaraa aankh men bhar lo paanii jo shahiid hue hain unakii zaraa yaad karo qurabaanii \t jab ghaayal huaa himaalay khatare men padii aazaadii jab tak thii saans lade vo phir apanii laash bichhaa dii sangiin pe dhar kar maathaa  so gaye amar balidaanii jo shahiidthreedots  jab desh men thii divaalii vo khel rahe the holi jab ham baithe the gharon men vo jhel rahe the golii the dhanya javaan vo aapane thii dhanya vo unakii javaanii jo shahiidthreedots  koii sikh koii jaat maraathaa koii gurakhaa koii madaraasii sarahad par maranevaalaa  har viir thaa bhaaratavaasii jo khuun giraa pavrat par vo khuun thaa hindustaanii jo shahiidthreedots  thii khuun se lathpath kaayaa phir bhii banduuk uthaake dasdas ko ek ne maaraa phir gir gaye hosh ganvaa ke jab antsamay aayaa to kah gaye ke ab marate hain khush rahanaa desh ke pyaaron ab ham to safar karate hain kyaa log the vo divaane kyaa log the vo abhimaanii jo shahiidthreedots \t tum bhuul na jaao unako is liye kahii ye kahaanii jo shahiidthreedots  jay hindthreedots jay hind kii senaa 2 jay hind jay hind jay hind', 'correct_label': 'c ramchandra', 'label': 2, 'split': 'test', 'title': 'ai mere vatan ke logon zaraa aankh men bhar lo paanii', 'year': '-1'}`
- output: `{"pred": "madan mohan", "top3": ["madan mohan", "c ramchandra", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='madan mohan' ref='c ramchandra'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='c ramchandra' in top3=['madan mohan', 'c ramchandra', 'shankarjaikishan']

### #426 — FAIL

- item: `{'lyrics': ' panchhii banuun udatii phiruun mast gagan men aaj main aazaad huun duniyaa kii chaman men  hillorii hillorii threedots o threedots oho  o mere jiivan men chamakaa saveraa o mitaa dil se vo gam kaa andheraa o hare kheton men gaae koii laharaa   o yahaan dil par kisii kaa na bairaa rang bahaaron ne bharaa mere jiivan men\t2 aaj main aazaad huun duniyaa kii chaman men panchhii banuun threedots  aa threedots o dil ye chaahe bahaaron se kheluun o gorii nadiyaa kii dhaaron se kheluun o chaand suuraj sitaaron se kheluun o apanii baahon men aakaash le luun badhati chaluun gaati chaluun apanii lagan men\t2 aaj main aazaad huun duniyaa kii chaman men panchhii banuun threedots  hillorii hillorii threedots   o main to oduungii baadal kaa aanchal o main to pahanuungii bijalii kii paayal o chhiin luungii ghataaon se kaajal o meraa jiivan hai nadiyaa kii halachal dil se mere laharen uthen thandii pavan men 2 aaj main aazaad huun duniyaa kii chaman men panchhii banuun threedots ', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'panchhii banuun udatii phiruun mast gagan men', 'year': '1955'}`
- output: `{"pred": "naushad", "top3": ["naushad", "shankarjaikishan", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='naushad' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='shankarjaikishan' in top3=['naushad', 'shankarjaikishan', 'laxmikantpyarelal']

### #427 — FAIL

- item: `{'lyrics': ' dapran ko dekhaa tuune jab jab kiyaa shrringaar phuulon ko dekhaa tuune jab jab aai bahaar ek badanasiib huun main 3 mujhe nahin dekhaa ek baar  suuraj ki pahali kiranon ko dekhaa tuune alasaate hue raaton men taaron ko dekhaa sapanon men kho jaate hue yuun kisi na kisi bahaane 2 tuune dekhaa sab sansaar 2  dapran ko dekhaa tuune jab jab kiyaa shrringaar  kaajal ki qismat kyaa kahiye nainon men tuune basaayaa hai aanchal ki qismat kyaa kahiye tuune ang lagaayaa hai hasarat hi rahi mere dil men 2 banuun tere gale kaa haar 2  dapran ko dekhaa tuune jab jab kiyaa shrringaar', 'correct_label': 'kalyanjianandji', 'label': 3, 'split': 'test', 'title': 'darpan ko dekhaa tuune jab jab kiyaa shrringaar', 'year': '-1'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "kalyanjianandji", "naushad"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='kalyanjianandji'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='kalyanjianandji' in top3=['laxmikantpyarelal', 'kalyanjianandji', 'naushad']

### #428 — PASS

- item: `{'lyrics': '  chalo sahelii chalo re saathii o pakadopakado re ise na chhodo are bainyaa na modo zaraa thahar jaa bhaabhii jaa re saraabii kyaa ho raajaa galii men aajaa holii re holii bhang kii golii o nakhare vaalii duungii main gaalii o raaamuu kii saalii holii re holii  holii ke din dil khil jaate hain rangon men rang mil jaate hain gile shiqave bhuul ke dosto dushman bhii gale mil jaate hain  gorii tere rang jaisaa thodaa saa rang milaa luun aa tere gulaabii gaalon se thodaa saa gulaal churaa luun jaa re jaa diivaane tuu holii ke bahaane tuu chhed na mujhe besharam puuch le zamaane se aise hii bahaane se lie aur die dil jaate hain holii ke din dil threedots  yahii terii marazii hai to achchhaa tuu kush ho le paas aa ke chhuunaa naa mujhe chaahe duur se bhigo le hiire kii kanii hai tuu motii kii banii hai tuu chhuune se tuut jaaegii kaanton ke chhuune se phuulon se naazuknaazuk badan chhil jaate hain holii ke din dil threedots ', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'chalo sahelii  holii ke din dil khil jaate hain', 'year': '1975'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "laxmikantpyarelal", "annu malik"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='r d burman' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='r d burman' in top3=['r d burman', 'laxmikantpyarelal', 'annu malik']

### #429 — PASS

- item: `{'lyrics': '  hamen bas ye pataa hai vo bahut hii khuubasuurat hai lifaafe ke liye lekin pate kii bhii zaruurat hai  ham ne sanam ko kat likhaa kat men likhaa ai dilrubaa dil kii galii shaharevafaa ham ne sanam ko   threedots  pahunche ye kat jaane kahaan jaane bane kyaa daasataan us par raqiibon kaa ye dar lag jaaye unake haath gar kitanaa buraa anjaam ho dil muft men badanaam ho aisaa na ho aisaa na ho apane ye raat din ham ne sanam ko   threedots  piipal kaa ye pattaa nahiin kaagaz kaa ye tukadaa nahiin is dil ke ye aramaan hain is men hamaarii jaan hai aisaa gazab ho jaaye na raste men ye kho jaaye na ham ne badii taaqiid kii daalaa ise jab daak men ye daak baabuu se kahaa ham ne sanam ko   threedots  barason javaabeyaar kaa dekhaa kiye ham raastaa ek din vo kat vaapas milaa aur daakiye ne ye kahaa is daak khaane men nahiin saare zamaane men nahiin koii sanam is naam kaa koii galii is naam kaa koii shahar is naam kaa ham ne sanam ko   threedots ', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'ham ne sanam ko kat likhaa', 'year': '1982'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "kalyanjianandji", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='r d burman' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='r d burman' in top3=['r d burman', 'kalyanjianandji', 'laxmikantpyarelal']

### #430 — FAIL

- item: `{'lyrics': ' do nainan ke milan ko do nainaa bulaaen jab nainaa hon saamane to nainaa jhuk jaaen   o panchhii pyaare saanjha sakhaare  bole tuu kaun sii bolii bataa re  bole tuu kaun sii bolii  2   main to panchhii pinjare kii mainaa pankh mere bekaar  biich hamaare saat re saagar  kaise chaluun us paar 2 o panchhii pyaare threedots   phaagun mahiinaa phuulii bagiyaa  aam jhare amraaii main khidakii se chup chup dekhuun  ritu basant kii aaii 2  o panchhii pyaare threedots ', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'o panchhii pyaare', 'year': '1963'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "c ramchandra", "r d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='s d burman' in top3=['laxmikantpyarelal', 'c ramchandra', 'r d burman']

### #431 — FAIL

- item: `{'lyrics': ' dekh tere sansaar kii haalat kyaa ho gaii bhagavaan kitanaa badal gayaa inasaan kitanaa badal gayaa inasaan suuraj na badalaa chaand na badalaa naa badalaa re aasamaan kitanaa badal gayaa inasaan kitanaa badal gayaa inasaan  aayaa samay badaa bedhangaa aaj aadamii banaa lafangaa kahiin pe jhagadaa kahiin pe dangaa naach rahaa nar ho kar nangaa chhal aur kapat ke haathon apanaa bech rahaa iimaan kitanaa threedots  raam ke bhakt rahiim ke bande rachate aaj fareb ke phande kitane ye makkar ye andhe dekh liye inake bhii dhandhe inhiin kii kaalii karatuuton se banaa ye mulk mashaan kitanaa threedots  jo ham aapas men na jhagadate bane hue kyon khel bigadate kaahe laakhon ghar ye ujadate kyon ye bachche maan se bichhadate phuutphuut kar kyon rote pyaare baapuu ke praan kitanaa threedots ', 'correct_label': 'c ramchandra', 'label': 2, 'split': 'test', 'title': 'dekh tere sansaar kii haalat kyaa ho gaii bhagavaan', 'year': '-1'}`
- output: `{"pred": "madan mohan", "top3": ["madan mohan", "c ramchandra", "kalyanjianandji"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='madan mohan' ref='c ramchandra'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='c ramchandra' in top3=['madan mohan', 'c ramchandra', 'kalyanjianandji']

### #432 — FAIL

- item: `{'lyrics': ' ye kaun hansaa haa haa haa haa are kaun hansaa haa haa haa haa ye kaun hansaa haa haa haa haa are kaun hansaa uun huun huun aisaa lagaa mujhe  jaise merii galii men koii dhiire se aake  bade pyaar se pukaare meraa naam kaise haa haa haa haa  ye kaun hansaa haa haa haa haa are kaun hansaa haa aisaa lagaa mujhe  jaise merii galii men koii dhiire se aake  bade pyaar se pukaare meraa naam e haa haa haa haa ye kaun hansaa haa haa haa haa are kaun hansaa  kyaa kahuun kabhii aisii ho jaatii huun magan main to chup rahuun magar hansataa hai tan badan ye naa jaanuun kaise aa aa aa aa aa aa ye naa jaanuun kaise baithe baithe hii jaise apane hii chhue se gudagudii sii uthe hai mere raam aa haa haa haa haa  ye kaun hansaa haa haa haa haa are kaun hansaa haa haa haa haa  laa laa laa laa laa laa laa laa laa laa laa laa  ho koii naa ho lekin itanaa to hai zaruur main thahar thahar jaauun chal chalake thodii duur dhat kaisii huun main aa aa aa aa aa aa dhat kaisii huun main jab bhii chhaayen andhere lage piichhe se mere koii meraa dupattaa rahaa thaam uii maan haa haa haa haa  ye kaun hansaa main nahiin nahiin nahiin phir kaun hansaa kaun phir kaun hansaa main nahiin nahiin nahiin phir kaun hansaa kaun uun huun main nahiin haa haa haa haa ', 'correct_label': 'laxmikantpyarelal', 'label': 4, 'split': 'test', 'title': 'ye kaun hansaa are kaun hansaa', 'year': '1975'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "s d burman", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='r d burman' ref='laxmikantpyarelal'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='laxmikantpyarelal' in top3=['r d burman', 's d burman', 'shankarjaikishan']

### #433 — FAIL

- item: `{'lyrics': ' ki kush raho saathiyo tumhen chhodake ham chale 2 la tumhen chhodake ham chale hamen chhodake gam chale donon khush raho saathiyo threedots  la mujhe tere dukh ne sainyaan kitanaa rulaayaa hai ki mujhe tere prem ne gorii maut se bachaayaa hai la bahate bahate magar ye aaj aansuu tham chale donon kush raho saathiyo threedots  ki tumhen ham nahiin bhuulenge hamen tum bhulaanaa naa la milenge kabhii aashaa ke diipak bujhaanaa naa ki hansate hansate tumhaarii aankhen karake nam chale donon kush raho saathiyo threedots  ki gaii re judaaii aaiin prem kii ratiyaan la gaii re judaaii aaiin prem kii ratiyaan ki kisii aur ke mukhade pe thahare na ankhiyaan la tere mukh pe saanvariyaa mere nainaa jam chale donon kush raho saathiyo threedots', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'kush raho saathiyo tumhen chhodake', 'year': '1972'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "laxmikantpyarelal", "kalyanjianandji"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='r d burman' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='s d burman' in top3=['r d burman', 'laxmikantpyarelal', 'kalyanjianandji']

### #434 — FAIL

- item: `{'lyrics': ' ek ladakii thii kitanii sharmiili ho gaii re main kaisii rangiilii 2  naagin ban ke mujhase lipat gaii merii chunariyaa piiliipiilii 2  ek ladakii thii kitanii sharmiili ho gaii re main kaisii rangiilii  mere bachapan chhod de bainyaan meraa yauvan meraa sainyaan  haath men usake haath main de duun aage jiivan bhuulbhulaiyaan  dil kii galiyon men aaye banjaare bech rahe vo sapane kunvare  chhedii kisane bansii pe dhun suriilii  ek ladakii thii kitanii sharmiili ho gaii re main kaisii rangiilii  chhanchhan  chuudiyaan haathon men khankhan paayalen raaton men chhanchhan  jal gaii re barasaaton men aa gaii dil kii baaton men  chuudiyaan haathon men khankhan paayalen raaton men chhanchhan jal gaii re barasaaton men aa gaii dil kii baaton men  ha  naam kaa saavan buundbuund barase patajhad jaisaa ye man tarase  kaisii badan men aag lagii ye main to aa gaii baahar ghar se  kaare badaraa tuu mujhako bhigo de duub jaauun main mujhako dubo de  kaisii pyaarii rut hai ye miithii suriilii  ek ladakii thii kitanii sharmiili ho gaii re main kaisii rangiilii 2 naagin ban ke mujhase lipat gaii merii chunariyaa piiliipiilii 2 ek ladakii thii kitanii sharmiili ho gaii re main kaisii rangiilii chhanchhan  chuudiyaan haathon men khankhan paayalen raaton men chhanchhan jal gaii re barasaaton men aa gaii dil kii baaton men  3 ', 'correct_label': 'a r rahman', 'label': 0, 'split': 'test', 'title': 'ek ladakii thii kitanii sharmiili', 'year': '2001'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "a r rahman", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='r d burman' ref='a r rahman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='a r rahman' in top3=['r d burman', 'a r rahman', 'laxmikantpyarelal']

### #435 — FAIL

- item: `{'lyrics': ' mere anganaa aaye re ghanashyaam aaye re main ne saare hosh ganvaaye mere anganaa aaye re ghanashyaam threedots  laaj ke maare simatii jaauun aanchal hii se lipatii jaauun meraa aanchal ud ud jaaye mere anganaa aaye re ghanashyaam aaye re threedots  sudh budh khoii man ghabaraaye ik rang aaye ik rang jaaye man bairii bol sunaaye mere anganaa aaye re ghanashyaam aaye re threedots ', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'mere anganaa aaye re ghanashyaam aaye re', 'year': '1981'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "s d burman", "c ramchandra"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='shankarjaikishan' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='r d burman' in top3=['shankarjaikishan', 's d burman', 'c ramchandra']

### #436 — FAIL

- item: `{'lyrics': '     la \tsaanii re 6 \tghar ghar men ek chor saanii 2 \tghar ghar men ek chor \t ko \tsaanii re 4 \tghar ghar men ek chor saanii 2 \tghar ghar men ek chor la \tsaanii re  \ttuu bhaktii kaa diyaa jalaavaii \tchor bujhaavaii baatii \to \ttuu bhaktii kaa diyaa jalaavaii \tchor bujhaavaii baatii \tluut jaaye sab maal kazaanaa \tdin dekhe naa raatii re \tdin dekhe naa raatii \thaath kise ke aavaii naa wo 2 \tlaakh kare koii shor \tsaanii ghar ghar men ek chor 2  ko \tsaanii re 4 \tghar ghar men ek chor saanii 2 \tghar ghar men ek chor la \tsaanii re  \to \ttere dekhate ghar men aayaa \tghar men aayaa tere dekhate \tro le \tkaisaa jaaduu daalaa tujhape \ttuu kuchh bhii naa bole re \ttuu kuchh bhii naa bole \ttan man baandh liye hain donon 2 \tbaandh karam kii dor \tsaanii ghar ghar men ek chor 2  ko \tsaanii re 4 \tghar ghar men ek chor saanii 2 \tghar ghar men ek chor la \tsaanii re ', 'correct_label': 'c ramchandra', 'label': 2, 'split': 'test', 'title': 'saanii re ghar ghar men ek chor', 'year': '1952'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "c ramchandra", "a r rahman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='r d burman' ref='c ramchandra'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='c ramchandra' in top3=['r d burman', 'c ramchandra', 'a r rahman']

### #437 — PASS

- item: `{'lyrics': '  tum aaj mere sang hans lo tum aaj mere sang gaa lo aur hansategaate is jiivan kii ulajhii raah sanvaaro tum aaj mere threedots  shaam kaa suuraj bindiyaa ban kar saagar men kho jaae subahsavere vo hii suuraj aashaa lekar aae naii umangen naii tarangen aas kii jyoti jagaae re aas kii jyoti jagaae tum aaj mere threedots  dukh men jo gaae malhaar vo insaan kahalaae 2 jaise banshii ke siine men chhed hai phir bhii gaae gaategaate roe mayuuraa phir bhii naach dikhaae re phir bhii naach dikhaae tum aaj mere threedots ', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'tum aaj mere sang hans lo tum aaj mere sang gaa lo', 'year': '1962'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "naushad", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='shankarjaikishan' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='shankarjaikishan' in top3=['shankarjaikishan', 'naushad', 'laxmikantpyarelal']

### #438 — PASS

- item: `{'lyrics': ' gaadii bulaa rahii hai siitii bajaa rahii hai chalanaa hii zindagii hai chalatii hii jaa rahii hai  dekho vo rel bachchon kaa khel siikho sabak javaanon sar pe hai bojh siine men aag lab par dhuvaan hai jaano phir bhii ye jaa rahii hai nagamen sunaa rahii hai  aage tuufaan piichhe barasaat uupar gagan men bijalii soche na baat din ho ke raat siganal huaa ke nikalii dekho vo aa rahii hai dekho vo jaa rahii hai  aate hain log jaate hain log paanii me jaise rele jaane ke baad aate hain yaad guzare hue vo mele yaaden banaa rahii hai yaaden mitaa rahii hai  gaadii ko dekh kaisii hai nek achchhaa buraa na dekhe sab hain savaar dushman ke yaar sabako chalii ye leke jiinaa sikhaa rahii hai maranaa sikhaa rahii hai  gaadii kaa naam naa kar badanaam patarii pe rakh ke sar ko himmat na haar kar intazaar aa laut jaaen ghar ko ye raat jaa rahii hai vo subah aa rahii hai  sun ye paigaam ye hai sangraam jiivan nahiin hai sapanaa dariyaa ko faand pavart ko chiir kaam hai ye usakaa apanaa niinden udaa rahii hai jaago jagaa rahii hai', 'correct_label': 'laxmikantpyarelal', 'label': 4, 'split': 'test', 'title': 'gaadii bulaa rahii hai siitii bajaa rahii hai', 'year': '1974'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "shankarjaikishan", "s d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='laxmikantpyarelal' ref='laxmikantpyarelal'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='laxmikantpyarelal' in top3=['laxmikantpyarelal', 'shankarjaikishan', 's d burman']

### #439 — PASS

- item: `{'lyrics': ' aa paa paa paa paa paa       lo suno ki a bolo naa aa yahaan nahiin kahuungii ki  phir kahaan kahogii aa are yahaan naa     to to to phir kahaan kisi aur jagah aa haa aa haa chalo naa re lo suno suno naa to chalo chalo naa  ki dekho zaraa chaaron taraf yahaan wahaan       khile hue rang hain ruup hain phuul hain 2 aa bechain rahane lagii huun main haan       achchhaa lo kahane lagii huun main      yahaan nahiin   ki thandii hawaa mastii men aaii       ye uunche parabat chuumake jhuumake ghuumake 2 aa hai baraf kaisii gorii gorii        ye baat sunalo chorii chorii       yahaan nahiin   aa o bekabar use koii ladakii par bhii hai iqaraar kyaa prem kaa pyaar kaa 2 ki main ye ishaaraa samajhaa nahiin       matalab tumhaaraa samajhaa nahiin aa yahaan nahiin  ', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'yahaan nahiin kahuungii', 'year': '1973'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "s d burman", "annu malik"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='r d burman' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='r d burman' in top3=['r d burman', 's d burman', 'annu malik']

### #440 — FAIL

- item: `{'lyrics': ' teraa meraa pyaar amar phir kyon mujhako lagataa hai dar mere jiivan saathii bataa dil kyon dhadake rahrah kar  kyaa kahaa hai chaand ne jisako sunake  chaandanii har lahar pe jhuumake kyon ye naachane lagii chaahat kaa hai harasuu asar phir kyon mujhako lagataa hai dar  kah rahaa hai meraa dil ab ye raat na dhale khushiyon kaa ye silasilaa aise hii chalaa rahe tujhako dekhuun dekhuun jidhar phir kyon mujhako lagataa hai dar  hai shabaab par umang har khushii javaan hai merii donon baahon men jaise aasmaan hai chalatii huun main taaron par phir kyon mujhako lagataa hai dar', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'teraa meraa pyaar amar phir kyon mujhako lagataa hai dar', 'year': '1962'}`
- output: `{"pred": "annu malik", "top3": ["annu malik", "r d burman", "s d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='annu malik' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='shankarjaikishan' in top3=['annu malik', 'r d burman', 's d burman']

### #441 — FAIL

- item: `{'lyrics': '      chandaa maamaa bole taare bhii bole nazaare bhii bole tuu so jaa re  3  nahiin soye re kaahe roye re o munnaa chandaa maamaa bole taare bhii bole ham saare bole tuu so jaa re tuu so jaa re  are dekhe kaahe julmii choriichorii tere liye gaatii huun main lorii haay phans gaii merii jaan kahaan ye aake pad gaii kaisii haay gale men dorii dil ghabaraaye kaahe tadapaaye o munnaa  chandaa maamaa bole taare bhii bole nazaare bhii bole tuu so jaa re haan tuu so jaa re  main to jaagii huun diwaanii ho ke kyuun phir sabakii niind udhaaye ro ke din bhar to chupachaap rahaa tuu pyaare kuub nikaale ab rone ke mauke merii taubaa re kyaa hogaa re o munnaa  chandaa maamaa bole taare bhii bole nazaare bhii bole tuu so jaa re chandaa maamaa bole taare bhii bole ham saare bole tuu so jaa re haan tuu so jaa re 2 ', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'chandaa maamaa bole  tuu so jaa re', 'year': '1973'}`
- output: `{"pred": "s d burman", "top3": ["s d burman", "annu malik", "r d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='s d burman' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='r d burman' in top3=['s d burman', 'annu malik', 'r d burman']

### #442 — PASS

- item: `{'lyrics': '  ai husnpariicheharaa kyon itanii dardamand ho duniyaa kii manzilon par tum hii mujhe pasand ho  shabanam ke dil kii dhadakan mahasuus kar rahii ho tum kitanii narmdil ho aahen sii bhar rahii ho ai husnpariicheharaa threedots  itanaa kyaal koii karataa nahiin kisii kaa tumane badal diyaa hai ruk merii zindagii kaa ai husnpariicheharaa threedots  sab kuchh thaa paas mere lekin na ye kushii thii puurii huii hai tumase jiivan men jo kamii thii ai husnpariicheharaa threedots ', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'ai husnpariicheharaa kyon itanii dardamand ho', 'year': '1967'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "laxmikantpyarelal", "c ramchandra"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='shankarjaikishan' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='shankarjaikishan' in top3=['shankarjaikishan', 'laxmikantpyarelal', 'c ramchandra']

### #443 — PASS

- item: `{'lyrics': ' zindagii ek safar hai suhaanaa yahaan kal kyaa ho kisane jaanaa   2  hansate gaate jahaan se guzar duniyaa kii tuu paravaah na kar   2 muskuraate hue din bitaanaa yahaan kal kyaa ho kisane jaanaa haan zindagii ek safar threedots  maut aanii hai aaegii ik din jaan jaanii hai jaaegii ik din   2 aisii baaton se kyaa ghabaraanaa yahaan kal kyaa ho kisane jaanaa haan zindagii ek safar threedots  chaand taaron se chalanaa hai aage aasamaanon se badhanaa hai aage   2 piichhe rah jaaegaa ye zamaanaa yahaan kal kyaa ho kisane jaanaa haan zindagii ek safar threedots', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'zindagii ek safar hai suhaanaa', 'year': '-1'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "r d burman", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='shankarjaikishan' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='shankarjaikishan' in top3=['shankarjaikishan', 'r d burman', 'laxmikantpyarelal']

### #444 — FAIL

- item: `{'lyrics': ' ye afasaanaa nahiin zaalim mere dil kii haqiiqat hai mujhe tum se mohabbat hai mujhe tum se mohabbat hai ye afasaanaathreedots  lagii hai aag siine men nahiin kuchh lutf jiine men nazar kuchh kah nahiin sakatii kahe bin rah nahiin sakatii tumhen kayonkar main samajhaauun mujhe tum se mohabbat hai ye afasaanaathreedots  machaltii hain tamannaaen kahiin rusuvaa na ho jaaen musiibat uljhanen dil kii qayaamat dhadakanen dil kii tumhen kayonkar main samajhaauun mujhe tum se mohabbat hai ye afasaanaathreedots  na jiitii huun na maratii huun kalish mehasuus karatii huun kahiin aisaa na ho jaae kalii khilate hii murjhaae tumhen kayonkar main samajhaauun mujhe tum se mohabbat hai ye afasaanaathreedots', 'correct_label': 'naushad', 'label': 6, 'split': 'test', 'title': 'ye afasaanaa nahiin zaalim mere dil kii haqiiqat hai', 'year': '1947'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "madan mohan", "annu malik"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='shankarjaikishan' ref='naushad'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='naushad' in top3=['shankarjaikishan', 'madan mohan', 'annu malik']

### #445 — FAIL

- item: `{'lyrics': '  mile jo kadiikadii ek zanjiir bane pyaar ke rang bharo zindaa tasviir bane o hamasafar ban ke chalo to suhaanaa hai safar jo akelaa hii rahe use na mile dagar  yaar ke bin koii jie to kyaa jie zindagii hai muskaraane ke lie jo bhii yahaan pe saath kuchh jaataa nahiin ho mile jo kadiikadii threedots  chaahe aur kuchh na mujhe yaar de yaar tuu jii bhar ke mujhe pyaar de badii mushqil se bhalaa yaar milataa hai yahaan koii hamaraaz na ho to hai suunaa ye jahaan mile jo kadiikadii threedots  jaane ek din ye kaise ho gayaa chalatechalate main raahon men kho gayaa subah kaa bhuulaa huaa shaam ko ghar laut aae use bhuulaa na kaho yahii hai apanii raay mile jo kadiikadii threedots ', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'mile jo kadiikadii ek zanjiir bane', 'year': '1978'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "r d burman", "kalyanjianandji"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='r d burman' in top3=['laxmikantpyarelal', 'r d burman', 'kalyanjianandji']

### #446 — PASS

- item: `{'lyrics': ' tandaa naa ne taa naa ne aanand men 4  pyaare panchhii baanhon men gaatii koyal raahon men  dharatii pe yahii to kushii hai apanii duniyaa men aansuu bhii nahiin hain  pyaare panchhii baanhon men gaatii koyal raahon men dharatii pe yahii to kushii hai apanii duniyaa men aansuu bhii nahiin hain  chhotiichhotii kutiyaa men svarg hai yahaan  aur chhotechhote dil men bahataa pyaar kaa ye jharanaa  panchhii jo udanaa chaahe to pattaa kaahe kaa  ye pyaar hii kaafii hai gorii paisaavaisaa kyaa karanaa  pyaare panchhii baanhon men gaatii koyal raahon men dharatii pe yahii to kushii hai apanii duniyaa men aansuu bhii nahiin hain   aasamaanon men aanand mittii men bhii hai aanand  ye dharatii chiir ke ugane vaale ankur men aanand  dhuup kaa sardii men aanand nadii kaa varshaa men aanand  aur varshaa men badale bhuumi ke rangon men aanand  jiivan kaa ye aanand sau barason kaa aanand sajanii  duniyaa men har dil kii dhadakan men aanand aanand  pyaare panchhii baanhon men gaatii koyal raahon men dharatii pe yahii to kushii hai apanii duniyaa men aansuu bhii nahiin hain   terii saanson men rah ke dhalatii umar kaa aanand  tum agale janam men phir se milo to aur bhii aanand  thandii raaton men tere badan kii garmii kaa aanand  aur jiivan bhar jo tumane diyaa hai jiine kaa aanand  apanepan men aanand rishton men bhii aanand  chhalake auron kii kaatir jo aansuu hain aanand   pyaare panchhii baanhon men gaatii koyal raahon men dharatii pe yahii to kushii hai apanii duniyaa men aansuu bhii nahiin hain  2  chhotiichhotii kutiyaa men svarg hai yahaan aur chhotechhote dil men bahataa pyaar kaa ye jharanaa panchhii jo udanaa chaahe to pattaa kaahe kaa ye pyaar hii kaafii hai gorii paisaavaisaa kyaa karanaa  pyaare panchhii baanhon men gaatii koyal raahon men dharatii pe yahii to kushii hai apanii duniyaa men aansuu bhii nahiin hain ', 'correct_label': 'a r rahman', 'label': 0, 'split': 'test', 'title': 'pyaare panchhii baanhon men gaatii koyal raahon men', 'year': '1996'}`
- output: `{"pred": "a r rahman", "top3": ["a r rahman", "r d burman", "s d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='a r rahman' ref='a r rahman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='a r rahman' in top3=['a r rahman', 'r d burman', 's d burman']

### #447 — FAIL

- item: `{'lyrics': ' gii  aan milo aan milo shyaam saanvare threedots aan milo aan milo aan milo shyaam saanvare brij men akelii raadhe khoikhoi phire ma   o raadhe khoikhoi phire o kaanhaa aan milo gii ma  o threedots aan milo aan milo  threedots  gii  brindaavan kii galiyon men tum bin jiyaraa naa laage ma   o threedots jiyaraa naa laage gii  nis din tumhaarii baat dekhe vyaakul nainaa bhaage ma  vyaakul naina bhaage threedots gii  ab hii aisii dashaa hai man kii kyaa hovai phir aage re brij men akelii raadhe khoikhoi phire ma  o raadhe khoikhoi phire o kaanhaa aan threedots  gii  aaj na kaahe jamunaa tiire muralii madhur bajaai ma  o threedots muralii madhur bajaai gii  aaj na kaahe sakhiyaan ke sang hilmil raas rachaai ma  o threedots milmil raas rachaai gii  hamaara aangan chhod ke tohe kaun nagariyaa bhaai re brij men akelii  threedots  gii  ajahun na bheje re mohan taine koi khabariyaa 2 ma  o threedots taine koi khabariyaa gii  ho gai hai ye brij ki baalaa roro kar baavariyaa ma  roro kar baavariyaa gii  dhiir bandha jaa threedots dhiir bandh jaa mukh dikhalaa jaa nat naagar saanvariyaa re brij men akelii raadhe threedots', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'aan milo aan milo shyaam saanvare aan milo', 'year': '1955'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "shankarjaikishan", "kalyanjianandji"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='s d burman' in top3=['laxmikantpyarelal', 'shankarjaikishan', 'kalyanjianandji']

### #448 — FAIL

- item: `{'lyrics': ' gam diye mustaqil itanaa naazuk hai dil ye na jaanaa haay haay ye zaalim zamaanaa  de uthe daag lo unase ai mahalon kah sunanaa haay haay ye zaalim zamaanaa  dil ke haathon se daaman chhudaakar gam kii nazaron se nazaren bachaakar uthake vo chal diye kahate hii rah gaye ham fasaanaa haay haay ye zaalim zamaanaa  koii merii ye ruudaad dekhe ye mohabbat kii bedaad dekhe phuuk rahaa hai jigar pad rahaa hai magar muskuraanaa haay haay ye zaalim zamaanaa  gam diye mustaqil itanaa naazuk hai dil ye na jaanaa haay haay ye zaalim zamaanaa ', 'correct_label': 'naushad', 'label': 6, 'split': 'test', 'title': 'gam diye mustaqil itanaa naazuk hai dil ye na jaanaa', 'year': '1946'}`
- output: `{"pred": "s d burman", "top3": ["s d burman", "shankarjaikishan", "madan mohan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='s d burman' ref='naushad'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='naushad' in top3=['s d burman', 'shankarjaikishan', 'madan mohan']

### #449 — FAIL

- item: `{'lyrics': '  saaqii saaqii dil bujh hii gayaa hai siine men kuchh lutf nahiin ab jiine men saaqii saaqii   saaqii tere jaam wo jaam nahiin kyaa rakhaa hai ab piine men  2 saaqii saaqii  saaqii pahalii sii baat nahiin pahale din pahalii raat nahiin jab teraa hii wo haath nahiin 2 kyaa rakhaa hai phir siine men saaqii saaqii  ab saawan ke din biit gaye ham haar gaye tum jiit gaye saaqii jab chhod ke miit gaye 2 kuchh lutf nahiin phir jiine men saaqii saaqii  dil bujh hii gayaa hai siine men kuchh lutf nahiin ab jiine men saaqii saaqii ', 'correct_label': 'naushad', 'label': 6, 'split': 'test', 'title': 'saaqii saaqii dil bujh hii gayaa hai siine men', 'year': '1944'}`
- output: `{"pred": "c ramchandra", "top3": ["c ramchandra", "naushad", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='c ramchandra' ref='naushad'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='naushad' in top3=['c ramchandra', 'naushad', 'laxmikantpyarelal']

### #450 — PASS

- item: `{'lyrics': '  nain milaakar chain churaanaa kisakaa hai ye kaam 2 hamase puuchho hamako pataa hai us zaalim kaa naam 2 nain milaakar chain threedots  vo aayaa to kho gaii ye saarii mahafil dekhaa is andaaz se sab kho baithe dil thodaa saa vo meharabaan thodaa saa qaatil vo jisakii har ek adaa par laakhon hain ilzaam hamase puuchho hamako threedots  kisakaa gussaa hai bhalaa jisape aae pyaar aisaa dushman haay re jisako samajhe yaar socho to vah kaun hai sharmiilaa diladaar 2 jisakii mast nashiilii nazaren aisii jaise jaam 2 hamase puuchho hamako threedots  jaagiijaagii sii zaraa kuchh soiisoii 2 aankhen bhii us shokh kii hain khoiikhoii 2 sholaa hai vo phuul hai yaa sapanaa koii 2 jisakii kaatir koii bhii ho sakataa hai badanaam hamase puuchho hamako threedots ', 'correct_label': 'kalyanjianandji', 'label': 3, 'split': 'test', 'title': 'nain milaakar chain churaanaa kisakaa hai ye kaam', 'year': '1967'}`
- output: `{"pred": "kalyanjianandji", "top3": ["kalyanjianandji", "laxmikantpyarelal", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='kalyanjianandji' ref='kalyanjianandji'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='kalyanjianandji' in top3=['kalyanjianandji', 'laxmikantpyarelal', 'shankarjaikishan']

### #451 — FAIL

- item: `{'lyrics': ' chi  aanaa merii jaan merii jaan sunday ke sunday       aanaa merii jaan merii jaan sunday ke sunday chi  i love you mii  bhaag yahaan se duur chi  i love you mii  bhaag yahaan se duur  chi  tujhe pairis dikhaauun tujhe landan ghuumaauun       tujhe braindii pilaauun vhiskii pilaauun       aur khilaauun       khilaauun mugrii ke mugrii ke ande ande       aanaa merii jaan merii jaan sunday ke sunday  mii  main dharam karam kii naarii       tuu niich adham vyabhichaarii       maamaa hain gangaa pujaarii       baabaa kaashii ke kaashii ke pande pande chi  aanaa merii jaan merii jaan sunday ke sunday  chi  aao haathon men haath le walk karen ham       aao sweet sweet aapas men talk karen ham mii  aare hat       sainyyaa meraa pahalavaan hai maare dand hazaar       sainyyaa meraa pahalavaan hai maare dand hazaar       bhaag jaaoge tum bandar degaa jo lalakaar       maare gin gin ke gin gin ke dande dande chi  aanaa merii jaan merii jaan sunday ke sunday  mii  o my saab come come come       tum romeo juliet ham       o dear come here dont fear       ye gaanv kii native ladakii hai       ye dil kii beating kyaa jaane       ye chasing hunting kyaa jaane       ye love kii meeting kyaa jaane chi  right right right all right mii  aao dear ham chale there chi  where mii  there kare muhabbat ke muhabbat ke dhandhe dhandhe dono aanaa merii jaan merii jaan sunday ke sunday ', 'correct_label': 'c ramchandra', 'label': 2, 'split': 'test', 'title': 'aanaa merii jaan merii jaan sunday ke sunday', 'year': '-1'}`
- output: `{"pred": "a r rahman", "top3": ["a r rahman", "c ramchandra", "annu malik"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='a r rahman' ref='c ramchandra'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='c ramchandra' in top3=['a r rahman', 'c ramchandra', 'annu malik']

### #452 — PASS

- item: `{'lyrics': '  sha \to  \tpi pi pi piyaa \tpi pi piyaa \tho ho \tpi pi piyaa \tho o ho o ho o ho \tpi pi piyaa ki \tham aur tum sha \tpi pi piyaa ki \ttum aur ham sha \tpi pi piyaa ki \tham aur tum donon rahen ek saath sha \tnainon men nainaa aur haathon men haath  ki \tham aur tum sha \tpi pi piyaa ki \ttum aur ham sha \tpi pi piyaa do \tham aur tum donon rahen ek saath \tnainon men nainaa aur haathon men haath \tjalaa karen jalane waale chaahen jo bhii ho sha \tho o ho o ho ki \tho o ho o ho do \tham aur tum donon rahen ek saath  sha \trum paa ki \tpaa paa paa sha \trum paa ki \tpaa paa paa  sha  aa jaa o baanke piyaa aajaa \tpiyaa aajaa \tnainon se ras barasaa jaa \tpiyaa aajaa \taa jaa o baanke piyaa aajaa ki \thuun huun huun huun sha \tnainon se ras barasaa jaa ki \trut mastaanii  sha \taa haa ki \traat suhaanii sha \twaa waa ki \tmauj men jawaanii bhii hai aajaa sha \to pi pi pi piyaa ki \to pi pi pi piyaa \toy do \tjalaa karen jalane waale chaahen jo bhii ho sha \tho o ho o ho ki \tho o ho o ho do \tham aur tum donon rahen ek saath \tnainon men nainaa aur haathon men haath \tjalaa karen jalane waale chaahen jo bhii ho sha \tho o ho o ho ki \tho o ho o ho  ki \tyoodling ', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'o pi pi pi piyaa ham aur ham pi pi piyaa tum aur ham', 'year': '1951'}`
- output: `{"pred": "s d burman", "top3": ["s d burman", "madan mohan", "r d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='s d burman' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='s d burman' in top3=['s d burman', 'madan mohan', 'r d burman']

### #453 — FAIL

- item: `{'lyrics': ' lataa jiivan kii bagiyaa mahakegii lahakegii chahakegii khushiyon kii kaliyaan jhuumengii jhuulengii phuulengii jiivan kii bagiyaa threedots lataa vo meraa hogaa  vo sapanaa teraa hogaa milajul ke maangaa  vo teraa meraa hogaa jab jab vo muskuraaegaa  apanaa saveraa hogaa threedots thodaa hamaaraa thodaa tumhaaraa aayegaa phir se bachapan hamaaraa jiivan kii bagiyaa threedots  kishor ham aur bandhenge  ham tum kuchh aur bandhenge hogaa koii biich  to ham tum aur bandhenge baandhegaa dhaagaa kachchaa  ham tum tab aur bandhenge threedots thodaa hamaaraa thodaa tumhaaraa aayegaa phir se bachapan hamaaraa jiivan kii bagiyaa threedots  lataa meraa raajadulaaraa  vo jiivan praan hamaaraa phuulegaa ek phuul  khilegaa pyaar hamaaraa din kaa vo suuraj hogaa  raaton kaa chaand sitaaraa threedots thodaa hamaaraa thodaa tumhaaraa aayegaa phir se bachapan hamaaraa jiivan kii bagiyaa threedots', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'jiivan kii bagiyaa mahakegii lahakegii chahakegii', 'year': '-1'}`
- output: `{"pred": "kalyanjianandji", "top3": ["kalyanjianandji", "laxmikantpyarelal", "r d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='kalyanjianandji' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='s d burman' in top3=['kalyanjianandji', 'laxmikantpyarelal', 'r d burman']

### #454 — FAIL

- item: `{'lyrics': ' umabetaab hai dil betaab hai dil dardemuhabbat ke asar se jis din se meraa chaand chhupaa merii nazar se betaab hai dil  umasoii huii qismat ko merii aake jagaa jaa aajaa merii duniya men zaraa laut ke aajaa2 aankhon ko hai ummiid aankhon ko hai ummiidterii raahguzar  se jis din se meraa chaand chhupaa merii nazar se betaab hai dil  surye kaun mere dil merii aankhon men samaaya ye kiskii nigaahon ne mujhe apanaa banaayaa2 begaana huii begaanaa huii jaati huun duniyaa kii kabar se takaraagaii ye kis kii nazar merii nazar se betaab hai dil  umadam bhar ko terii yaad se gaafil nahiin rahatii jo dil pe guzaratii hai zubaan se nahiin kahatii2 fariyaad bhii fariyaad bhii hotii nahiin rusuvaaii ke dar se jis din se meraa chaand chhupaa merii nazar se betaab hai dil  surik mauj hai ik raag hai ik rang hai jii men hanstii huun kushii men gaatii huun kushii men2 utthaa hai ye tuufaan utthaa hai ye tuufaan kudaa jaane kidhar se takaraagaii ye kiskii nazar merii nazar se', 'correct_label': 'naushad', 'label': 6, 'split': 'test', 'title': 'betaab hai dil dardemuhabbat ke asar se', 'year': '1947'}`
- output: `{"pred": "c ramchandra", "top3": ["c ramchandra", "madan mohan", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='c ramchandra' ref='naushad'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='naushad' in top3=['c ramchandra', 'madan mohan', 'shankarjaikishan']

### #455 — PASS

- item: `{'lyrics': ' bhuulane vaale yaad na aa   2  dekh hamen majabuur na kar  tujhako kasam dukh dur na kar  ham to jiye bas tere liye  tune kuchh aise ranj diye  thes lagi dil tuut gayaa  bhuulane vaale yaad na aa threedots   haay vafaa nakaam huii  subah ke badale shaam huii  phuul khushi ke khil na sake  aankh milii dil mil na sake  dekh liyaa anjaamevafaa  bhulane vaale yaad na aa threedots   dil se mitaa ulfat ka nishaan  tujhase hamaaraa pyaar kahaan  pyaar ka naataa tod yahiin  giit adhuuraa chhod yahiin  main bhi na gaaun tu bhi na gaa  bhulane vaale yaad na aa threedots ', 'correct_label': 'naushad', 'label': 6, 'split': 'test', 'title': 'bhuulane vaale yaad na aa', 'year': '-1'}`
- output: `{"pred": "naushad", "top3": ["naushad", "c ramchandra", "s d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='naushad' ref='naushad'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='naushad' in top3=['naushad', 'c ramchandra', 's d burman']

### #456 — FAIL

- item: `{'lyrics': ' lataa ye dil tum bin kahiin lagataa nahiin ham kyaa karen ye dil tum bin kahiin lagataa nahiin ham kyaa karen tasavvur men koi basataa nahiin ham kyaa karen tumhii kah do ab ai jaanevafaa ham kyaa karen  rafi lute dil men diyaa jalataa nahiin ham kyaa karen tumhi kah do ab ai jaaneadaa ham kyaa karen  lataa ye dil tum bin kahiin lagataa nahiin ham kyaa karen  kisii ke dil men bas ke dil ko tadapaanaa nahin achchhaa  2 nigaahon ko chhalakate dekh ke chhup jaanaa nahiin achchhaa ummidon ke khile gulashan ko jhulasaanaa nahiin achchhaa hamen tum bin koi janchataa nahiin ham kyaa karen tumhi kah do ab ai jaanevafaa ham kyaa karen  rafi lute dil men diyaa jalataa nahiin ham kyaa karen  muhabbat kar to len lekin muhabbat raas aaye bhi  2 dilon ko bojh lagate hain kabhi zulfon ke saaye bhi hazaaron gam hain is duniyaa men apane bhi paraaye bhi muhabbat hi kaa gam tanhaa nahiin ham kyaa karen tumhi kah do ab ai jaaneadaa ham kyaa karen  lataa ye dil tum bin kahiin lagataa nahiin ham kyaa karen  bujhaa do aag dil ki yaa ise khul kar havaa de do  2 rafi jo isakaa mol de paaye use apani vafaa de do lataa tumhaare dil men kyaa hai bas hamen itanaa pataa de do ke ab tanhaa safar katataa nahiin ham kyaa karen rafi lute dil men diyaa jalataa nahiin ham kyaa karen lataa ye dil tum bin kahin lagataa nahiin ham kyaa karen', 'correct_label': 'laxmikantpyarelal', 'label': 4, 'split': 'test', 'title': 'ye dil tum bin kahiin lagataa nahiin ham kyaa karen', 'year': '1963'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "s d burman", "r d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='shankarjaikishan' ref='laxmikantpyarelal'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='laxmikantpyarelal' in top3=['shankarjaikishan', 's d burman', 'r d burman']

### #457 — FAIL

- item: `{'lyrics': ' havaa ke saath saath ghataa ke sang sang o saathii chal mujhe leke saath chal tuu yuun hii dinraat chal tuu sambhal mere saath chal tuu le haathon men haath chal tuu o saathii chal  ek to ye mausam hai badaa suhaanaa apanaa to ye dil bhii hai diivaanaa parbat se aake na takaraa jaanaa tuu banake baadal o saathii chal threedots  hansatii hai ye duniyaa to hansane de are naagan banakar is rut ko dansane de mujhako apanii aankhon men basane de o banake kaajal o saathii chal threedots  apani reshamii zulphen laharaane de mujhako apanii baanhon men aane de thak gaii aaj bahut main ab jaane de naa milenge phir kal o saathii chal threedots', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'havaa ke saath saath ghataa ke sang sang o saathii chal', 'year': '-1'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "s d burman", "r d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='r d burman' in top3=['laxmikantpyarelal', 's d burman', 'r d burman']

### #458 — PASS

- item: `{'lyrics': ' abhi hai e ho o threedots alkaa laah laa laa threedots  abhi  aankhon men base ho tum        aankhon men base ho tum tumhen dil men chhupaa luungaa         aankhon men base ho tum tumhen dil men chhupaa luungaa         jab chaahuun tumhen dekhuun aaiinaa banaa luungaa 2         aankhon men base ho tum tumhen dil men chhupaa luungaa   alkaa aankhon men base ho tum        aankhon men base ho tum tumhen dil men chhupaa luungii         aankhon men base ho tum tumhen dil men chhupaa luungii        jab chaahuun tumhen dekhuun aaiinaa banaa luungii 2         aankhon men base ho tum tumhen dil men chhupaa luungii   alkaa takadiir merii ab to takadiir tumhaarii hai        zahaan dil thaa kabhii meraa tasviir tumhaarii hai abhi ye lab jo tere laraze mere dil men huii halachal        meraa chain churaataa hai terii aankh kaa kaajal alkaa abhii chain churaayaa hai        abhii chain churaayaa hai kal tumhen churaa luungii 2         jab chaahuun tumhen dekhuun aaiinaa banaa luungii abhi he e ho o  abhi tuu paas jo mere hai kyaa kaam bahaaron se        ye chamakiile nainaa kyaa kaam sitaaron se alkaa tere naam kii dhadakan huun tere naam kii saansen huun        ik pal naa judaa ho tum aankhon men aankhen hon abhi koii naameevafaa puchhe        koii naameevafaa puchhe main naam teraa luungaa  2        jab chaahuun dekhuun aaiinaa banaa luungaa  abhi ho o  alkaa aa   alkaa        aankhon men base ho tum         aankhon men base ho tum tumhen dil men chhupaa luungii         aankhon men base ho tum tumhen dil men chhupaa luungii        jab chaahuun tumhen dekhuun aaiinaa banaa luungii   2   abhi he e ho o ', 'correct_label': 'annu malik', 'label': 1, 'split': 'test', 'title': 'aankhon men base ho tum', 'year': '-1'}`
- output: `{"pred": "annu malik", "top3": ["annu malik", "madan mohan", "c ramchandra"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='annu malik' ref='annu malik'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='annu malik' in top3=['annu malik', 'madan mohan', 'c ramchandra']

### #459 — FAIL

- item: `{'lyrics': ' raat akeli hai bujh gae diye aake mere paas kaanon men mere jo bhi chaahe kahiye jo bhi chaahe kahiye raat threedots  1 tum aaj mere liye ruk jaao rut bhi hai furasat bhi hai  tumhen na ho na sahii mujhe tumase muhabbat hai muhabbat kii ijaazat hai to chup kyuun rahiye jo bhi chaahe kahiye raat threedots  2 savaal banii huii dabii dabii ulajhan siinon men javaab denaa thaa to duube ho pasiinon men thaanii hai do hasiinon men to chup kyuun rahiye jo bhi chaahe kahiye raat threedots', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'raat akelii hai bujh gae diye aake mere paas kaanon men mere', 'year': '-1'}`
- output: `{"pred": "madan mohan", "top3": ["madan mohan", "s d burman", "c ramchandra"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='madan mohan' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='s d burman' in top3=['madan mohan', 's d burman', 'c ramchandra']

### #460 — FAIL

- item: `{'lyrics': '  mu \ttuu mahal men rahane vaalii main kutiyaa men rahane vaalaa \tbataa phir teraameraa pyaar kyaa \ttuu aasamaan kaa taaraa main ik zarraa bechaaraa \tbataa phir teraameraa pyaar kyaa  sha \tmere dil men pyaar kii aag piyaa haay  lagii rahii  3 \tmain khol ke khidakii mahal kii haay re  khadii rahii  3 mu  \ttuu hansatii khadii us paar merii naav biich majhadhaar \tbataa phir threedots  sha \tterii miithiimiithii yaad mere dil men haay re haay  aatii rahii  3 \tmerii bhiigiibhiigii ankhhiyon se nindiyaa haay re haay  jaatii rahii  3 mu  \tterii jhuuthii hai har baat tuu chhod gaii meraa saath \tbataa phir threedots  sha \tjab rimajhimrimajhimrimajhim barakhaa haay re haay  hotii rahii  3 \tmain saavan ke baadalon ke sangsang haay re haay  rotii rahii  3 mu  \ttuu khel samajh kar rotii tere aansuu mahal ke motii \tbataa phir threedots ', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'tuu mahal men rahane vaalii  bataa phir teraameraa', 'year': '1949'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "laxmikantpyarelal", "s d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='shankarjaikishan' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='s d burman' in top3=['shankarjaikishan', 'laxmikantpyarelal', 's d burman']

### #461 — FAIL

- item: `{'lyrics': '  yuun milaake nazar kar ke jaaduugarii deke dardejigar aage piichhe dol kar dil tuu churaa le gayaa   threedots  yuun milaake nazar kar ke jaaduugarii deke dardejigar aage piichhe dol kar dil teraa udaa le gayaa   threedots  na na na merii haan ban gayii tuu tuu tuu merii jaan ban gayii aji kyon kyon kyon mujhe pyaar ho gayaa yuun yuun yuun iqaraar ho gayaa qasam se tuu badaa jhuuthaa ho sanam tuune mujhe luutaa yuun milaake nazar   threedots  aa aa aa mere paas to zaraa jaa jaa jaa koii pyaas na jagaa kyaa kyaa kyaa koii dard uthaa kyaa haan haan haan meraa haal hai buraa tujhe aaye koii jaaduu meraa mujhape nahiin qaabuu yuun milaake nazar   threedots ', 'correct_label': 'annu malik', 'label': 1, 'split': 'test', 'title': 'soldier soldier miithii baaten bol kar', 'year': '1998'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "r d burman", "annu malik"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='annu malik'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='annu malik' in top3=['laxmikantpyarelal', 'r d burman', 'annu malik']

### #462 — FAIL

- item: `{'lyrics': ' bujhaa do diipak huun andheraa kar do uthaa do ghuunghat haay saveraa kar do bujhaa do diipak huun   threedots  sharam ke maare haathon se ye cheharaa dhaanp ke na duur duur jaao sar se kaanp kaanp ke ki ab aao paas merii pyaas to bujhaa do koii gam hai to haay vo meraa kar do bujhaa do diipak huun   threedots  badal lo ruup apanaa aaj mere pyaar se sajaa do merii suunii sej ko bahaar se khushii ke phuul gam ke dhuul pe bichhaa ke ise khushiyon kaa haay baseraa kar do bujhaa do diipak huun   threedots ', 'correct_label': 'laxmikantpyarelal', 'label': 4, 'split': 'test', 'title': 'bujhaa do diipak huun ', 'year': '1970'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "madan mohan", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='shankarjaikishan' ref='laxmikantpyarelal'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='laxmikantpyarelal' in top3=['shankarjaikishan', 'madan mohan', 'laxmikantpyarelal']

### #463 — PASS

- item: `{'lyrics': '  ajab hai daastaan terii ai zindagii  2 kabhii hansaa diyaa rulaa diyaa kabhii ajab hai daastaan terii ai zindagii  tum aaii maan kii mamataa liye to muskuraaye ham  ke jaise phir se apane bachapan men lauta aaye ham  2  tumhaare pyaar ke  2  isii  aanchal tale  phir se diipak jale  2  dhalaa andheraa jagii roshanii  ajab hai daastaan threedots  magar badaa hai sangadil hai ye maalik teraa jahaan  yahaan maan beto pe bhii log uthaate hai ungaliyaan  2  kalii ye pyaar kii  2 jhulas ke raha gaii   har taraf aag thii  2  hansaane aaii thii rulaakar chalii ajab hai daastaan threedots', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'ajab hai daastaan terii ai zindagii', 'year': '1959'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "s d burman", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='shankarjaikishan' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='shankarjaikishan' in top3=['shankarjaikishan', 's d burman', 'laxmikantpyarelal']

### #464 — FAIL

- item: `{'lyrics': ' kaanp rahii main abhii zaraa tham jaanam baakii hai raat abhii  haanf rahii main le luun zaraa dam jaanam naa kar ye baat abhii   tuune o re mere jaanii jo hai jii men thaanii usase daruun main daruun main tuu jo paas mere aaye jaan merii jaaye aahen bharuun main jaane de re rok zaraa haath abhii  abhii gul hain diiye saare paas aa jaa pyaare ban jaa diiwaanaa diiwaanaa zaraa mast main bhii ho luun to ye tujhe boluun tuu hai nishaanaa main bhii huun tuu bhii hai saath abhii', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'kaanp rahii main abhii zaraa tham jaanam', 'year': '1973'}`
- output: `{"pred": "annu malik", "top3": ["annu malik", "s d burman", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='annu malik' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='r d burman' in top3=['annu malik', 's d burman', 'laxmikantpyarelal']

### #465 — FAIL

- item: `{'lyrics': '  o paakhii paakhii paradesii  ai ajanabii tuu bhii kabhii aavaaz de kahiin se main yahaan tukadon men jii rahaa huun tuu kahiin tukadon men jii rahii hai ai ajanabii tuu bhii kabhii   threedots  roz roz resham sii havaa aate jaate kahatii hai bataa resham sii havaa kahatii hai bataa vo jo duudh dhulii maasuum kalii vo hai kahaan kahaan hai vo roshanii kahaan hai vo jaan sii kahaan hai main adhuuraa tuu adhuurii jii rahii hai ai ajanabii tuu bhii kabhii   threedots  o paakhii paakhii paradesii  tuu to nahiin hai lekin terii muskuraahat hai cheharaa kahiin nahiin hai par terii aahat hai tuu hai kahaan kahaan hai teraa nishaan kahaan hai meraa jahaan kahaan hai main adhuuraa tuu adhuurii jii rahii hai ai ajanabii tuu bhii kabhii   threedots ', 'correct_label': 'a r rahman', 'label': 0, 'split': 'test', 'title': 'ai ajanabii tuu bhii kabhii', 'year': '1998'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "annu malik", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='a r rahman'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='a r rahman' in top3=['laxmikantpyarelal', 'annu malik', 'shankarjaikishan']

### #466 — FAIL

- item: `{'lyrics': ' ko  tak dhinaa dhin   dhinaa dhin   tak dhinaa dhin  barasaat men  ko  tak dhinaa dhin  barasaat men hamase mile tum sajan tumase mile ham  barasaat men  ko  tak dhinaa dhin  barasaat men hamase mile tum sajan tumase mile ham  barasaat men  ko  tak dhinaa dhin   nainon se jhaanke jii  mast jawaanii  merii mast jawaanii  kahatii phire duniyaa se  dil kii kahaanii  mere dil kii kahaanii  unakii jo main unase kaisii sharam 2  kaisii sharam  barasaat men  ko  tak dhinaa dhin  barasaat men hamase mile tum sajan tumase mile ham  barasaat men  ko  tak dhinaa dhin   priit ne singaar kiyaa  main banii dulhan 2  sapanon kii rimajhim men  naach uthaa man  meraa naach uthaa man  aaj main tumhaarii huii tum mere sanam 2  tum mere sanam  barasaat men threedots   ye samaan hai jaa rahe ho  kaise manaauun 2  main tumhaarii raah men ye  nain bichhaauun 2  jo naa aao tumako merii  jaan kii qasam 2  barasaat men threedots   der naa karanaa kahiin ye  aas tuut jaaye  saans chhuut jaaye  tum naa aao dil kii lagii  mujhako hii jalaaye  kaak men milaaye  aag kii lapaton men pukaare ye meraa gam  mil naa sake haay mil naa sake ham 2 ', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'barasaat men hamase mile tum sajan', 'year': '1949'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "madan mohan", "s d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='r d burman' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='shankarjaikishan' in top3=['r d burman', 'madan mohan', 's d burman']

### #467 — FAIL

- item: `{'lyrics': ' suresh nigaahon ne chhedaa hai dil kaa taraanaa nigaahon ne chhedaa hai dil kaa taraanaa sunakar kahiin na tum buraa maan jaanaa mainne kiyaa hai pyaar pahalii baar 2 2 nigaahon ne chhedaa hai dil kaa taraanaa   saadhanaa dil kii baaten aankhon se kyaa honthon se bolo sajanaa 2  suresh yuun hai ki mujhako pyaar tumase ho gayaa hai bas yahii kahanaa hai bas yahii kahanaa o jaanejaanaan 2 mainne kiyaa hai pyaar pahalii baar 2 nigaahon ne chhedaa hai dil kaa taraanaa   saadhanaa aa haa threedots  suresh dil kii haalat kaise dikhaauun sochaa hii karataa thaa jatan  saadhanaa aankhon men ab to rahane lagii hai suurat tumhaarii jaaneman  suresh ras kii bhiigii in aankhon men aa main duub ke rah jaauun2  saadhanaa main bhii ye chaahuun aaj tere pyaar ke tuufaan men bah jaauun  tuufaan men bah jaauun dekhe zamaanaa 2 ki mainne kiyaa hai pyaar pahalii baar mainne kiyaa hai pyaar pahalii baar nigaahon ne chhedaa hai dil kaa taraanaa   saadhanaa jaise ab hai waise kyaa tuu kal bhii mujhako chaahegaa 2  suresh jo aaj tujhako ye dilojaan de chukaa kaise na chaahegaa chaahegaa chaahegaa kal bhii diiwaanaa 2 mainne kiyaa hai pyaar pahalii baar 2   saadhanaa nigaahon ne chhedaa hai dil kaa taraanaa sunakar kahiin na tum buraa maan jaanaa mainne kiyaa hai pyaar pahalii baar 2  suresh mainne kiyaa hai pyaar pahalii baar  saadhanaa mainne kiyaa hai pyaar pahalii baar 2', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'nigaahon ne chhedaa hai', 'year': '1996'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "madan mohan", "r d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='shankarjaikishan' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='r d burman' in top3=['shankarjaikishan', 'madan mohan', 'r d burman']

### #468 — FAIL

- item: `{'lyrics': '  ki \tarii o pottii kahaan chalii \tpalat merii anaar kii kalii aa \tbadatamiiz  taane diin  tanadaanaa  3 3 khaatuun kii khidamat men salaam apun kaa 2  ajii pottii pataanaa hai  2 pottii pataanaa hai ajii pottii pataanaa hai faqat kaam apun kaa gharbaar huaa ishq men niilaam apun kaa khaatuun kii khidamat threedots  baataan nahiin karate ham haidaraabaadii 2 haathaan men tere joo menhadii na lagaa dii to naam nahiin lenge  kabhii apane vatan kaa  2 khaatuun kii khidamat threedots  gulabadan khaadim ke haathaan se munh men daal ko chabaaenge kyaa paan ye paanaa men mere kaleje ke tuukade supaarii kii jagah rakh ko chabarchabar ke chabar jaa mar mitane men jaanam ham logaan hain maahir 2 ghus kar tere dil men nikalenge na baahir 2 kharchaa ho qafan kaa na  charchaa ho dafan kaa  2 khaatuun kii khidamat threedots ', 'correct_label': 'laxmikantpyarelal', 'label': 4, 'split': 'test', 'title': 'arii o pottii  khaatuun kii khidamat men salaam apun kaa', 'year': '1982'}`
- output: `{"pred": "madan mohan", "top3": ["madan mohan", "c ramchandra", "kalyanjianandji"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='madan mohan' ref='laxmikantpyarelal'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='laxmikantpyarelal' in top3=['madan mohan', 'c ramchandra', 'kalyanjianandji']

### #469 — PASS

- item: `{'lyrics': ' zamaane men ajii aise kaii naadaan hote hain vahaan le jaate hain kashtii jahaan tuufaan hote hain  shamaa kii bazm men aa kar ke paravaane samajhate hain yahiin par umr guzaregii yah diivaane samajhate hain magar ik raat ke yah to faqat mehamaan hote hain zamaane men threedots  mohabbat sabakii mahfil men shamaa ban kar nahiin jalatii hasiinon kii nazar sab pe chhurii ban kar nahiin chalatii jo hain taqadiir vaale bas vahii qurbaan hote hain zamaane men threedots  dubo kar duur saahil se nazaaraa dekhanevaale lagaa kar aag chup ke se tamaashaa dekhanevaale tamaashaa aap banate hain to kyon hairaan hote hain zamaane mein threedots ', 'correct_label': 'laxmikantpyarelal', 'label': 4, 'split': 'test', 'title': 'zamaane men ajii aise kaii naadaan hote hain', 'year': '1970'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "naushad", "c ramchandra"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='laxmikantpyarelal' ref='laxmikantpyarelal'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='laxmikantpyarelal' in top3=['laxmikantpyarelal', 'naushad', 'c ramchandra']

### #470 — FAIL

- item: `{'lyrics': ' bhagavaan do ghadii jaraa insaan banake dekh dharatii pe chaar din kabhii mehamaan banake dekh mehamaan banake dekh  o o o  hai jinako terii yaad kabhii unakii le khabar kabhii unakii le khabar aasamaan vaale kabhii gariibon pe kar nazar gariibon pe kar nazar dil men kisii gariib ke aramaan banake dekh dharatii pe chaar din threedots  o o o jo kuchh bhii ho rahaa hai vo terii nazar men hai terii nazar men hai aa dekh merii aas kii naiyaa bhanvar men hai naiyaa bhanvar men hai sab jaanate hue bhii naa anajaan banake dekh dharatii pe chaar din threedots  o o o tujh ko khabar nahiin koi kitanaa niraash hai kitanaa niraash hai tinake kii duubate ko maalik talaash hai maalik talaash hai inasaan ban sake naa to bhagavaan banake dekh dharatii pe chaar din threedots', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'bhagavaan do ghadii zaraa insaan banake dekh', 'year': '1951'}`
- output: `{"pred": "c ramchandra", "top3": ["c ramchandra", "naushad", "kalyanjianandji"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='c ramchandra' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='s d burman' in top3=['c ramchandra', 'naushad', 'kalyanjianandji']

### #471 — FAIL

- item: `{'lyrics': ' ye shaam mastaanii madahosh kiye jaaye mujhe dor koii khiinche terii or liye jaaye  duur rahatii hai tuu mere paas aatii nahiin hothon pe tere kabhii pyaas aatii nahiin aisaa lage jaise ki tuu hansake zahar koii piye jaaye shaam mastaanii threedots  baat jab main karuun mujhe rok detii hai kyon terii miithii nazar mujhe tok detii hai kyon terii hayaa terii sharam terii qasam mere honth siye jaaye shaam mastaanii threedots  ek ruthii huii taqadiir jaise koii khaamosh aise hai tuu tasviir jaise koii terii nazar banake zubaan lekin tere paigaam diye jaaye  ye shaam mastaanii madahosh kiye jaaye mujhe dor koii khiinche terii or liye jaaye', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'ye shaam mastaanii madahosh kiye jaaye', 'year': '-1'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "s d burman", "kalyanjianandji"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='r d burman' in top3=['laxmikantpyarelal', 's d burman', 'kalyanjianandji']

### #472 — FAIL

- item: `{'lyrics': ' vaqt se pahale qisamat se jyaadaa kisii ko milaa hai na kisii ko milegaa pyaar se saaraa gulashan mahake nafarat se koii gul na khilegaa vaqt se pahale qisamat se jyaadaa   threedots  gam ko hamane giit banaa kar is duniyaa kaa dil bahalaayaa hansate hansaate jaane kaise dil hii dil men tumako paayaa ham hain sabake koii na apanaa ik din koii apanaa milegaa pyaar se saaraa gulashan mahake nafarat se koii gul na khilegaa vaqt se pahale qisamat se jyaadaa   threedots  nain mile aur chain ganvaayaa baat puraanii phir bhii naii hai terii nazar ne merii nazar se bin bole ik baat kahii hai dekh ke mujhako yuun na lajaao dil pe phir qaabuu na rahegaa pyaar se saaraa gulashan mahake nafarat se koii gul na khilegaa vaqt se pahale qisamat se jyaadaa   threedots ', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'vaqt se pahale qisamat se jyaadaa', 'year': '1981'}`
- output: `{"pred": "kalyanjianandji", "top3": ["kalyanjianandji", "naushad", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='kalyanjianandji' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='r d burman' in top3=['kalyanjianandji', 'naushad', 'shankarjaikishan']

### #473 — FAIL

- item: `{'lyrics': ' jaane vaale zaraa hoshiyaar yahaan ke ham hain raaj kumaar oy hoy aage piichhe hamaarii sarakaar yahaan ke ham hain raaj kumaar oy hoy jaane vaale  amariikii andaaz bhii siikhe ham yoraph ke raaz bhii siikhe ham se jo baazii le kar jaaye hai koii aisaa saamane aaye saarii duniyaa men apanii jayakaar yahaan ke ham hain raaj kumaar   threedots  hamase muhabbat hamase javaanii rang bharii hai apanii kahaanii  dard saa apane dil men jo paayaa jaan gaye ham kisane bulaayaa unase hii milane jhuum ke nikale bhaii thaath se nikale dhuum se nikale unako bhii hai hamaaraa intazaar yahaan ke ham hain raaj kumaar   threedots ', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'jaane vaale zaraa hoshiyaar yahaan ke ham hain raaj kumaar', 'year': '1964'}`
- output: `{"pred": "s d burman", "top3": ["s d burman", "c ramchandra", "kalyanjianandji"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='s d burman' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='shankarjaikishan' in top3=['s d burman', 'c ramchandra', 'kalyanjianandji']

### #474 — FAIL

- item: `{'lyrics': '  ra \taa mere hamajolii aa khelen aankh michaulii aa \tgaliyon men chaubaaron men baagon men bahaaron men ho \tmain dhuundhuun tuu chhup jaa la \taa mere hamajolii threedots  \tmain aauun ra \tna na la \tmain aauun ra \tna na na la \tmain aauun ra \tnaa la \tmain aauun ra \taa jaa  la \tpiipal ke uupar jaa baithaa chhip ke meraa saathii \tdhak se lekin dhadak gayaa dil gir gaii haath se laathii \to pakadaa gayaa  ra \tmain aauun la \tna na ra \tmain aauun la \tna na na ra \tmain aauun la \tnaa ra \tmain aauun la \taa jaa  ra \tpanaghat ke piichhe jaa baithii chhip ke merii sajaniyaa \tchhan se lekin anajaane men chhanak gaii painjaniyaa \to pakadii gaii ko \taa mere hamajolii threedots  \tmain aauun ra \tna na la \tmain aauun ra \tna na na la \tmain aauun ra \tnaa la \tmain aauun ra \taa jaa  la \to mere nayanon se tuu chhip sakataa hai o mere rasiyaa \tlekin mere man se chhipanaa mushqil hai manabasiyaa \tai pakadaa gayaa  ra \tmain aauun la \tna na ra \tmain aauun la \tna na na ra \tmain aauun la \tnaa ra \tmain aauun la \taa jaa  ra \tkaahe lukchhup ke khel men chhede tuu prem kii batiyaan \tdekh tamaashaa dekh rahii hain saare shahar kii ankhiyaan \to pakadii gaii ko \taa mere hamajolii threedots ', 'correct_label': 'laxmikantpyarelal', 'label': 4, 'split': 'test', 'title': 'aa mere hamajolii aa khelen aankh michaulii aa', 'year': '1969'}`
- output: `{"pred": "madan mohan", "top3": ["madan mohan", "laxmikantpyarelal", "kalyanjianandji"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='madan mohan' ref='laxmikantpyarelal'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='laxmikantpyarelal' in top3=['madan mohan', 'laxmikantpyarelal', 'kalyanjianandji']

### #475 — FAIL

- item: `{'lyrics': ' muhabbat men kashish hogii to ek din tumako paa lenge isii duniyaa men hamtum ek duusarii duniyaa banaa lenge  sitaaron men gulon men chaand men tum mil hii jaaoge muhabbat men haqiiqat hai kahaan tak aazamaa lenge  zamaane ko dikhaa denge ki do dil kaise milate hain isii suurat se ham bigadii huii qismat banaa lenge', 'correct_label': 'madan mohan', 'label': 5, 'split': 'test', 'title': 'muhabbat men kashish hogii to ek din tumako paa lenge', 'year': '1952'}`
- output: `{"pred": "c ramchandra", "top3": ["c ramchandra", "naushad", "r d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='c ramchandra' ref='madan mohan'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='madan mohan' in top3=['c ramchandra', 'naushad', 'r d burman']

### #476 — PASS

- item: `{'lyrics': ' faao han ye mokshii uu mahaa chhaiir mahaa chhaiir maas chhaiir maas chhaiir  latakaa dikhaa diyaa hamane  jhatakaa lagaa diyaa tumane tadaa ho tumako tadaa  matakaa ke chal diye ham to  khatakaa huaa hai kyuun tumako tadaa ho tumako tadaa   manch kii jo aurat hai desh kaa sensation  nazar milaaii nazaron se sabhii ko temptation  chhod denge chhod denge ham ho ho ho   dhin tak dhin tak dhin o ho ho deviyon kaa saath denge ham   latakaa dikhaa diyaa hamane jhatakaa lagaa diyaa tumane tadaa ho tumako tadaa matakaa ke chal diye ham to khatakaa huaa hai kyuun tumako tadaa ho tumako tadaa  ghuum le kidhar bhii udhar hii glamour hai  umar bhii javaan hai sabhii to humour hai  hamanen vo joke sune censor bhii nahiin sune  hamane jo dress pahaniin filmstar bhii naa pahanen  chuudiidaarvuudiidaar bhuul jaayen hollywood bollywood chhuute piichhe  ye pahan vo pahan bore ho gaye aakir men ghaagharaa bhii bhaagaa piichhe  chhod denge chhod denge ham ho ho ho  dhin tak dhin tak dhin o ho ho  deviyon kaa saath denge ham   latakaa dikhaa diyaa hamane  jhatakaa lagaa diyaa tumane tadaa ho tumako tadaa  matakaa ke chal diye ham to  khatakaa huaa hai kyuun tumako tadaa ho tumako tadaa   kamariyaa kamal sii lachak hai noodal sii   dil ko puncture jo kare nazar hai needle sii   apanii jo kabaren hain b b c men bhii nahiin   ham jaisii sundarataa m tv men bhii nahiin   miithiimiithii baaton kaa mukkaalaa   mandii men bhii mahal men bhii muqaabalaa   jhuuth nahiin bolaa mainne gopaalaa   jhuuth hai to pii le tuu cocacola   chhod denge chhod denge ham ho ho ho dhin tak dhin tak dhin o ho ho deviyon kaa saath denge ham   latakaa dikhaa diyaa hamane jhatakaa lagaa diyaa tumane tadaa ho tumako tadaa matakaa ke chal diye ham to khatakaa huaa hai kyuun tumako tadaa ho tumako tadaa  manch kii jo aurat hai desh kaa sensation nazar milaaii nazaron se sabhii ko temptation chhod denge chhod denge ham ho ho ho dhin tak dhin tak dhin o ho ho deviyon kaa saath denge ham  ', 'correct_label': 'a r rahman', 'label': 0, 'split': 'test', 'title': 'latakaa dikhaa diyaa hamane jhatakaa lagaa diyaa tumane', 'year': '1996'}`
- output: `{"pred": "a r rahman", "top3": ["a r rahman", "kalyanjianandji", "c ramchandra"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='a r rahman' ref='a r rahman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='a r rahman' in top3=['a r rahman', 'kalyanjianandji', 'c ramchandra']

### #477 — FAIL

- item: `{'lyrics': ' ye sar ye sar ye ye ye 2 kyaa karen kyaa naa karen ye kaisii mushkil haay  koii to bataa de isakaa haal o mere bhaaii  ki ek taraf to us se pyaar karen ham  aur us ko hii ye kahane se daren ham  rozroz ham sochataa yahii aaj hamako vo agar mil jaaye kahiin  to aisaa bolegaa saalaa vaisaa bolegaa khullamkhullaa us pe dil kaa raaz ham kholegaa  vo saamane chamakatii hai saans hii atakatii hai aur ye zabaan jaatii hai phisal   hey hey hey hey hey 2  koii badii baat nahiin hamen kahanaa thaa jo bhii vo to ham yuun bhii kahate magar  phir bhii kahaa nahiin vajah usakii hai yahii bas inkaar se hamako thaa dar  ab kahen yaa tab kahen kahaan kahen kab kahen  sochsoch men hii vo gaii nikal ', 'correct_label': 'a r rahman', 'label': 0, 'split': 'test', 'title': 'kyaa karen kyaa naa karen ye kaisii mushkil haay', 'year': '1996'}`
- output: `{"pred": "annu malik", "top3": ["annu malik", "a r rahman", "s d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='annu malik' ref='a r rahman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='a r rahman' in top3=['annu malik', 'a r rahman', 's d burman']

### #478 — PASS

- item: `{'lyrics': '  jaa jaa jaa re jaa re jaa jaa jaa jaa re jaa re jaa re ranjogam ke andhere tuu jaa teraameraa saath kyaa teraameraa saath kyaa re tuu merii duniyaa se jaa jaa jaa jaa re jaa re jaa   ummiidon ne chhedaa kushii kaa ye taraanaa nigaahon ne siikhaa hai phir se muskuraanaa  2 jaa jaa jaa re jaa re jaa jaa jaa jaa re jaa re jaa re ranjogam ke andhere tuu jaa jaa jaa jaa re jaa re jaa   muhabbat kii aisii ghadii aa rahii hai nazar merii mujhase hii sharmaa rahii hai  2 jaa jaa jaa re jaa re jaa jaa jaa jaa re jaa re jaa re ranjogam ke andhere tuu jaa jaa jaa jaa re jaa re jaa   sitaaron kii chhainyaan men miithiimiithii baaten fasaanaa banengii hamaarii mulaaqaaten  2 jaa jaa jaa re jaa re jaa jaa jaa jaa re jaa re jaa re ranjogam ke andhere tuu jaa teraameraa saath kyaa teraameraa saath kyaa re tuu merii duniyaa se jaa jaa jaa jaa re jaa re jaa ', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'jaa jaa jaa re jaa re jaa', 'year': '1953'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "naushad", "s d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='shankarjaikishan' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='shankarjaikishan' in top3=['shankarjaikishan', 'naushad', 's d burman']

### #479 — FAIL

- item: `{'lyrics': ' jise dil men basaanaa chaahaa thaa use dil men apane basaa na sake par ab ye tamannaa hai dil ki hamen yaad bhii usakii aa na sake  dhokhaa ye teraa kab tak chalataa jo haal thaa aakir khul ke rahaa 2 dil tuut gayaa achchhaa hii huaa ham aur to thokar khaa na sake jise dil men basaanaa chaahaa thaa threedots  ab aur nahiin ulajhan koii ik chiiz abhii tak baaqii hai 2 kyon gair ko ham apanaa samajhe is gam ko dil se bhulaa na sake jise dil men basaanaa chaahaa thaa threedots', 'correct_label': 'madan mohan', 'label': 5, 'split': 'test', 'title': 'jise dil men basaanaa chaahaa thaa', 'year': '1951'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "laxmikantpyarelal", "c ramchandra"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='shankarjaikishan' ref='madan mohan'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='madan mohan' in top3=['shankarjaikishan', 'laxmikantpyarelal', 'c ramchandra']

### #480 — FAIL

- item: `{'lyrics': '  chanchal shiital nirmal komal sangiit kii devii svar sajanii 2 sundarataa kii har pratimaa se badhakar hai tuu sundar sajanii chanchal shiital threedots  kahate hain jahaan naa ravi pahunche kahate hain vahaan par kavi pahunche tere rangruup kii chhaayaa tak naa ravi pahunche naa kavi pahunche main chhuune laguun tuu ud jaae pariyon se tere par sajanii chanchal shiital threedots  ko \taa a aa aa aa hn tere rasavantii honthon kaa main giit koii ban jaauungaa saragam ke phuulon se tere sapanon kii sej sajaauungaa dolii men baith ke aaegii jab tuu saajan ke ghar sajanii chanchal shiital threedots  aisaa lagataa hai tuut gae sab taare goregore ik chandaa se rangiin badan se lipat gae ko \to  mu \tbanakar nath kangan karadhaniyaa ghungharuu jhumake jhuumar sajanii mu ko \tchanchal shiital threedots ko \tchanchal shiital nirmal komal mu \tsangiit kii devii svar sajanii 2 ', 'correct_label': 'laxmikantpyarelal', 'label': 4, 'split': 'test', 'title': 'chanchal shiital nirmal komal sangiit kii devii', 'year': '1978'}`
- output: `{"pred": "s d burman", "top3": ["s d burman", "shankarjaikishan", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='s d burman' ref='laxmikantpyarelal'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='laxmikantpyarelal' in top3=['s d burman', 'shankarjaikishan', 'laxmikantpyarelal']

### #481 — FAIL

- item: `{'lyrics': ' mere des men ho mere des men pavan chale puravaaii mere des ko dekhane bhaii saarii duniyaa aaii mere des men threedots  jhilamil jhilamil taaraa chamake  dagamag dagamag naiyaa dole rimajhim baadal barase raamaa ho  gunagun gunagun bhanware ghuumen jharajhar jharajhar jharane jhuumen  chhamachham paayal baaje raamaa ho  he gaiyaa naache baansurii bajaaye re kanhaaii mere des men threedots  amawaa kii daalii pe koyal giit sunaaye komal komal mere baag kii kaliyon ke ho   patajhad mast bahaaron jaise patthar bhii hain taaron jaise mere gaanv kii galiyon ke ho he mere khet kii mittii ne sone kii muurat paaii mere des men threedots', 'correct_label': 'laxmikantpyarelal', 'label': 4, 'split': 'test', 'title': 'mere des men pavan chale purawaaii', 'year': '1969'}`
- output: `{"pred": "s d burman", "top3": ["s d burman", "r d burman", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='s d burman' ref='laxmikantpyarelal'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='laxmikantpyarelal' in top3=['s d burman', 'r d burman', 'laxmikantpyarelal']

### #482 — FAIL

- item: `{'lyrics': '     chi \thaa aa \tare buudhaa hai ghodaa laal hai lagaam la \to buudhaa hai ghodaa laal hai lagaam \tkaisii ye jodii milaaii mere do \traam \tkaisii ye jodii milaaii mere raam 3  chi \thaan pahaluuehuur men languur kudaa kii qudarat la \taan kauwe kii chonch men anguur kudaa kii gudarat chi \tare gadhe ko de diye khaane badaam la \to gadhe ko de diye khaane badaam  do \tkaisii ye jodii milaaii mere raam 4  chi \tho bandar ke haath men ye saaz dekhiye \taur ulluu ke sar pe ye taaz dekhiye \tjo dekhaa kabhii na wo aaj dekhiye la \thansegii jo dekhegii duniyaa tamaam \tho hansegii jo dekhegii duniyaa tamaam  do \tkaisii ye jodii milaaii mere raam 3 \thaa kaisii ye jodii milaaii mere raam  do \tkaisii ye jodii milaaii mere raam 3 \tho kaisii ye jodii milaaii mere raam  la \thaan budhawaa hai ghudawaa lalawaa lagaam chi \thaan budhawaa hai ghudawaa lalawaa lalawaa hai lagaam \thaan do \tkaisii ye judiyaa milaiyaa more raam 3 ', 'correct_label': 'c ramchandra', 'label': 2, 'split': 'test', 'title': 'are buudhaa hai ghodaa laal hai lagaam', 'year': '1950'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "madan mohan", "a r rahman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='c ramchandra'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='c ramchandra' in top3=['laxmikantpyarelal', 'madan mohan', 'a r rahman']

### #483 — FAIL

- item: `{'lyrics': ' haan tumhen tumhen tumhen ham chaahate hain dekho naa tum se duur jaa kar tumhaare paas aate hain kaun main haan tum bas tum offo haan tumhen threedots  thodii sii mastii thodaa saa nashaa hai kaise bataauun is dil men kyaa hai koii adaa se bijalii giraae koii nazar se jaaduu chalaae jaanaan maine jaanaa hai tuu meraa diivaanaa hai koi anjaanaa hai koii pareshaan hai kaun main haan tum bas tum offo haan tumhen threedots  ho ye husn teraa kaatil badaa hai saaraa zamaanaa is pe fidaa hai he karane lagii hai rut beimaanii bach ke hai rahanaa ham ko diivaanii dekho aankhon aankhon men haay aisii mulaakaaton men luute koii baaton men dekhe koii pyaar se kaun main haan tum bas tum offo haan tumhen threedots ', 'correct_label': 'annu malik', 'label': 1, 'split': 'test', 'title': 'haan tumhen ham chaahate hain  kaun main haan tum bas tum offo', 'year': '2002'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "annu malik", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='r d burman' ref='annu malik'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='annu malik' in top3=['r d burman', 'annu malik', 'laxmikantpyarelal']

### #484 — PASS

- item: `{'lyrics': '  do \t mile mile do badan khile khile do chaman \tye zindagii kam hii sahii koii gam nahiin  2  la \tder se aaii aaii to bahaar \tangaaron pe sokar jaagaa pyaar ki \t tuufaanon men phuul khilaae  2 kaisaa ye milan do \tmile mile do badan threedots  ki \thonth vahii hain hai vahii muskaan \tab tak kyon kar dabe rahe aramaan la \t biite dinon ko bhuul hii jaaen  2 ab hamtum sajan do \tmile mile do badan threedots ', 'correct_label': 'kalyanjianandji', 'label': 3, 'split': 'test', 'title': 'mile mile do badan khile khile do chaman', 'year': '1973'}`
- output: `{"pred": "kalyanjianandji", "top3": ["kalyanjianandji", "r d burman", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='kalyanjianandji' ref='kalyanjianandji'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='kalyanjianandji' in top3=['kalyanjianandji', 'r d burman', 'laxmikantpyarelal']

### #485 — FAIL

- item: `{'lyrics': '  mu \tye shahar badaa alabelaa har taraf hasiinon kaa melaa \tpar aur bhii hai kuchh aage tuu chalaa chal akelaa ko \tsingaapur 3  mu \tjavaan shahar dilavaalon kaa hamaare jaise matavaalon kaa \tgale mile sab yahaan pe aakar nahiin bhed gorekaalon kaa ko \tniyummaa mu \tye shahar badaa threedots ko \tsingaapur 3  mu \tyu muskaraatii natakhat gudiyaan yah husn vaalii miithii chhuriyaan \tzaraa der ko sab chakaraaen kahaan se aaiin itanii pariyaan ko \tnamaste mu \tye shahar badaa threedots ko \tsingaapur 3  mu \tjidhar se guzare ham mastii men bahaar aaii us bastii men \tchalen pyaar ke nagamen gaate hai ghar kisii dil kii dillii men ko \tniyummaa mu \tye shahar badaa threedots ko \tsingaapur 3 ', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'ye shahar badaa alabelaa  singaapur', 'year': '1960'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "kalyanjianandji", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='shankarjaikishan' in top3=['laxmikantpyarelal', 'kalyanjianandji', 'shankarjaikishan']

### #486 — FAIL

- item: `{'lyrics': ' ruk jaanaa nahiin tuu kahiin haar ke kaanton pe chalake milenge saaye bahaar ke o raahii o raahiithreedots  suuraj dekh ruk gayaa hai tere aage jhuk gayaa hai jab kabhii aise koii mastaanaa nikale hai apanii dhun men diivaanaa shaam suhaanii ban jaate hain din intazaar ke o raahii o raahiithreedots  saathii na kaaravaan hai ye teraa imtihaan hai yuun hii chalaa chal dil ke sahaare karatii hai manzil tujhako ishaare dekh kahiin koii rok nahiin le tujhako pukaar ke o raahii o raahiithreedots  nain aansuu jo liye hain ye raahon ke diye hain logon ko unakaa sab kuchh deke tuu to chalaa thaa sapane hii leke koii nahiin to tere apane hain sapane ye pyaar ke o raahii o raahiithreedots ', 'correct_label': 'laxmikantpyarelal', 'label': 4, 'split': 'test', 'title': 'ruk jaanaa nahiin tuu kahiin haar ke', 'year': '1974'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "laxmikantpyarelal", "s d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='r d burman' ref='laxmikantpyarelal'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='laxmikantpyarelal' in top3=['r d burman', 'laxmikantpyarelal', 's d burman']

### #487 — FAIL

- item: `{'lyrics': ' tumhen jo bhii dekh legaa kisii kaa naa ho sakegaa parii ho bhalaa ho kyaa ho tum tumhen jo bhii dekh legaa threedots  duniyaa chale udhar hii jidhar ye nigaah ghuume shabanam ko dekh lo gar banakar sharaab jhuume nashaa hii nashaa ho kyaa ho tum tumhen jo bhii dekh legaa threedots  kajaraare nain bhanvare palaken jo kholate hain dilon kii bhii baat kyaa hai imaan bhii dolate hain bhuuton ke khudaa ho kyaa ho tum tumhen jo bhii dekh legaa threedots  kahaan ye dhamakataa cheharaa kahaan aisaa nuur hogaa jisane banaayaa tumako use bhii guruur hogaa khudaa kii adaa ho kyaa ho tum tumhen jo bhii dekh legaa threedots', 'correct_label': 'kalyanjianandji', 'label': 3, 'split': 'test', 'title': 'tumhen jo bhii dekh legaa kisii kaa naa ho sakegaa', 'year': '-1'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "annu malik", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='shankarjaikishan' ref='kalyanjianandji'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='kalyanjianandji' in top3=['shankarjaikishan', 'annu malik', 'laxmikantpyarelal']

### #488 — PASS

- item: `{'lyrics': ' use hansanaa bhii hogaa use ronaa bhii hogaa use paanaa bhii hogaa use khonaa bhii hogaa subah shaam tanhaaii men aahen bharegaa har dil jo pyaar karegaa  o palakon ke mahake ghar men sapanaa ban ke palataa hai isakii paagal dhadakan pe jor koii kahaan chalataa hai use jaganaa bhii hogaa use sonaa bhii hogaa use jiinaa bhii hogaa zahar piinaa bhii hogaa kisii ke hasiin chehare pe vo to maregaa har dil jo pyaar karegaa threedots  o deke chain kisii ko bechainii kyuun letaa hai ye aisaa diivaanaa hai jo ishq men jaan bhii detaa hai use kahanaa bhii hogaa chup rahanaa bhii hogaa use dardejudaaii yahaan sahanaa bhii hogaa laakh jhukaae koii vo naa jhukegaa har dil jo pyaar karegaa threedots use hansanaa bhii hogaa use ronaa bhii hogaa use paanaa bhii hogaa use khonaa bhii hogaa subah shaam tanhaaii men aahen bharegaa har dil jo pyaar karegaa  leke hansii honthon pe aankhon men bharake paanii sachchii muhabbat vo hai jo hans ke de de qurbaanii use rukanaa bhii hogaa use chalanaa bhii hogaa use bujhanaa bhii hogaa use jalanaa bhii hogaa piir paraaii vo chhup ke sahegaa har dil jo pyaar karegaa threedots  pedon kii har daalii pe phuul kahaan koii khilataa hai sabako yahaan manachaahaa haay pyaar kahaan kab milataa hai tanhaaii men hogaa shahanaaii men hogaa kabhii apanon men hogaa parachhaaii men hogaa kaanton kii raahon pe bhii hans ke chalegaa har dil jo pyaar karegaa threedots ', 'correct_label': 'annu malik', 'label': 1, 'split': 'test', 'title': 'use hansanaa bhii hogaa  har dil jo pyaar karegaa', 'year': '2000'}`
- output: `{"pred": "annu malik", "top3": ["annu malik", "kalyanjianandji", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='annu malik' ref='annu malik'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='annu malik' in top3=['annu malik', 'kalyanjianandji', 'shankarjaikishan']

### #489 — FAIL

- item: `{'lyrics': ' aa hamaarii galii aanaa ta achchhaa jii hamen na bhulaanaa aa achchhaa jii hamaarii galii aanaa ta achchhaa jii hamen na bhulaanaa aa achchhaa jii  aa jabase milii hain nigaahen chamakii hain muhabbat kii raahen 2 ta sun lo tumhen ham chaahen aa achchhaa jii ta sun lo tumhen ham chaahen aa dekho ye vaadaa nibhaanaa hamaarii galii aanaa ta achchhaa jii aa dekho ye vaadaa nibhaanaa hamaarii galii aanaa ta achchhaa jii hamen na bhulaanaa aa achchhaa jii  ta dil men tumhiin ho samaae aur mere kayaalon pe chhaae 2 aa hamako bhii chain na aae ta achchhaa jii aa hamako bhii chain na aae ta muhabbat kaa hai ye zamaanaa aa hamaarii galii aanaa ta achchhaa jii muhabbat kaa hai ye zamaanaa aa hamaarii galii aanaa ta achchhaa jii hamen na bhulaanaa aa achchhaa jii  aa naiyaa hai tere hawaale o maanjhii mere matawaale 2 ta ham hain tere rakhawaale aa achchhaa jii ta ham hain tere rakhawaale aa naiyaa kinaare lagaanaa hamaarii galii aanaa ta achchhaa jii aa naiyaa kinaare lagaanaa  aa hamaarii galii aanaa ta achchhaa jii hamen na bhulaanaa aa achchhaa jii hamaarii galii aanaa ta achchhaa jii hamen na bhulaanaa aa achchhaa jii', 'correct_label': 'madan mohan', 'label': 5, 'split': 'test', 'title': 'hamaarii galii aanaa', 'year': '1956'}`
- output: `{"pred": "naushad", "top3": ["naushad", "c ramchandra", "s d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='naushad' ref='madan mohan'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='madan mohan' in top3=['naushad', 'c ramchandra', 's d burman']

### #490 — FAIL

- item: `{'lyrics': ' jab dil men nahiin hai khot to phir kyuun darataa hai naadaan yahaan jo karataa hai wo bharataa hai ho o o o o jab dil men nahiin hai khot to phir kyuun darataa hai naadaan yahaan jo karataa hai wo bharataa hai ho o o o o jab dil men nahiin hai khot to phir kyuun darataa hai  kahaan chalaa hai thokar khaane ye raste hain anajaane ik paap chhupaane kii kaatir sau paap na kar diiwaane 2 kyon jiite jii tuu maut kaa saudaa karataa hai naadaan yahaan jo karataa hai wo bharataa hai ho o o o o jab dil men nahiin hai khot to phir kyuun darataa hai  jab saaf teraa ye dil hai kis baat kii phir mushkil hai bhagawaan hai terii raxaa ko insaaf terii manzil hai 2 is raah men tuu dar dar ke qadam kyuun dharataa hai naadaan yahaan jo karataa hai wo bharataa hai ho o o o o jab dil men nahiin hai khot to phir kyuun darataa hai 2 ', 'correct_label': 'madan mohan', 'label': 5, 'split': 'test', 'title': 'jab dil men nahiin hai khot', 'year': '1959'}`
- output: `{"pred": "annu malik", "top3": ["annu malik", "c ramchandra", "a r rahman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='annu malik' ref='madan mohan'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='madan mohan' in top3=['annu malik', 'c ramchandra', 'a r rahman']

### #491 — FAIL

- item: `{'lyrics': ' beshaq mandir masjid tode bulleshaa ye kahataa  2 par pyaar bharaa dil kabhii na todothreedots is dil men dilavar rahataa jis palade men tule mohabbatthreedots jis palade men tule mohabbat usamen chaandii nahiin taulanaa taubaa merii naa dolanaa main nii bolanaa o nahiin bolanaa jaa main nahiin bolanaa jaa o main nahiin bolanaa jaa dolanaa main nii bolanaa taubaa merii na dolanaa main nii bolanaa  aag te ishq baraabar dono par paanii aag bujhaae  2 aashiq ke jab aansuu nikale aur agan lag jaae tere saamane baithake ronaathreedots o tere saamane baithake ronaa dil kaa dukhadaa nahiin tolanaa dolanaa main nii bolanaa o nahiin bolanaa jaa main nahiin bolanaa jaa ve main nahiin bolanaa jaa bolanaa main nii bolanaa taubaa merii na dolanaa main nii bolanaa ve main nahiin bolanaa o ve main nahiin bolanaa ve main nahiin bolanaa te main nahiin bolanaa nahiin bolanaa dolanaa main nii bolanaa nahiin bolanaa nahiin bolanaathreedots', 'correct_label': 'laxmikantpyarelal', 'label': 4, 'split': 'test', 'title': 'beshaq mandir masjid tode bulleshaah ye kahataa', 'year': '-1'}`
- output: `{"pred": "naushad", "top3": ["naushad", "annu malik", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='naushad' ref='laxmikantpyarelal'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='laxmikantpyarelal' in top3=['naushad', 'annu malik', 'laxmikantpyarelal']

### #492 — PASS

- item: `{'lyrics': ' kitanaa pyaaraa hai ye pyaar pyaaraa pyaaraa huaa hai pahalii baar hotaa hai ek baar phir naa hogaa ye dobaaraa  haay meraa dil churaake le gayaa churaane vaalaa meraa qaatil  haay meraa dil churaake le gaii churaane vaalii merii qaatil  ye dil tujhape aayaa hai aate aate dardedil to jaataa hai jaate jaate jaage hain soe hain ham dono khoe hain kaisii tanhaaii hai mastii sii chhaaii hai ye mausam hai pyaar ke qaabil haay meraa dil threedots  ab to kaate naa katen pyaasii raaten kuchh kuchh hotaa hai sunake aisii baaten bechainii sahane de palakon men rahane de terii baahon men hai terii raahon men hai jaanejaan merii manzil haay meraa dil threedots ', 'correct_label': 'annu malik', 'label': 1, 'split': 'test', 'title': 'kitanaa pyaaraa hai ye pyaar  haay meraa dil', 'year': '2000'}`
- output: `{"pred": "annu malik", "top3": ["annu malik", "r d burman", "kalyanjianandji"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='annu malik' ref='annu malik'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='annu malik' in top3=['annu malik', 'r d burman', 'kalyanjianandji']

### #493 — PASS

- item: `{'lyrics': '  ki \tteriimerii meriiterii nazar lad gaii 2 \tdo mulaakaaton men baaton hii baaton men \tchhotii sii baat badh gaii aa \tteriimerii meriiterii threedots ki \tteriimerii meriiterii nazar lad gaii \tteriimerii aa \tmeriiterii ki \thaay nazar lad gaii  aa \taaii nahiin niind kaii raaton se ho \thoke majabuur dil ke haathon se \tulfat o ho o ho ulfat karanii pad gaii \tteriimerii meriiterii threedots \tteriimerii ki \tmeriiterii aa \thaan nazar lad gaii  ki \tkabhii is kabhii us bahaane se ho \ttere kvaabon men aanejaane se 2 \thaalat o ho e he haalat merii bigad gaii \tteriimerii meriiterii threedots do \tdo mulaakaaton men threedots ', 'correct_label': 'laxmikantpyarelal', 'label': 4, 'split': 'test', 'title': 'teriimerii meriiterii nazar lad gaii', 'year': '1972'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "shankarjaikishan", "r d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='laxmikantpyarelal' ref='laxmikantpyarelal'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='laxmikantpyarelal' in top3=['laxmikantpyarelal', 'shankarjaikishan', 'r d burman']

### #494 — FAIL

- item: `{'lyrics': ' la baalii baalii umariyaa bhajan karuun kaise     chadhatii jawaanii jogan banuun kaise mu jhuuthaa jhuuthaa guru kaa vachan karuun kaise     saadhu huun teraa sajan banuun kaise     jhuuthaa  la ho chaal merii bahakii nazar merii dolii 2     chhuut gayaa bachapan badal gayii bolii mu terii tuu jaan mujhe chhod de akelaa     main na ban paauungaa saadhu se chhailaa     maayaa men man ko magan karuun kaise la chadhatii jawaanii threedots  mu naa ghar kii paravaah naa logon kaa dar hai 2     aisii kyaa terii hii chadhatii umar hai la jaane kyon tujh par na koii asar hai     terii aur merii baraabar umar hai     naazuk naazuk kamariyaa sambhal chaluun kaise mu saadhu huun teraa threedots  mu baar baar tujhako ye kaise samajhaauun 2     tujhase koii rishtaa main jod nahiin paauun la laaj lage batiyaan main kaise bataauun     aisaa naa ho main kunwaarii rah jaauun     thandii thandii ye man kii agan karuun kaise mu saadhu huun teraa threedots ', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'baalii umariyaa bhajan karuun kaise', 'year': '1975'}`
- output: `{"pred": "kalyanjianandji", "top3": ["kalyanjianandji", "laxmikantpyarelal", "madan mohan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='kalyanjianandji' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='shankarjaikishan' in top3=['kalyanjianandji', 'laxmikantpyarelal', 'madan mohan']

### #495 — FAIL

- item: `{'lyrics': '  la \ttan bhii badalaa man bhii badalaa badal gaii hai kaayaa \tkaalii raat se jiivan ko ab mil gaii ujalii chhaayaa ko \tye dil vaalon kii bastii hai ye basatebasate basatii hai \tgam ko kushii men dhaal de jo bhaarat kii aisii hastii hai \tjisane rachaa sansaar hai ye ham rachanaa us kii gaate hain  la \tluii shamaashaa uii 5 \tle jaa pyaar zaraa saa de jaa pyaar zaraa saa  uii  5 \tluii shamaashaa threedots ko \tluii shamaashaa threedots la \tluii shamaashaa threedots  \tmausam ne lii angadaaii hai qudarat ne baandhii paayal hai \thaay main kisakii baat karuun dil meraa hii ghaayal hai \trishton kii mehandii le aao 2 \t dulhan saa mujhe sajaao  2 rii \tprem kii bhaashaa uii 5 \tprem kii bhaashaa \tle jaa pyaar zaraa threedots ko \tluii shamaashaa threedots  ni \t ho dil chandaa kaa le aaenge suuraj se aankh milaaenge \taa jaaenge jab apanii par taaron ko tod ke laaenge  2 la \to ho ni \tmanzil hai apanii raahon men aakaash hamaarii baanhon men \tdekh tamaashaa uii 5 \tdekh tamaashaa \tle jaa pyaar zaraa threedots la \tuii 4 ko \tluii shamaashaa threedots  ni \tuthakar giranaa girakar uthanaa jiivan kii riit puraanii hai la \tuthakar giranaa girakar uthanaa jiivan kii riit puraanii hai \tchattaanon se takaraane kii hamane jiivan men thaanii hai do \tparavat ko dhuul banaa denge 2 \tsaagar ko buund banaa denge \tjaagii aashaa uii \tuii 5 \tjaagii aashaa uii jaagii aashaa \tle jaa pyaar zaraa threedots ', 'correct_label': 'laxmikantpyarelal', 'label': 4, 'split': 'test', 'title': 'tan bhii badalaa  luii shamaashaa uuii', 'year': '1981'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "r d burman", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='shankarjaikishan' ref='laxmikantpyarelal'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='laxmikantpyarelal' in top3=['shankarjaikishan', 'r d burman', 'laxmikantpyarelal']

### #496 — FAIL

- item: `{'lyrics': ' ye jiivan hai  is jiivan kaa yahii hai yahii hai yahii hai rang ruup 2 thode gam hain thodii khushiyaan yahii hai yahii hai yahii hai chhaanv dhuup ye jiivan hai threedots  ye naa socho isamen apanii haar hai ki jiit hai   2 use apanaa lo jo bhii jiivan kii riit hai ye zid chhodo yun naa todo har pal ek darpan hai ye jiivan hai threedots  dhan se naa duniyaa se ghar se na dvaar se saanson kii dor bandhii hai priitam ke pyaar se duniyaa chhuute par naa tuute ye kaisaa bandhan hai ye jiivan hai is jiivan kaa yahii hai yahii hai yahii hai rang ruup thode gam hain  thodii khushiyan yahii hai yahii hai yahii hai chhaanv dhuup ye jiivan hai', 'correct_label': 'laxmikantpyarelal', 'label': 4, 'split': 'test', 'title': 'ye jiivan hai is jiivan kaa yahii hai yahii hai yahii hai rang ruup', 'year': '-1'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "laxmikantpyarelal", "annu malik"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='r d burman' ref='laxmikantpyarelal'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='laxmikantpyarelal' in top3=['r d burman', 'laxmikantpyarelal', 'annu malik']

### #497 — FAIL

- item: `{'lyrics': '  merii taqadiir kahaan par mujhe le aaii hai saarii duniyaa merii ulfat kii tamaashaaii hai isalie laaj kaa pardaa hai mere chehare par khul gayaa raaz to isamen terii rusavaaii hai  raam kare kahiin nainaa na ulajhen 2 nainaa jo ulajhen to mushkil se sulajhe raam kare kahiin threedots  aae na jis din ghar saanvariyaa paagal banakar dhuundhe najariyaa morii kaayaa aise tadape jaise tadape jal bin machhariyaa raam kare kahiin threedots  jisake kaaran sab kuchh chhodaa usane mere dil ko todaa har tuufaan men saath rahaa vo aake kinaare mukhadaa modaa raam kare kahiin threedots ', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'merii taqadiir kahaan par  raam kare kahiin nainaa na ulajhen', 'year': '1967'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "shankarjaikishan", "naushad"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='shankarjaikishan' in top3=['laxmikantpyarelal', 'shankarjaikishan', 'naushad']

### #498 — FAIL

- item: `{'lyrics': ' maahii re maahii maahii re  aajaa maahii mere aajaa maahii mere aajaa maahii mere aa aa dhuup maluun main tere haathon men  aa sajadaa karuun main tere haathon men o subah kii mehandii chhalak rahii hai aajaa aajaa maahiyaa aajaa aajaa maahiyaa ho aajaa maahiyaa  aahistaa pukaaro sab sun lenge bas labon se chhuu lo lab sun lenge aa aankh bhii kal se phadak rahii hai aajaa aajaa maahiyaa threedots  ik nuur se aankhen chaunk gaiin dekhaa jo tujhe aaiine men koii nuur kiran hogii vo bhii jo chubhane lagii hai siine men aajaa maahiyaa threedots  laal ho jab ye shaam kinaaraa odhaa lenaa sar pe saaraa chal rok le suuraj chhup jaaegaa paanii men gir ke bujh jaaegaa aajaa maahiyaa threedots ', 'correct_label': 'annu malik', 'label': 1, 'split': 'test', 'title': 'aajaa maahiyaa aa dhuup maluun main', 'year': '2000'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "annu malik", "c ramchandra"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='r d burman' ref='annu malik'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='annu malik' in top3=['r d burman', 'annu malik', 'c ramchandra']

### #499 — FAIL

- item: `{'lyrics': '  muhabbat pe itanii javaanii na hotii agar tum na aate agar tum na aate kayaalon kii duniyaa suhaanii na hotii agar tum na aate agar tum na aate  ye chaahat na hotii ye aramaan na hote mere dil men khushiyon ke saamaan na hote hasiin is qadar zindagaanii na hotii agar tum na aate agar tum na aate muhabbat pe itanii   threedots  ye chup chup nazaare ye jhilamil sitaare bahut duur hain phir bhii lagate hain pyaare labon pe khushii kii kahaanii na hotii agar tum na aate agar tum na aate muhabbat pe itanii   threedots ', 'correct_label': 'c ramchandra', 'label': 2, 'split': 'test', 'title': 'muhabbat pe itanii javaanii na hotii', 'year': '1951'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "s d burman", "naushad"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='c ramchandra'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='c ramchandra' in top3=['laxmikantpyarelal', 's d burman', 'naushad']

### #500 — FAIL

- item: `{'lyrics': ' sangiit hai shakti iishvar kii har sur men base hain raam raagii ko sunaaye raag madhur rogii ko mile aaraam  ho chandan kaa palanaa resham kii dorii jhuulaa jhulaauun nindiyaa ko torii chandan kaa palanaa   threedots  so jaa tuu aise morii sajaniyaa so jaa tuu aise morii sajaniyaa sajiyaa pe soye jaise dulhaniyaa chandaa kaa tiikaa maathe lagaauun taaron kii maalaa tujhako pahanaauun taaron kii maalaa tujhako pahanaauun tohe sulaauun gaa gaa ke lorii jhuulaa jhuulaauun nindiyaa ko torii chandan kaa palanaa   threedots   uunche gagan se koii bulaaye laayiin hain pariyaan dolaa sajaaye sajan se milane duur chalii jaa udake tuu nindiyaa phurr chalii jaa udake tuu nindiyaa phurr chalii jaa chandaa pukaare aajaa chakorii jhuulaa jhuulaauun nindiyaa ko torii chandan kaa palanaa   threedots  ', 'correct_label': 'naushad', 'label': 6, 'split': 'test', 'title': 'chandan kaa palanaa resham kii dorii', 'year': '-1'}`
- output: `{"pred": "s d burman", "top3": ["s d burman", "naushad", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='s d burman' ref='naushad'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='naushad' in top3=['s d burman', 'naushad', 'laxmikantpyarelal']

### #501 — PASS

- item: `{'lyrics': '  ra \tjaane vaale kabhii nahiin aate \tjaane vaalon kii yaad aatii hai  su \tdil ek mandir hai 2 \tpyaar kii jisamen hotii hai puujaa \tye priitam kaa ghar hai \tdil ek mandir threedots  \t har dhadakan hai aaratii vandan \taankh jo miinchii ho gae darshan  2 \tmaut mitaa de chaahe hastii yaad to amar hai \tdil ek mandir threedots  \t ham yaadon ke phuul chadhaaen \taur aansuu ke diip jalaae  2 \tsaanson kaa har taar pukaare ye premnagar hai \tdil ek mandir threedots ', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'jaane vaale kabhii nahiin aate  dil ek mandir hai', 'year': '1963'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "s d burman", "naushad"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='shankarjaikishan' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='shankarjaikishan' in top3=['shankarjaikishan', 's d burman', 'naushad']

### #502 — FAIL

- item: `{'lyrics': ' tujhe kyaa sunaaun main dilarubaa tere saamane meraa haal hai terii ik nigaah kii baat hai merii zindagii kaa savaal hai  merii har kushii tere dam se hai merii zindagii tere gam se hai tere dard se rahe bekabar mere dil kii kab ye mazaal hai  tere husn par hai merii nazar mujhe subah shaam kii kyaa kabar merii shaam hai terii justajuu merii subaha teraa kayaal hai  mere dil jigar men samaa bhii jaa rahe kyon nazar kaa bhii faasalaa ke tere bagair o jaanejaan mujhe zindagii bhii muhaal hai', 'correct_label': 'madan mohan', 'label': 5, 'split': 'test', 'title': 'tujhe kyaa sunaauun main dilarubaa tere saamane meraa haal hai', 'year': '-1'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "laxmikantpyarelal", "madan mohan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='shankarjaikishan' ref='madan mohan'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='madan mohan' in top3=['shankarjaikishan', 'laxmikantpyarelal', 'madan mohan']

### #503 — FAIL

- item: `{'lyrics': ' dil se dil zaraa milaa hii lo duurduur na rahaa karo  dil tumhaaraa ab tumhiin rakho nako re baabaa malaa nako  hamase tum zaraa gale milo pyaar kaa zaraa mazaa chakho  duur se hii tum milaa karo nako re baabaa malaa nako  dekho socho sanam is jahaan men tumhen aisaa aashiq phir dhuundhe milegaa nahiin  dil se dil zaraa milaa hii lo duurduur na rahaa karo dil tumhaaraa ab tumhiin rakho nako re baabaa malaa nako hamase tum zaraa gale milo pyaar kaa zaraa mazaa chakho duur se hii tum milaa karo nako re baabaa malaa nako dekho socho sanam is jahaan men tumhen aisaa aashiq phir dhuundhe milegaa nahiin  dil se dil zaraa milaa hii lo duurduur na rahaa karo dil tumhaaraa ab tumhiin rakho nako re baabaa malaa nako  dede dil mujhako aaj dikhaa de zindaadilii  le lo jaan chaahen lekin ye dil nahiinnahiin  khilaakhilaa aasmaan khilaakhilaa ye samaan   aise mausam men ye duuriyaan kyuun hain bhalaa  terii ye mastiyaan terii chanchal nigaah  koii asar naa karegii re jaa re jaa  dil se dil zaraa milaa hii lo duurduur na rahaa karo dil tumhaaraa ab tumhiin rakho nako re baabaa malaa nako hamase tum zaraa gale milo pyaar kaa zaraa mazaa chakho duur se hii tum milaa karo nako re baabaa malaa nako dekho socho sanam is jahaan men tumhen aisaa aashiq phir dhuundhe milegaa nahiin  kyaakyaa kahataa hai aur dil diivaanaa teraa  likh duun main tere liye ye jiivan ai dilarubaa  aisaa hai to aa yahaan tanman hai teraa  tere qadamon men hai ye dil aur ye jaan  nahiin nahiin jaanejaan terii jagah hai yahaan  kahate hain jisako dil vo hai teraa jahaan   dil se dil zaraa milaa hii lo duurduur na rahaa karo dil tumhaaraa ab tumhiin rakho nako re baabaa malaa nako hamase tum zaraa gale milo pyaar kaa zaraa mazaa chakho duur se hii tum milaa karo nako re baabaa malaa nako dekho socho sanam is jahaan men tumhen aisaa aashiq phir dhuundhe milegaa nahiin  2  dil se dil zaraa milaa hii lo duurduur na rahaa karo dil tumhaaraa ab tumhiin rakho nako re baabaa malaa nako ', 'correct_label': 'a r rahman', 'label': 0, 'split': 'test', 'title': 'dil se dil zaraa milaa hii lo duurduur na rahaa karo', 'year': '1996'}`
- output: `{"pred": "kalyanjianandji", "top3": ["kalyanjianandji", "s d burman", "a r rahman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='kalyanjianandji' ref='a r rahman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='a r rahman' in top3=['kalyanjianandji', 's d burman', 'a r rahman']

### #504 — FAIL

- item: `{'lyrics': '   tujhasaa hasiin dekhaa naa kahiin tuu hogii meharabaan kabhii naa kabhii  2  pahale milan men hotii hai kashamakash pyaar se pahale hotii hai kashamakash tere jo dil men hai merii nazar men hai chaahat men hotii hai ko \t kashamakash 4 2  tujhasaa hasiin threedots   qudarat kaa tuu ek karishmaa hai gulabadan pichhale janam kaa koii rishtaa hai gulabadan mahakaa huaa shabaab jaise koii gulaab teraa nahiin javaab ko \tgulabadan 4   2  tujhasaa hasiin threedots ', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'tujhasaa hasiin dekhaa naa kahiin', 'year': '1981'}`
- output: `{"pred": "annu malik", "top3": ["annu malik", "laxmikantpyarelal", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='annu malik' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='r d burman' in top3=['annu malik', 'laxmikantpyarelal', 'shankarjaikishan']

### #505 — PASS

- item: `{'lyrics': ' re re re re rere  raa raa raa raaraa he he he he hehe  o ho o ho oho  ai masakkalii masakkalii masakkalii ud matakalii matakalii ai masakkalii masakkalii masakkalii ud matakalii matakalii masakkalii masa masa kalii ud matakkalii matakkalii threedots  zaraa pankh jhatak gaii dhuul atak aur lachak machak ke duur bhatak ud dagar dagar kasabe kuuche nukkad bastii men yaay yaay ye titaliisii mud adaa se ud kar le puurii dil kii tamannaa havaa se jud adaa se ud phurr phurr phurr tuu hai hiiraa pannaa re masakkalii masakkalii masakkalii matakkalii matakkalii threedots  ghar teraa salonii baadal kii kolonii dikhalaa de thengaa un sab ko jo udanaa na jaane udiyo na dariyo kar manmaanii manmaanii manmaanii badhiyo na mudiyo kar naadaanii udiyo na dariyo kar manmaanii manmaanii manmaanii badhiyo na mudiyo kar naadaanii jab taan le muskaan le kare sana nana nana nana havaa bas thaan le tuu jaan le kahe sana nana nana nana nana havaa  masakkalii masakkalii masakkalii matakkalii matakkalii threedots  re re re re rere  raa raa raa raaraa  tujhe kyaa gam teraa rishtaa gagan kii baansurii se hai pavan kii guftaguu se hai suuraj kii roshanii se hai udiyo na dariyo kar manmaanii manmaanii manmaanii badhiyo na mudiyo kar naadaanii udiyo na dariyo kar manmaanii manmaanii manmaanii badhiyo na mudiyo kar naadaanii jab taan le muskaan le kare sana nana nana nana havaa bas thaan le tuu jaan le kahe sana nana nana nana nana havaa  masakkalii masakkalii masakkalii matakkalii matakkalii threedots  re re re re rere  raa raa raa raaraa he he he he hehe  o ho o ho oho ', 'correct_label': 'a r rahman', 'label': 0, 'split': 'test', 'title': 'masakkalii masakkalii', 'year': '2009'}`
- output: `{"pred": "a r rahman", "top3": ["a r rahman", "s d burman", "madan mohan"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='a r rahman' ref='a r rahman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='a r rahman' in top3=['a r rahman', 's d burman', 'madan mohan']

### #506 — FAIL

- item: `{'lyrics': '  kise maaluum thaa do din men saavan biit jaayegaa tamannaaen hamarii yuun tadapatii chhod jaayegaa saavan biit jaayegaa kise maaluum thaa threedots  dilebetaab terii yaad men aansuu bahaayegaa hamen rahrah ke ye zaalim zamaanaa yaad aayegaa saavan biit jaayegaa kise maaluum thaa do din men threedots  zabaan bedardiyaan us kii na kahane paayegii lekin hamaarii aankh kaa paanii kahaanii kah sunaayegaa saavan biit jaayegaa kise maaluum thaa threedots  jahaan vaalon are ham ne kisii kaa kyaa bigaadaa thaa hamaarii raah men bhagavaan bhii kaante bichhaayegaa saavan biit jaayegaa kise maaluum thaa threedots ', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'kise maaluum thaa do din men saavan biit jaayegaa', 'year': '1948'}`
- output: `{"pred": "naushad", "top3": ["naushad", "kalyanjianandji", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='naushad' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='s d burman' in top3=['naushad', 'kalyanjianandji', 'shankarjaikishan']

### #507 — FAIL

- item: `{'lyrics': ' merii zindagi ke chiraag ko terii berukii ne bujhaa diyaa tere raaste kii main kaak huun mujhe aaj tuune basaa diyaa  tujhe paake bhii terii justujuu tujhe milake bhii terii aarzuu tere paas laake nasiib ne mujhe kitanii duur hataa diyaa  tuu vo phuul jisamen vafaa nahiin main vo dard jisakii dawaa nahiin tujhe dekhakar jo ye lab hanse terii aarzuu ne rulaa diyaa', 'correct_label': 'laxmikantpyarelal', 'label': 4, 'split': 'test', 'title': 'merii zindagi ke chiraag ko terii berukii ne bujhaa diyaa', 'year': '1967'}`
- output: `{"pred": "c ramchandra", "top3": ["c ramchandra", "s d burman", "kalyanjianandji"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='c ramchandra' ref='laxmikantpyarelal'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='laxmikantpyarelal' in top3=['c ramchandra', 's d burman', 'kalyanjianandji']

### #508 — PASS

- item: `{'lyrics': ' aan milo yaa milane se inkaar karo faisalaa jo bhii karanaa hai ik baar karo dil men rah kar baat asar kho baithegii honth hain chup to aankhon se ikaraar karo  khullam khullaa naa aise izahaar karo chorii chorii jo karanaa ho yaar karo diivaane ho diivaanaapan karate ho jaao jaao aise naa takaraar karo aan milo yaa threedots  bechain huun main betaab tum ho dekho na aise naa naa karo samajho merii kyaa majabuuriyaan hain dekho naa aise aahen bharo dardejigar kaise sahuun main tere bin kaise rahuun aise chhup chhup ke naa tum diidaar karo thodaa thaharo phir jii bhar ke pyaar karo dil men rah kar threedots  achchhaa nahiin hai itanaa sataanaa achchhii nahiin ye diivaanagii kaise bujhaauun bujhatii nahiin hai ye pyaas kaisii man men jagii paagal bade tum ho sanam chhedo na yuun tum ko kasam paas baitho baaten tum do chaar karo thodaa thaharo phir jii bhar ke pyaar karo faisalaa jo bhii threedots', 'correct_label': 'annu malik', 'label': 1, 'split': 'test', 'title': 'aan milo yaa milane se inkaar karo', 'year': '1999'}`
- output: `{"pred": "annu malik", "top3": ["annu malik", "laxmikantpyarelal", "r d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='annu malik' ref='annu malik'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='annu malik' in top3=['annu malik', 'laxmikantpyarelal', 'r d burman']

### #509 — FAIL

- item: `{'lyrics': ' aaj furakat ka khvaab tuut gayaa  mil gaye tum hijaab tuut gayaa   tum se izahaarehaal kar baithe  bekhudii men kamaal kar baithe  tum se izahaarehaal threedots  kho gaye husn ki bahaaron men  kah diyaa raazedil ishaaron men  kaam ham bemisaal kar baithe  bekhudii men kamaal kar baithe  tum se izahaarehaal threedots  kitane majabuur ho gaye dil se  soche samajhe bagair qaatil se  zindagii ka savaal kar baithe  bekhudii men kamaal kar baithe  tum se izahaarehaal threedots  ye adaaen ye shokhiyaan taubaa  bas khudaa hii khudaa hai us dil ka  jo tumhaaraa khayaal kar baithe  bekhudii men kamaal kar baithe  tum se izahaarehaal threedots', 'correct_label': 'naushad', 'label': 6, 'split': 'test', 'title': 'tum se izahaarehaal kar baithe bekhuudii men kamaal kar baithe', 'year': '1963'}`
- output: `{"pred": "madan mohan", "top3": ["madan mohan", "shankarjaikishan", "naushad"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='madan mohan' ref='naushad'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='naushad' in top3=['madan mohan', 'shankarjaikishan', 'naushad']

### #510 — FAIL

- item: `{'lyrics': ' kyon yaad aa rahe hain  guzare hue zamaane  ye sukh bhare fasaane  rote hue taraane  kisako sunaa rahe hain  kyon yaad rahe hain   kyon muskuraa rahe hain  dekho agar to samajho  aansuu bahaa rahe hain  kyon yaad aa rahe hain   kyaa vaqt hai na jaane  kyon hichakiyon kii lay pe  gaate gam ke gaane  ham bhor ke diye hain  bujhate hii gaa rahe hain  kyon yaad aa rahe hain ', 'correct_label': 'naushad', 'label': 6, 'split': 'test', 'title': 'kyon yaad aa rahe hain', 'year': '1946'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "naushad", "madan mohan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='naushad'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='naushad' in top3=['laxmikantpyarelal', 'naushad', 'madan mohan']

### #511 — FAIL

- item: `{'lyrics': ' la laa laa laa laa laa laa laa laa la laa laa laa laa laa laa laa laa   i love you you love me  2 lo mohabbat ho gaii  terii do aankhon men  2 merii duniyaa kho gaii  i love you you love me  2  ye to pahalii mulaaqaat hai abhii shuruu hue do fasaane abhii bane miit puraane teraa meraa ajab saath hai abhii mile do anjaane abhii lage kahane do diiwaanae suno   i love you you love me  2 lo mohabbat ho gaii  kyaa hai kyon hai agar kuchh nahiin binaa piye nashaa chhaa rahaa hai terii qasam mazaa aa rahaa hai hamako tumako kabar kuchh nahiin pataa nahiin kaun jaa rahaa hai pataa nahiin kaun aa rahaa hai suno   i love you you love me  2 lo mohabbat ho gaii terii do aankhon men merii duniyaa kho gaii  i love you you love me  5 ', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'i love you you love me', 'year': '1976'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "annu malik", "kalyanjianandji"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='r d burman' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='s d burman' in top3=['r d burman', 'annu malik', 'kalyanjianandji']

### #512 — FAIL

- item: `{'lyrics': '  haq maangate hain apane pasiine kaa adhikaar hamen bhii hai jiine kaa  tum laakh amiiron aish karo ham dekh tumhen kab jalate hain saae men tumhaare mahalon ke lekin kitane gam palate hain dekho to nazaaraa aake kabhii gam khaane aansuu piine kaa haq maangate hain threedots  mehanat pe hamaarii hii tumane ye shiishamahal hai khadaa kiyaa tum jinako chhotaa kahate ho in chhoton ne tumako badaa kiyaa kyon saal ke piichhe chubhataa hai phir bonas ek mahiine kaa haq maangate hain threedots  tum khud bhii jiyo aur jiine do  hai maang yahii mazaduuron kii insaaf karo insaaf karo aah na lo mazaduuron kii sholaa na kahiin banakar bhadake ab tak jo dhuaan hai siine kaa haq maangate hain threedots ', 'correct_label': 'madan mohan', 'label': 5, 'split': 'test', 'title': 'haq maangate hain apane pasiine kaa', 'year': '1959'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "r d burman", "s d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='madan mohan'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='madan mohan' in top3=['laxmikantpyarelal', 'r d burman', 's d burman']

### #513 — FAIL

- item: `{'lyrics': '  jaapaan love in tokyo 2 le gaii dil gudiyaa jaapaan kii 2 paagal mujhe kar diyaa 2 jaapaan love in tokyo threedots  ye to shahar mastaanaa jisakaa andaaz maashuuqaanaa detaa hai pyaar kaa paimaanaa karataa hai sabako diivaanaa 2 le gaii dil threedots  dekho vo goriigorii raahen hamako ishaare se bulaaen kitanii rangiin hain fizaaen jaapaanii pariyaan muskaraaen 2 le gaii dil threedots  naache har mod par javaanii kahatii hai pyaar kii kahaanii aaii vo kaibare kii raanii jisakii adaa men zindagaanii 2 le gaii dil threedots ', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'jaapaan love in tokyo le gaii dil gudiyaa jaapaan kii', 'year': '1966'}`
- output: `{"pred": "annu malik", "top3": ["annu malik", "shankarjaikishan", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='annu malik' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='shankarjaikishan' in top3=['annu malik', 'shankarjaikishan', 'laxmikantpyarelal']

### #514 — PASS

- item: `{'lyrics': '  chhotiisii ye duniyaa pahachaane raaste hain  tum kabhii to miloge kahiin to miloge to puuchhenge haal  chhotiisii ye duniyaa   ham to ye samajhenge hamane ek patthar ko puujaa  lekin tumako apane jaisaa nahiin milegaa duujaa nahiin milegaa duujaa  chhotiisii ye duniyaa   siikhaa nahiin hamaare dil ne pyaar men dhiiraj khonaa  aag men jalake bhii jo nikhaare hai vahii sachchaa sonaa hai vahii sachchaa sonaa  chhotiisii ye duniyaa   dil kii daulat mat thukaraao dekho pachhataaoge aaj chale jaate ho jaise laut ke bhii aaoge laut ke bhii aaoge  chhotiisii ye duniyaa     chhotiisii ye duniyaa pahachaane raaste hain  tum kabhii to miloge kahiin to miloge to puuchhenge haal  chhotiisii ye duniyaa   siikhaa nahiin hamaare dil ne pyaar men dhiiraj khonaa  aag men jalake bhii jo nikhaare vahii hai sachchaa sonaa vahii hai sachchaa sonaa  chhotiisii ye duniyaa   meraa pahalaa pyaar aakharii bhii hai is jiivan kaa ek baar hotaa hai jag men rishtaa man se man kaa rishtaa man se man kaa chhotiisii ye duniyaa ', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'chhotiisii ye duniyaa pahachaane raaste hain', 'year': '1962'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "madan mohan", "s d burman"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='shankarjaikishan' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='shankarjaikishan' in top3=['shankarjaikishan', 'madan mohan', 's d burman']

### #515 — FAIL

- item: `{'lyrics': '  prem kaa rog badaa buraa maakaa nakaa ga baaii maakaa nakaa aisaa mere ko merii maan ne kahaa maakaa nakaa nakaa baaii maakaa nakaa prem kaa rog badaa buraa   ro ro ka kate ye din kahaan kal raaton ko rahuungii  nanhe se dil men baabaa kaise main ye dukh sahuungii kachchii kalii huun rang dekho zaraa dil dil dil bhii hai naazuk meraa prem kaa rog badaa buraa   phir bhii karuun main kyaa ki tuu badaa pyaaraa mohe laage par kaise teraa meraa milan ho tuu hii bataade abhii abhii abhii haath chhodo meraa dekho dekho dekho koii hai tiisaraa prem kaa rog badaa buraa  ', 'correct_label': 'laxmikantpyarelal', 'label': 4, 'split': 'test', 'title': 'prem kaa rog badaa buraa', 'year': '1976'}`
- output: `{"pred": "s d burman", "top3": ["s d burman", "c ramchandra", "a r rahman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='s d burman' ref='laxmikantpyarelal'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='laxmikantpyarelal' in top3=['s d burman', 'c ramchandra', 'a r rahman']

### #516 — FAIL

- item: `{'lyrics': ' are ladakaa hai chaand jaisaa ladakii chakorii  allaah salaamat rakhe donon kii jodii  sone kaa palang banaanaa bistar pe taare bichhaanaa  chandaa kii dolii men bithaa ke dulhan ko tum le jaanaa 2  sone kaa palang banaanaa bistar pe taare bichhaanaa chandaa kii dolii men bithaa ke dulhan ko tum le jaanaa  hoy sone kaa palang puraanaa dolii kaa guzaraa zamaanaa  dulhan ko baanhon men uthaa ke le jaayegaa ye diivaanaa 2  are hiiremotii kii anguuthii naa chaandii kii suramedaanii   e e e e e oye oye oye oye oye  daulat naa dekho mere dil ko dekho  chhup ke akele men tum hamase mil ke dekho  tuu kaisaa chhailaa nahale pe dahalaa  tuu sabako chhede par pyaar hai meraa pahalaa  vo kaun hai bolo vo terii ek sahelii  par kaisii hai vo laakhon men ek akelii  jo vo naa maane to us se puuchh ke dekho  us kii suurat pe likhaa hai mere pyaar ka afasaanaa  sone kaa palang banaanaa bistar pe taare bichhaanaa chandaa kii dolii men bithaa ke dulhan ko tum le jaanaa 2  hoy ladakaa hai chaand jaisaa ladakii chakorii allah salaamat rakhe donon kii jodii  2  achchhaaachchhaa teraa pyaar agar hai sachchaa  ham ladakii se mil ke kar denge rishtaa pakkaa  haay ai ai ai ai ai 2  ladakii kii band zubaan hai isakaa matalab haan hai  lagataa hai haannaa ke biich men ladakii terii jaan hai  chal merii banno ye sharm chhod de  dil tod de yaa dil ko jod de  aankhon men intazaar hai ye dil bhii beqaraar hai  isii kaa naam pyaar hai mujhako pyaar hai mujhako pyaar hai  ab tum kuchh bhii bolo ye laaj kaa ghuunghat kholo  re jaa re jaa na chhed is ko gaa ke aisaa filmii gaanaa  sone kaa palang banaanaa bistar pe taare bichhaanaa chandaa kii dolii men bithaa ke dulhan ko tum le jaanaa 2 ', 'correct_label': 'a r rahman', 'label': 0, 'split': 'test', 'title': 'are ladakaa hai chaand jaisaa  sone kaa palang banaanaa', 'year': '2001'}`
- output: `{"pred": "annu malik", "top3": ["annu malik", "a r rahman", "c ramchandra"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='annu malik' ref='a r rahman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='a r rahman' in top3=['annu malik', 'a r rahman', 'c ramchandra']

### #517 — PASS

- item: `{'lyrics': '        yaarii ho gaii  2 yaarii ho gaii yaar se lak tunu tunu pyaar ko kaam kyaa jhuuthe sansaar se yaarii ho gaii threedots  os men bhiige bhiige aakaash ke tale jaane ham jal jaanaa lagakar yaar ke siine se ho chuur thakan se hoke jab saans naa chale hamako jiivan mil jaataa hai jahar ke piine se jiite hai pyaar se marate hai pyaar se haan yaarii ho gaii threedots  dharam sadaa apanaa to hansanaa bolanaa lukanaa chhupanaa kyaa jaane ham hod men aanchal kii ho karam sadaa apanaa to khulake dolanaa laharaatii bainyaan hain aur ye taal hai paayal kii guunjatii har galii prem jhankaar se haan yaarii ho gaii threedots ', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'yaarii ho gaii yaar se', 'year': '1972'}`
- output: `{"pred": "r d burman", "top3": ["r d burman", "laxmikantpyarelal", "kalyanjianandji"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='r d burman' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='r d burman' in top3=['r d burman', 'laxmikantpyarelal', 'kalyanjianandji']

### #518 — FAIL

- item: `{'lyrics': ' do lafzon kii hai dil kii kahaanii yaa hai mohabbat yaa hai javaanii  dil kii baaton kaa matalab na puuchho kuchh aur hamase bas ab na puuchho jisake liye hai duniyaa diivaanii yaa hai mohabbat yaa hai hai javaanii  is zindagii ke din kitane kam hai kitane hai kushiyaan aur kitane gam hain lag jaa gale se rut hai suhaanii yaa hai mohabbat yaa hai javaanii  ye kashtii vaalaa kyaa gaa rahaa hai koii ise bhii yaad aa rahaa hai jisake liye hai duniyaa diivaanii yaa hai mohabbat yaa hai javaanii  do lafzon kii hai dil kii kahaanii yaa hai mohabbat yaa hai javaanii ', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'do lafzon kii hai dil kii kahaanii', 'year': '1979'}`
- output: `{"pred": "naushad", "top3": ["naushad", "r d burman", "a r rahman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='naushad' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='r d burman' in top3=['naushad', 'r d burman', 'a r rahman']

### #519 — PASS

- item: `{'lyrics': '  jiivan bhar dhuundhaa jisako vo pyaar milaa par nahiin milaa saath nibhaataa sukhdukh men vo yaar milaa par nahiin milaa jiivan bhar dhuundhaa threedots  usakii suurat aankhon men usakaa jalavaa dil men hai mujhako aisaa lagataa hai jaise vo mahafil men hai rang badalatii duniyaa men diladaar milaa par nahiin milaa jiivan bhar dhuundhaa threedots  is duniyaa kii riit kii kaatir maine baat nibhaaii hai yuun to hansataa rahataa huun par chot jigar pe khaaii hai chaahat ke doraahe par gamakvaar milaa par nahiin milaa jiivan bhar dhuundhaa threedots ', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'jiivan bhar dhuundhaa jisako vo pyaar milaa', 'year': '1971'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "annu malik", "naushad"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='shankarjaikishan' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='shankarjaikishan' in top3=['shankarjaikishan', 'annu malik', 'naushad']

### #520 — PASS

- item: `{'lyrics': '  aisii muhabbat se ham baaz aaye jo dil ko jalaaye sataaye dukhaaye dil ko jalaaye sataaye dukhaaye  aisii muhabbat se ham baaz aaye jo dil ko jalaaye sataaye dukhaaye  banaakar tumhen apanaa kyaa hamane paayaa khushii lut gayii chain dil kaa ganvaayaa 2 bade gam sahe aur bahut dukh uthaaye aisii muhabbat se ham baaz aaye threedots  tasavvur men tumase huii kitanii baaten guzaarii bahut jaag kar hamane raaten 2 kabhii hamane chhup chhup ke aansuu bahaaye aisii muhabbat se ham baaz aaye threedots  aisii muhabbat se ham baaz aaye jo dil ko jalaaye sataaye dukhaaye dil ko jalaaye sataaye dukhaaye ', 'correct_label': 'c ramchandra', 'label': 2, 'split': 'test', 'title': 'aisii muhabbat se hum baaz aaye', 'year': '0'}`
- output: `{"pred": "c ramchandra", "top3": ["c ramchandra", "s d burman", "naushad"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='c ramchandra' ref='c ramchandra'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='c ramchandra' in top3=['c ramchandra', 's d burman', 'naushad']

### #521 — FAIL

- item: `{'lyrics': '  main to pyaar se tere piyaa maang sajaauungii tere anganaa ye saarii umariyaa bitaauungii  sajdhaj ke main savere savere mahakii mahakii karatii huun phere lagatii huun kaise tuu bhii to dekhe khol de akhiyaan saajan mere tere haathob se ye ghuunghat uthaauungii tere anganaa ye threedots   tohe rakh luungii jiyaa men basaa ke dekhuungii phir shiish jhukaake ghar ko tere jaan ke mandir aur mandir men tujhe bithaa ke diyaa gore gore tan kaa jalaauungii tere anganaa ye threedots ', 'correct_label': 'naushad', 'label': 6, 'split': 'test', 'title': 'main to pyaar se tere piyaa maang sajaauungii', 'year': '1968'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "s d burman", "annu malik"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='naushad'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='naushad' in top3=['laxmikantpyarelal', 's d burman', 'annu malik']

### #522 — FAIL

- item: `{'lyrics': '  mu \ttere hamasafar giit hain tere \tgiit hii to jiivan miit hain tere \tho nagamen pyaar ke tuu gaae jaa \tgaae jaa aur muskaraae jaa \ttere hamasafar giit threedots  ki \ttere hamasafar giit hain tere mu \tho nagamen pyaar ke threedots ki \ttere hamasafar giit hain tere mu \ttere hamasafar giit hain tere ko \tla la laa  ki \tsundarataa kii o shahazaadii husn kii devii \tai muurat kaamoshii kii \titanii pyaarii suurat le ke kaash ki tuu bhii \tmere sur men jaa sakatii \thar dil koo diivaanaa tuu banaa detii jaaneman 2 \ttere hamasafar giit threedots  \tgaao gaao naa shaabaash aa \taa aa ki \tlaa laa la la laa bolo la la laa aa \taa aa ki \ttere aa \ttere ki \thamasafar aa \tsafar ki \tgiit hain tere aa \ttere ki \tlaa laa la laa aa \tjiivan laa laa laa aa \ttere hamasafar giit hain tere \tgiit hii to jiivan miit hain tere ki \tho nagamen pyaar ke threedots aa \ttere hamasafar giit threedots ki \ttere hamasafar giit threedots ko \tla la laa  aa \tmere hamadam mere saathii terii dhun men \tkyaa jaaduu hai kyaa jaane \to mere hamadam threedots \tgunagunaane lage dil ke viiraane \tdekho naa gunagunaane lage dil ke viiraane ki aa \ttere hamasafar giit threedots aa \tho nagamen pyaar ke threedots  mu \tgiit sunaa ke saaj bajaa ke pal do pal ko \tdukhiyon kaa dil bahalaa ke aa \tlaa laa laa mu \to giit sunaa ke threedots \tkoii kaam kar gae ham to ye jaanen duniyaa men 2 ki aa \ttere hamasafar giit threedots mu \tnagamen pyaar ke tuu gaae jaa mu ki aa \tgaae jaa aur muskaraae jaa \ttere hamasafar giit threedots ', 'correct_label': 'r d burman', 'label': 7, 'split': 'test', 'title': 'tere hamasafar giit hain tere', 'year': '1975'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "kalyanjianandji", "shankarjaikishan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='r d burman'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='r d burman' in top3=['laxmikantpyarelal', 'kalyanjianandji', 'shankarjaikishan']

### #523 — FAIL

- item: `{'lyrics': '  ole ole ole ole ole ole o dil kii manzil kuchh aisii hai manzil pyaar jis ne kiyaa ho vo jaane  pahaluu men yuun to sab ke hii dil hai dard ho jis men dil vahii dil hai pahaluu men yuun to sab ke hii dil hai dard ho jis men dil vahii dil hai pyaar jo hogaa dard bhii hogaa pyaar na ho to jiinaa mushkil hai aaj kis se javaan hai ye mahafil pyaar jis ne kiyaa ho vo jaane  dil kii manzil kuchh aisi hai manzil threedots  itanaa badaa hai duniyaan kaa melaa log dilon se milate nahiin hain itanaa badaa hai duniyaan kaa melaa log dilon se milate nahiin hain pyaar binaa to dono jahaan men phuul khushii ke khilate nahiin hain kaun kis kaa huaa hai qaatil pyaar jis ne kiyaa ho vo jaane  dil kii manzil kuchh aisi hai manzil threedots ', 'correct_label': 's d burman', 'label': 8, 'split': 'test', 'title': 'dil kii manzil kuchh aisii hai manzil', 'year': '1963'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "madan mohan", "naushad"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='shankarjaikishan' ref='s d burman'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='s d burman' in top3=['shankarjaikishan', 'madan mohan', 'naushad']

### #524 — FAIL

- item: `{'lyrics': ' sanvar gaii sanvar gaii qisamat ye sanvar gaii 2  milaa duulhaa aisaa dulhan nikhar gaii  2  sanvar gayaa sanvar gayaa nasiibaa sanvar gayaa   milii dulhan aisii duulhaa nikhar gayaa 2  nasiibon vaalaa hai kushii ye paaii hai   khile hain phuul tere sahare ke   kushii mubaarak ho dulhan   ye naii subah jiivan kii   tujhape chhayen naa koii andhere   baabul ne god khilaayaa tuu un se bhii sharmaaii   kaisaa ye vaqt hai aayaa duhaaii   in baanhon men jhulaayaa har gam se tujhako bachaayaa   tuu ham ko hii dard de jaayegii   pyaar se bharenge daaman le jaayenge tujhe saajan   tere liye sajaaii mahafil tuu banii hai suhaagan   baabul bhii naachenge jhuumenge   haay haay haay haay haay haay haay 2 haay haay haay haay haay haay haay haay  haay haay haay  haay haay haay haay haay haay  haay haay haay haay haay haay haay 2 haay haay haay   o charaagon ke badale jalegaa ye dil ab roshan hogii aisii shaamen merii 2  hawaaon ko thandak milegii jyaadaa un men ghulengii jab ye aahen merii   tuu agar nazar aayegii ye nigaah jhuk jaayegii   tere saaye ko chuumegii aankh ye bhar aayegii   par duaayen dengii tujhako jiivan bhar   kushiyon kii jiivan bhar kushiyon kii   sanvar gaii sanvar gaii qisamat ye sanvar gaii  milaa duulhaa aisaa dulhan nikhar gaii 2  sanvar gayaa sanvar gayaa nasiibaa sanvar gayaa  milii dulhan aisii duulhaa nikhar gayaa 2   kaajal se aankhen kiyaa kajaraarii   gajaron se mahakaaiin zulfen sunaharii   kaajal se aankhen kiyaa kajaraarii  gajaron se mahakaaiin zulfen sunaharii   sar se paanv tak gahanon men saj ke   aaii shaamiyaane men dulhan navelii   mridang kii taal pe baandhe haar dulhan ko duulhaa   ek akelaa dil phuulon ko barsaa ke detaa hai ye duaa   tum sadaa hii jiitii rahanaa phuulon men   kushiyon men phuulon men kushiyon men   sanvar gaii sanvar gaii qisamat ye sanvar gaii  milaa duulhaa aisaa dulhan nikhar gaii 2  sanvar gayaa sanvar gayaa nasiibaa sanvar gayaa  milii dulhan aisii duulhaa nikhar gayaa 2  baabul ne god khilaayaa tuu un se bhii sharmaaii  kaisaa ye vaqt hai aayaa duhaaii  in baanhon men jhulaayaa har gam se tujhako bachaayaa  tuu ham ko hii dard de jaayegii  ', 'correct_label': 'a r rahman', 'label': 0, 'split': 'test', 'title': 'sanvar gaii sanvar gaii qisamat ye sanvar gaii', 'year': '1999'}`
- output: `{"pred": "kalyanjianandji", "top3": ["kalyanjianandji", "laxmikantpyarelal", "a r rahman"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='kalyanjianandji' ref='a r rahman'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='a r rahman' in top3=['kalyanjianandji', 'laxmikantpyarelal', 'a r rahman']

### #525 — FAIL

- item: `{'lyrics': ' oye hoye gore haathon par na zulm karo haazir hai ye bandaa huqm karo tumhaarii kanvaarii kalaaii ko daag na lage gore haathon par   threedots  jaaneman in haathon men to mehandii kaa rang laganaa hai haay pyaar kii rangat se teraa naazuk ang ang sajanaa hai hai kaun sii aisii majabuurii jo husn kare ye mazaduurii tumhaarii kanvaarii kalaaii ko   threedots  mahalon kii tum raanii ho main priit nagar kaa shahazaadaa baant len ham kyon na dono dhan apanaa aadhaa aadhaa ham kaam karen tum raaj karo manzuur to haath pe haath dharo tumhaarii kanvaarii kalaaii ko   threedots  gusse men jo ulajhii hai aao to vo lat main sulajhaa duun haay chhede jo zulfen terii us shokh havaa ko rukavaa duun dekho na yuun aankhen malmal ke pad jaayenge dhabbe kaajal ke tumhaarii kanvaarii kalaaii ko   threedots ', 'correct_label': 'laxmikantpyarelal', 'label': 4, 'split': 'test', 'title': 'gore haathon par na zulm karo', 'year': '1966'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "kalyanjianandji", "annu malik"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='shankarjaikishan' ref='laxmikantpyarelal'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='laxmikantpyarelal' in top3=['shankarjaikishan', 'kalyanjianandji', 'annu malik']

### #526 — FAIL

- item: `{'lyrics': '  mu \taankhon men rang kyuun aayaa bolo nashaa saa kyon chhaayaa \thamako ye raaz batalaao dil kho ke tumane kyaa paayaa la \tchamakii nasiib kii raahen ham kyuun na aaj itaraaen \traahon se hat gae kaante to phuul kyuun na muskaaen mu \taankhon men rang threedots  \tmukhade pe subah kii dhuup ye khilataakhilataa ruup \tkaajal lakiir chitavan ke tiir ye nainaa ruup anuup la \ttum kyaa samajho ye raaz ulfat ke ye andaaz \tsun ke zaruur hogaa guruur aur karane lagoge naaz mu \taisaa kyaal mat kiije ham se ye bhed kah diije \tham bhii to aap hii ke hain hamase yuun sharm naa kiije la \tchamakii nasiib kii raahen threedots mu \taankhon men rang threedots  \ttarasaao na yuun hamadam tumhen naazoadaa kii qasam \tjaldii se bol do ye raaz khol do paradaa uthaa do sanam la \tharagiz na kahuungii ye baat jodoge na jab tak haath \tbanake nasiib rahanaa qariib jyuun taare chaand ke saath mu \ttumase judaa na honge ham badalen hazaar ye aalam \tham tumape jaan de denge gaatii hai saans kii saragam \taankhon men rang threedots ', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'aankhon men rang kyuun aayaa', 'year': '1960'}`
- output: `{"pred": "laxmikantpyarelal", "top3": ["laxmikantpyarelal", "kalyanjianandji", "madan mohan"]}`
- grader `Exact match (pred == gold composer)`: passed=False score=0.00 — pred='laxmikantpyarelal' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=False score=0.00 — ref='shankarjaikishan' in top3=['laxmikantpyarelal', 'kalyanjianandji', 'madan mohan']

### #527 — PASS

- item: `{'lyrics': ' mujhako apane gale lagaa lo ai mere hamaraahii tumako kyaa batalaauun main ki tumase kitanaa pyaar hai mujhako apane gale lagaa lo   jab tum mujhase duur rahate ho jiyaa meraa ghabaraataa hai niind aankhon se ud jaatii hai chaand agan barasaataa hai donon pahaluu jal jaate hain aag men aag lagaataa hai jaise tadape bin jal machhalii pyaar mujhe tadapaataa hai  pyaar mujhe tadapaataa hai is ulajhan se mujhako bachaa lo ai mere hamaraahii tumako kyaa batalaauun main   jin raahon par hansake chalo tum phuul vahaan khil jaate hain dam lene ko jahaan ruko tum madhushaale ban jaate hain tumako chhuukar pavan jhakore khushabuu lekar jaate hain lekin ham to dekhake suurat dil thaame rah jaate hain  dil thaame rah jaate hain dil se dil ke taar milaa lo ai mere hamaraahii tumako kyaa batalaauun main   jab tak tumako main na dekhuun chain mujhe kab aataa hai khoj men terii man kaa panchhii duur kahiin kho jaataa hai jab tum mujhako mil jaatii ho dard davaa ban jaataa hai varanaa tum bin saaraa jiivan suunaa ban kahalaataa hai suunaa ban kahalaataa hai har manzil par mujhako sanbhaalo ai mere hamaraahii tumako kyaa batalaauun main ', 'correct_label': 'shankarjaikishan', 'label': 9, 'split': 'test', 'title': 'mujhako apane gale lagaa lo ai mere hamaraahii', 'year': '1963'}`
- output: `{"pred": "shankarjaikishan", "top3": ["shankarjaikishan", "annu malik", "laxmikantpyarelal"]}`
- grader `Exact match (pred == gold composer)`: passed=True score=1.00 — pred='shankarjaikishan' ref='shankarjaikishan'
- grader `Top-3 contains gold composer`: passed=True score=1.00 — ref='shankarjaikishan' in top3=['shankarjaikishan', 'annu malik', 'laxmikantpyarelal']

## Usage

```json
[{'model_name': 'baseline-full', 'invocation_count': 527, 'prompt_tokens': 75611, 'completion_tokens': 1581, 'total_tokens': 77192, 'cached_tokens': 0}]
```

## Research notes

- Treat this report as a **signal**, not a certificate of safety.
- Calibrate automated graders against human labels before scaling.
- Grow the dataset with production edge cases (logs → eval items).
