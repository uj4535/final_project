from django.test import TestCase
import os
# Create your tests here.

os.getcwd()

    age=request.GET['age']
    weight=request.GET['weight']
    animal=request.GET['animal'] # 기본 개=1, 고양이=0
    color=request.GET['color']
    species_dash=request.GET['species_dash']
    species_dalma=request.GET['species_dalma']
    species_dosa=request.GET['species_dosa']
    species_laika=request.GET['species_laika']
    species_russian=request.GET['species_russian']
    species_retriever=request.GET['species_retriever']
    species_mali=request.GET['species_mali'] 
    species_malla=request.GET['species_malla']
    species_maltiz=request.GET['species_maltiz']
    species_miniature=request.GET['species_miniature']
    species_minipin=request.GET['species_minipin']
    species_mixdog=request.GET['species_mixdog']
    species_mixcat=request.GET['species_mixcat']
    species_bengalcat=request.GET['species_bengalcat']
    species_bedling=request.GET['species_bedling']
    species_boder=request.GET['species_border']
    species_boston=request.GET['species_boston']
    species_britany=request.GET['species_britany']
    species_british=request.GET['species_british']
    species_biggle=request.GET['species_biggle']
    species_bichon=request.GET['species_bichon']
    species_bbabbi=request.GET['species_bbabbi']
    species_hunter=request.GET['species_hunter']
    species_samo=request.GET['species_samo']
    species_sapsal=request.GET['species_sapsal']
    species_shapei=request.GET['species_shapei']
    species_sham=request.GET['species_sham']
    species_shipdog=request.GET['species_shipdog']
    species_shuna=request.GET['species_shuna']
    species_scotish=request.GET['species_scotish']
    species_spiz=request.GET['species_spiz']
    species_shiba=request.GET['species_shiba']
    species_husky=request.GET['species_husky']
    species_chu=request.GET['species_chu']
    species_americat=request.GET['species_americat']
    species_abasiniancat=request.GET['species_abasiniancat']
    species_akida=request.GET['species_akida']
    species_allaskan=request.GET['species_allaskan']
    species_yoki=request.GET['species_yoki']
    species_welsh=request.GET['species_welsh']
    species_japan=request.GET['species_japan']
    species_german=request.GET['species_german']
    species_jack=request.GET['species_jack']
    species_jindo=request.GET['species_jindo']
    species_chawoo=request.GET['species_chawoo']
    species_chiwawa=request.GET['species_chiwawa']
    species_koreancat=request.GET['species_koreancat']
    species_coca=request.GET['species_coca']
    species_turkish=request.GET['species_turkish']
    species_purg=request.GET['species_purg']
    species_persian=request.GET['species_persian']
    species_penekiz=request.GET['species_penekiz']
    species_pome=request.GET['species_pome']
    species_pompiz=request.GET['species_pompiz']
    species_puddle=request.GET['species_puddle']
    species_poongsan=request.GET['species_poongsan']
    species_frenchbuldog=request.GET['species_frenchbuldog']
    species_hound=request.GET['species_hound']
    neuteryn_n=request.GET['neuteryn_n']
    neuteryn_y=request.GET['neuteryn_y']   #y,u-> n일때 0,0
    outer_health_a=request.GET['outer_health_a'] 
    outer_health_s=request.GET['outer_health_s']
    inner_health_a=request.GET['inner_health_a']
    inner_health_s=request.GET['inner_health_s']
    disable=request.GET['disable']
    personality_f=request.GET['personality']
    personality_u=request.GET['personality']
    care=request.GET['care']
    sex_f=request.GET['sex']
    sex_m=request.GET['sex']


    	나이(만): <p> <input type="text" name="age" > </p> 
	무게(kg): <p><input type="text" name="weight"> </p>
	동물(개/고양이): <p> 개<input type="radio" name="animal" value=1>
					고양이 <input type="radio" name="animal" value=0> </p>
	색: <p> 검은색 <input type="radio" name="color" value=0>
			혼합 <input type="radio" name="color" value=1>
			흰색 <input type="radio" name="color" value=2>
			갈색 <input type="radio" name="color" value=3> 
	 </p> 

	종(species):<p> <select name=option name>
						<option name="species_dash" value=1> 닥스훈트 </option> 
						<option name="species_dalma" value=2> 달마시안  </option>
						<option name="species_dosa" value=3> 도사견  </option> 
						<option name='species_laika' value=4> 라이카  </option>
						<option name='species_russian' value=5> 러시안블루  </option> 
						<option name='species_retriever' value=6> 리트리버  </option> 
						<option name='species_mali' value=7> 마리노이즈 </option> 
						<option name='species_malla' value=8> 말라뮤트  </option> 
						<option name='species_maltiz' value=9> 말티즈  </option> 
						<option name='species_miniature'value=10> 미니어쳐  </option> 
						<option name='species_minipin' value=11> 미니핀  </option> 
						<option name='species_mixdog' value=12> 믹스견 </option> 
						<option name='species_mixcat' value=13> 믹스묘 </option> 
						<option name='species_bengalcat' value=14> 뱅갈고양이 </option> 
						<option name='species_bedling' value=15> 베들링턴</option> 
						<option name='species_boder' value=16> 보더콜리 </option> 
						<option name='species_boston' value=17> 보스턴 </option> 
						<option name='species_britany' value=18> 브리타니 </option> 
						<option name='species_british' value=19> 브리티시 </option> 
						<option name='species_biggle' value=20> 비글 </option> 
						<option name='species_bichon' value=21> 비숑 </option> 
						<option name='species_bbabbi' value=22> 빠삐용 </option> 
						<option name='species_hunter' value=23> 사냥개 </option> 
						<option name='species_samo' value=24> 사모예드 </option> 
						<option name='species_sapsal' value=25> 삽살개 </option> 
						<option name='species_shapei' value=26> 샤페이 </option> 
						<option name='species_sham' value=27> 샴 </option> 
						<option name='species_shipdog' value=28> 쉽독 </option> 
						<option name='species_shuna' value=29> 슈나우져 </option> 
						<option name='species_scotish' value=30> 스코티시폴드</option> 
						<option name='species_spiz'value=31> 스피츠 </option> 
						<option name='species_shiba' value=32> 시바 </option> 
						<option name='species_husky' value=33> 시베리아허스키 </option> 
						<option name='species_chu' value=34> 시츄 </option> 
						<option name='species_americat' value=35> 아메리칸숏헤어 </option> 
						<option name='species_abasininacat' value=36> 아비시니안 </option> 
						<option name='species_yoki' value=37> 요크셔 </option> 
						<option name='species_welsh' value=38> 웰시 </option> 
						<option name='species_japan' value=39> 재패니즈친 </option> 
						<option name='species_german' value=40> 저먼 </option> 
						<option name='species_jack' value=41> 젝러셀테리어 </option> 
						<option name='species_jindo' value=42> 진돗개 </option> 
						<option name='species_chawoo' value=43> 차우차우</option> 
						<option name='species_chiwawa' value=44> 치와와 </option> 
						<option name='species_koreancat' value=45> 코리안숏헤어 </option>
						<option name='species_coca' value=46> 코카스파니엘 </option> 
						<option name='species_turkish' value=47> 터키쉬앙고라 </option> 
						<option name='species_purg' value=48> 퍼그 </option> 
						<option name='species_persian' value=49> 페르시안 </option> 
						<option name='species_penekiz' value=50> 페니키즈 </option> 
						<option name='species_pome' value=51> 포메라니안 </option> 
						<option name='species_pompiz' value=52> 폼피츠 </option> 
						<option name='species_puddle' value=53> 푸들 </option> 
						<option name='species_poongsan' value=54> 풍산개 </option> 
						<option name='species_frenchbuldog' value=55> 프렌치불독 </option> 
						<option name='species_hound' value=56> 하운드 </option> 
				</select>
			
	</p>
	
	중성화 여부:<p> Yes <input type="radio" name="neuteryn" value=2>
				unknown <input type="radio" name='neuteryn' value=1>
				 No <input type="radio" name="neuteryn" value=0>
				 
	</p>

	outer health(부상): <p> 심각<input type="radio" name="outer_health" value=2>
							치료 가능<input type="radio" name="outer_health" value=1>
							해당없음 <input type="radio" name="outer_health" value=0>
	</p>

	inner health(질병): <p> 심각<input type="radio" name="inner_health" value=2>
							치료 가능<input type="radio" name="inner_health" value=1>
							해당없음 <input type="radio" name="inner_health" value=0>
	</p>
	장애여부: <p> 있음<input type="radio" name="disable" value=1>
				없음 <input type="radio" name="disable" value=0> 
			</p>
				
	
	생후 3개월 이내: <p>온순<input type="radio" name="personality" value=2>
				사나움<input type="radio" name="personality" value=1>
				알수없음 <input type="radio" name="personality" value=0>
			</p>
	성별: <p> 여자<input type='radio' name='sex' value=1>
			남성<input type='radio' name='sex' values=0> </p>