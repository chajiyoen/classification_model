menu_sets=[]
//메뉴 생성기 시작 S =================================
class Menu {
    constructor(mtitle){
        this.mtitle=mtitle;
    }
    mtitle;
    url; tips;
}
menu1= new Menu("CNN AND Crawling");
menu1.url="https://github.com/chajiyoen/classification_model/"
menu1.tips="네이버, 구글 이미지 크롤링 및 컨볼루션 적용한 모델";
menu2 = new Menu("RNN AND LSTM encryto meney")
menu2.url="https://chajiyoen.github.io/RNN_crytoanal/"
menu2.tips= "가상화페 분석을 이용한 미래 가격 측정"
menu_sets.push(menu1)
menu_sets.push(menu2)
