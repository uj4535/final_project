-- select feature from animal_list where species='없음'
-- update animal_list set species="코리안숏헤어" where species like "%한국%" or species like "%코숏%" or species like "%쇼콧%" or species like "%길고양이%"
-- 폴드혼종인듯->스코티쉬폴드, 
-- 아비시안종, 아비시니안 -> 아비시니안
-- 코숏, 고등어->코리안숏헤어, 
-- 벵갈고양이,  호피무늬
-- 아메리카숏헤어, 아몌리칸 숏헤어 -> 아메리칸숏헤어, 
-- 터키쉬앙고라, 터키쉬앙골라, 
-- 러시안블루, 러시안 블루, 러시안 불루, 
-- 화이트 페르시안, 페르시안 (고양이) -> 페르시안
-- 샴


-- update animal_list set species='젝러셀테리어' where species like "%테리어";
-- update animal_list set species='진돗개' where species like "%진도%"
-- update animal_list set species='믹스견' where species like "%발바리%"
-- update animal_list set species='리트리버' where species like "%골든%" or species like "%리트리버%" or species like "라브라도"
-- update animal_list set species='재패니즈친' where species like "%제페니즈%" or species like "%재패니즈%"
-- update animal_list set species='올드잉글리쉬쉽독' where species like "%올드%" or species like "%잉글리쉬%"
-- update animal_list set species='터키쉬앙고라' where species like "%앙고라%" or species like "%터키쉬%"
-- update animal_list set species='아메리칸숏헤어' where species like "%아메리칸%" or species like "%미국%"
-- update animal_list set species='스코티쉬폴드' where feature like "%폴드혼종인듯%"
-- update animal_list set species='아비시니안' where feature like "%아비시안%" OR feature like "%아비시니안%"
-- update animal_list set species='코리안숏헤어' where feature like "%코숏%" OR feature like "%고등어%"
-- update animal_list set species='뱅갈고양이' where feature like "%뱅갈%" OR feature like "%벵갈%"or feature like "호피무늬"
-- update animal_list set species='터키쉬앙고라' where feature like "%터키쉬%" OR feature like "%앙골라%"
-- update animal_list set species='러시안블루' where feature like "%러시안%" 
-- update animal_list set species='페르시안' where feature like "%페르시안%" 
-- update animal_list set species='샴' where feature like "%샴%" 
-- update animal_list set species='시베리아허스키' where species like "%시베리안%" or species like "%허스키%"
-- update animal_list set species='러시안블루' where species like "%러시안%"
-- update animal_list set species='보더콜리' where species like "%콜리%"
-- update animal_list set species='푸들' where species like "%토이%"
-- update animal_list set species='진돗개' where species like "%백구%"
-- update animal_list set species='코리안숏헤어' where species like "%반고등어%"
-- update animal_list set species='푸들' where species like "%스탠다드%"
-- update animal_list set species='하운드' where species like "%그레이트%" or species like "%아이리쉬%" or species like "%아일랜드%" or species like "%하운드%"
-- update animal_list set species='하운드' where species like "%아프간%"
-- update animal_list set species='스코티시폴드' where species like "%스코티쉬%"
-- update animal_list set species='터키쉬앙고라' where feature like "%터앙%"
-- update animal_list set species='믹스묘' where animal='고양이' and species like "%없음%" 
-- update animal_list set species='믹스견' where animal='개' and species like "%없음%"

-- update animal_list set species='믹스묘' where animal='고양이' and species like "%기타%" 
-- update animal_list set species='믹스견' where animal='개' and species like "%기타%" 
-- update animal_list set species='사냥개' where species like "%바센지%" or species like "%롯트와일러%" or species like "%케인%" or species like "%도베르만%" or species like "%셰퍼드%" or species like "%포인%"
-- update animal_list set species='스파니엘' where species like "%스파니엘%" 
-- update animal_list set species='코카스파니엘' where species like "%스파니엘%" or species like "%코카%"
-- update animal_list set species='하운드' where species like "%이탈리안%"
-- update animal_list set species='프렌치불독' where species like "%프렌치%" or species like "%불독%"
-- update animal_list set species='쉽독' where species like "%쉽독%" or species like "%셔틀랜드%"
-- update animal_list set species='스피츠' where species like "%미텔%"

-- select animal, feature from animal_list where species='없음'

select count(*), species from animal_list group by species order by count(*) DESC;

