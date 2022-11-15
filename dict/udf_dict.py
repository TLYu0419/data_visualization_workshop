udf_dict = {
    '學校': [
        '臺中教育', '臺北藝術', '交通', '台灣', '清華', '慈濟', '空中', '東華', '美崙校區', '台灣觀光', '輔大', '輔仁大學', '臺灣觀光',
        '臺觀', '第一學府', '輔仁', '東華', '台科', '高中', '世新', '彰化師範', '彰師', '東海', '大學', '學院', '國中', '私立', '國立',
        '平和', '台大', '中學', '小學', '幼稚園',
    ],

    '學院/科系': [
        '人文社會科學院', '人社院', '人社', '人院', '理工學院', '理工', '理院', '管理學院', '管院', '花師教育學院', '花師', 
        '藝術學院', '原住民民族學院', '原民', '原院', '環境暨海洋', '環院', '洄瀾學院', '師資培育中心', '師培中心',
        
        '諮商與臨床心理學系', '諮臨系', '諮臨所', '諮臨', '中國語文學系', '中文系', '中文所', '中文', 
        '臺灣文化學系', '臺文系', '臺文所', '臺文', '台灣文化學系', '台文系', '台文所', '台文',
        '經濟學系', '經濟系', '經濟所', '經濟', '公共行政學系', '公行系', '公行所', '公行', 
        '華文文學系', '華文系', '華文所', '華文', '英美語文學系', '英美系', '英美所', '英美',
        '歷史學系', '歷史系', '歷史所', '歷史', '社會學系', '社會系', '社會所', '社會', 
        '法律學系', '法律系', '法律所', '法律', 
        
        '應用數學系', '應數系', '應數所', '應數', '生命科學系', '生科系', '生科所', '生科', 
        '光電工程學系', '光電系', '光電所', '光電',  '材料科學與工程學系', '材料系', '材料所', '材料',
        '物理學系', '物理系', '物理所', '物理', '化學系', '化學所','化學', 
        '電機工程學系', '電機系', '電機所', '電機', '資訊工程學系', '資工系', '資工所', '資工', 
        
        '企業管理學系', '企管系', '企管所', '企管', '國際企業學系', '國企系', '國企所', '國企', 
        '資訊管理學系', '資訊系', '資訊所', '資管', '觀光暨休閒遊憩學系', '觀遊系', '觀遊所', '觀遊',
        '會計學系', '會計系', '會計所', '會計', '財務金融學系', '財金系', '財金所', '財金', '運籌管理研究所','運籌所','運籌',
        '管理科學與財金國際學系', '管科系', '管科所', '管科', '高階經營管理研究所', '經營所', '經營',
        
        '教育與潛能開發學系', '教育系', '教育所','教育', '課程設計與潛能開發學系', '課程系', '課程所','課程', 
        '特殊教育學系', '特教系', '特教所', '特教', '教育行政與管理學系', '教行系', '教行所','教行', 
        '體育與運動科學系', '體育系', '體育所', '體育', '體系', '幼兒教育學系', '幼教系', '幼教所','幼教',
        
        '音樂學系', '音樂系', '音樂所', '音樂', '藝術創意產業學系', '藝創系', '藝創所', '藝創', '藝術與設計學系', '藝設系', '藝設所', '藝設', 
        
        '族群關係與文化學系', '族文系', '族文所', '族文', '民族事務與發展學系', '民發系', '民發所','民發', 
        '民族語言與傳播學系', '民傳系', '民傳所', '民傳', '民族社會工作學系', '民社系', '民社所','民社', 
        '原住民族樂舞與藝術學系', '民樂系', '民樂所', '民樂',
        
        '自然資源與環境學系', '自資系', '自資所', '自資', '海洋生物研究所', '海洋所', '海洋', '人文與環境研究所', '人環所', '人環',
        
        '通識教育中心', '藝術中心', '體育中心', '語言中心', '華語文中心', '縱谷跨域書院學士學位學程',    
        
        '諮商與應用心理學系', '人類發展與心理學系', '電影創作學系', '電影學系', '醫學檢驗暨生物技術', '人類發展心理', '醫學資訊學系', 
        '科系', '學系', '研究所', '學士', '碩士', '博士', '法研所', '系級',
    ],

    '行政單位': [
        '校長室', '副校長室', '教務處', '學生事務處', '學務處', '總務處', '研發處', '國際處', '秘書室', '人事室', '主計室', '圖書資訊處',
        '教學卓越中心', '心理諮商輔導中心', '校級委員會', '國際組', '英語培力研究院籌備處', '行政中心', '育成中心', '東華農場', '戲水池', 
        '運動場', '器材室', 
    ],

    '委員會': [
        '學術獎助評審', '獎審會', '審查單位', '教評會', '三級三審', '評估小組', '升等', '性別平等教育', '調查小組', '性平會', '委員會', '教育法',
        '校園', '性侵害', '性騷擾', '性霸凌', '理事會',
    ],

    '教職員工生': [
        '校長', '副校長', '副教授', '教授', '助理教授', '講座教授', '專任', '兼任', '研究助理', '行政助理', '校長', '主任秘書',
        '東華校警', '系主任', '師生', '教職員生', '教師', '校園大使', '院長', '碩士班', '學士班', '博士班', '應屆畢業生',
        '大一', '大二', '大三', '大四', '大五', '大六', '一年級', '二年級', '三年級', '四年級', '五年級', '六年級', '延畢',
        '大學', '大專', '東華人', '學年度', '學長姐', '學長', '學弟', '學姐', '學妹', '本地', '外地', '僑生', '原民生',
        '在職專班', '一年', '二年', '三年', '四年', '菸酒生', '碩一', '碩二', '碩三', '碩四', '大學', '碩士', '博士', '在職',
        '長期', '短期', '學生', '同學', '學姊', '先生', '小姐', '陸生', '港生', '管理員', '國中生', '學生宿舍', '學測', '指考',
        '畢業', '市民', '專題', '學生會', '系學會', '期初', '期中', '期末', '澳門人', '台灣人', '大陸人', '中國人', '老屁股',
        '外招生', '技術員', '歪果仁', '會長', '隊長', '校警', '大學生', '臨時工', '有錢人', '網軍', '生理男', '生理女', '總編輯', 
        '創辦人', '副會長', '副隊長', '女店員', '男店員', '使用者', '申請人', '申請表', '使用人', '本地生', '宅男', '宅女', '趙校長',
        '吳校長', '黃人', '白人', '黑人', '日本人', '臺灣人', '中國人', '政治', '後現代主義', '州長',
        '系上', '甲一', '甲二', '系辦', '數學', '延畢生', '工讀生', '班上', '同學',
    ],

    '研究/獎勵': [
        '頂尖', '人才', '獎勵', '獎助', '溢領', '溢領', '研究計劃', '學術', '研究', '頂尖', '獎勵', '校務基金', '問卷', '青年築夢',
        '計畫', '實驗室', '人事', '主題', '對象', '工讀', '線上', '重複', '領取', '東都印記', '五百億', '論文', '受訪者', '作業',
        '定義', '範疇', '年會', '梯田計畫', '獎助金', '點數', '獎勵金', '人事案', 
    ],

    '政府部門/企業': [
        '教師會', '監察院', '林管處', '全教總', '公懲會', '臺灣青年民主', '協會', '國立故宮博物院', '台積電', '遠雄', '悅來',
        '玉軒西點烘培坊', '黎明向陽園', '行銷部', '高等', '地方', '最高', '行政', '法院', '國民政府', '環保局', '台銀', '台灣銀行',
        '露易沙', '種花電信', '志學書店', '遠百', '饈甲', '木槿軒', '卜蜂', '龍城', '樂和', '摩奇', '華泰', '馬里漾', '貝爾', 
        '機車行', '啵比', '動物園', '綿花甜', '萬家鄉', '吖漾', '蘋果日報', '新聞網', '新悅旅棧', '陳媽媽', '呼朋引伴', '大呼過癮',
        '竹緹', '蓮園', '行政體系', '社會局', '公開信', '移民禁令', '聯合國', 
    ],

    '地區': [
        '宜蘭', '花蓮', '台北', '新北', '桃園', '新竹', '苗栗', '台中', '彰化', '南投', '雲林', '台南', '高雄', '屏東', '台東', '壽豐',
        '河內', '外縣市', '馬來西亞', '臺北', '雙北', '臺中', '臺南', '後山', '鯉魚山', '台九線', '東海岸', '茶水間', '鳳林', '後花園',
        '新左營', '七星潭', '紐西蘭', '法國', '巴黎', '在地', '本土',
    ],

    '社團': [
        '英語文化', '雅頌箏樂', '古箏', '跆拳道', '魔術', '攝影', '社辦', '學生會', '系學會', '嗷嗚', '嗷嗚福利', '遊戲王', '研究社',
        '動畫漫畫', '德州撲克', '手鼓社', '非洲鼓', '德撲', '脊椎動物', '牌咖', '麻將', '文學創作社', '彈珠', '怪物彈珠', '狗媽媽',
        '樂舞文化', '金屬樂', '浪浪', '檢討會', '電子音樂', '愛狗', '同鄉會', '阿瓦隆', '心理戰', '儒學生活', '同好會', '汪汪社',
    ],

    '大樓/宿舍': [
        '人社', '人一', '人二', '人三', '外環', '行雲', '向晴', '湖畔', '沁月', '體育中心', '學活', '仰山', '理一', '理二', '行政', '涵星',
        '內環', '花師', '全家', '原民', '集賢', '多容', '圖書館', '東華會館', '學生活動', '中心', '迎曦', '籃球場', '停車場', '討論室',
        '教室', '校門口', '理工', '理一', '理二', '理三', '第一', '講堂', '第二', '第三', '行雲', '沁一', '沁二', '涵一', '涵二', '房間',
        '一館', '二館', '三館', '一莊', '二莊', '男宿', '女宿', '宿舍', '雅房', '套房', '第一床', '第二床', '第三床', '第四床',
        '村上村宿', '詰雲', '計算機', '夜間自習室', '快速列印區','討論區', '教學區', '籃網', '不鏽鋼', '校門', '校門口', '系辦', '院辦',
        '瓊林', '學生活動中心',
    ],

    '課程': [
        '服務學習', '社會研究法', '技術與社會',  '教學意見表', '院基礎', '校核心', '系核心', '社會科學研究法', '高等微積分',
        '廣告與消費者心理', '觀光休憩調查方法', '醫藥與健康', '動物福利學', '廣告與消費者心理', '政治學', '傳播與科技',
        '期中考', '期末考', '期末報告', '電影拍攝', '文創學程', '服務時數', '程式設計', '必修', '選修', '社會學', '認知與學習',
        '夢境經驗', '化學世界', '性別與法律', '體育課', '語言學', '法式滾球', '游泳', '國際關係', '影視史學', '心理學',
        '電影與宗教', '幼兒世界', '現代科技前瞻', '德語課', '文學經典', '跨領域', '文學神話', '爽課', '衍生性', '地圖學', 
        '文學史', '文法課', '世界文學', '系統分析與設計', '經濟學', '哲學', '意見調查表', '搶課', '必修', '選修', '上修',  
        '當掉', '選課', '通識課', '游泳課', '微課程', '微學程', '設計思考', '企劃寫作', '圖像表達', '社會實踐', '老人學',
        '醫學', '總名額', '總人數', '通識課', '交卷', '上傳成績', '鬆餅', 
    ],

    '志學街': [
        '志學', '麻油雞', '麵線', '志光街', '酥炸', '雞胸', '雞腿排', '烤雞', '弘爺漢堡', '皇家貴族派', '雞腿', '雞排', '大阪燒餐車',
        '肉粽伯', '蘭州拉麵', '娃娃機', '鹹水雞', '志安宮', '東芝鄉', '炒飯', '羹飯', '法國麵包', '玉米濃湯', '海苔酥', '回鍋肉',
        '洋蔥', '鬆餅', '巧克力塔', '布朗尼', '越南餐廳', '不錯', '菜單', '咖啡館', '紅茶', '紅茶洋行', '東華店', '貞媽深夜麵館',
        '中正路', '店員', '品牌', '小魚的家', '員工', '聚餐', '意麵', '加麵', '滷肉飯', '滷味', '百頁', '加點', '無骨雞腿排',
        '派克雞排', '志學', '派出所', '庭庭炸雞', '滷媽媽', '亞糜廚房', '外帶杯', '難吃', '東華藥局', '歐哈尼', '服務生', '電線桿',
        '百頁豆腐', '服務業', '貝納頌', '小黃瓜', '番茄醬', '少爺丼飯', '盛夏果實', '雙子座', '花蓮香', '微波食品', '百香愛玉', '半糖', '去冰', '東山鴨', '葡萄皮',
        '重新', '出發', '結束', '經營', '開張', '班表', '彼得兔', '捲心酥', '麻辣火鍋', '韓式料理','養雞場', '臭酸', '烏龍麵', '鹹豬肉', '卡拉雞',
        '滷蛋', '豬血糕', '關東煮', '綠豆沙', '丸山', '小灶坊', '牛肉麵', '麵條', '中正路', '鍋燒麵', '羊肉爐', '迷客夏', '客製化', '傳送', '加達車業',
        '買飲料', '買回來', '鍋燒意麵', '油蔥酥', '柴魚', '蛋餃', '甜不辣', '湖畔王', '三顧茅廬', '穆府牛肉麵', '路邊攤', '香噴噴', '飯菜', '很香', '好貴',
        '漲到', '即期品', '軟掉', '志新街', '雞蛋', '樓梯間', '蒜泥白肉', '賣完了', '梅花肉', '茄子', '煮飯', '有螞蟻', '出問題', '聯想', '沾醬雞排', '蛋炒飯',
        '米蟲', '簡餐店', '虧我', '好正', '卡拉雞塊', '咖哩飯', '踩地雷', '東華一隻貓', '蛋包飯', '葉子廚房', '餐車', '泰式奶茶', '香蕉煎餅', '腸子', '讚嘆',
        '咖啡農', '冷凍庫', '幫我', '調閱監視器', '聞起來', '咖喱醬', '饈呷', '吃吃看', '好欺負', '烤百頁', '法式吐司', '炸豬排', '皮蛋瘦肉粥', '雞蛋糕', '買買看',
        '章魚燒', '烤肉飯',
        
        
    ],

    '星期': [
        '週一', '週二', '週三', '週四', '週五', '週六', '周日',
        '一星期',
        '星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日', '星期天',
        '禮拜一', '禮拜二', '禮拜三', '禮拜四', '禮拜五', '禮拜六', '禮拜日', '禮拜天',
        '一點', '二點', '三點', '四點', '五點', '六點', '七點', '八點', '九點', '十點', '十一點', '十二點',
        '上午', '中午', '下午', '晚上', '凌晨', '傍晚', '那一刻',
        '半個', '四點半', '六點半', '有一天', '每個', '好幾天', '農曆', '十點半', '分鐘', '這年頭',
        '前期', '中期', '後期', '提前', '學期初', '學期中', '學期末',
        '半個月', '一個月', '兩個月', '二個月', '三個月', '四個月', '五個月', '六個月', '七個月', '八個月', '九個月', '十個月',
        '大前天', '前天', '昨天', '今天', '今日', '明天', '後天', '大後天', '短時間',
    ],

    '成語': [
        '到此為止', '轉移焦點', '佳節愉快', '濫用職權', '無稽之談', '利益輸送', '討價還價', '接二連三', '不實指控', '學術自主', '五四運動',
        '校園霸凌', '社會觀感', '工程舞弊', '虛擬實境', '盡忠職守', '雙重標準', '學術自由', '養家餬口', '親友亡故', '無的放矢', '毫無根據',
        '調查報告', '個人名譽', '長話短說', '風雨無阻', '聖誕快樂', '子虛烏有', '一國兩制', '資本主義', '積極主動', '誠摯邀請', '無怨無仇',
        '代為保管', '授課時數', '無病呻吟', '違法失職', '多多包涵', '正當程序', '坐領高薪', '實事求是', '愛校服務', '無限上綱', '毀於一旦',
        '自行補充', '職業操守', '意見調查', '回饋表單', '立意良好', '難分難捨', '一再強調', '敬謝不敏', '不祥預兆', '安然無恙', '原裝進口',
        '安全距離', '連署表單', '成雙成對', '睡眠障礙', '姑息養奸', '莫名奇妙', '網路釣魚', '妨害名譽', '交通規則', '隨身物品', '自以為是',
        '品牌經營', '青年創業', '理想生活', '運動場所', '一直以來', '耐心等待', '神秘人士', '走投無路', '個人經歷', '開開心心', '活動地點',
        '泱泱大國', '校外人士', '文化資產', '意義何在', '心跳加速', '民意調查', '新年快樂', '顛倒是非', '特殊才能', '日出月落', '天地恆久',
        '侵門踏戶', '蠱惑人心', '所做所為', '一修再修', '性別平等', '毛手毛腳', '逍遙法外', '高談闊論', '不知羞恥', '良心發現', '擋人財路',
        '一年半載', '以身試法', '歷歷在目', '好自為之', '丟人現眼', '有模有樣', '自甘墮落', '胡作非為', '變本加厲', '天長地久', '危害眾生',
        '真有其事', '種族歧視', '道聽途說', '短視近利', '水性楊花', '轟轟烈烈', '忍氣吞聲', '基本權利', '貪小便宜', '母胎單身', '大放厥詞',
        '共體時艱', '夏夕夏景', '螳臂擋車', '不削一顧', '休養生息', '心甘情願', '純屬巧合', '人身攻擊', '天長地久', '無縫接軌', '偷來暗去',
        '無理取鬧', '相親相愛', '乾我屁事', '不偷不搶', '嗚呼哀哉', '憤世嫉俗', '社會參與', '義務教育', '終身學習', '舉一反三', '以和為貴',
        '膽大包天', '不是不報', '時候未到', '娓娓到來', '四維八德', '士農工商', '吃喝嫖賭', '射後不理', '好手好腳', '隨袋徵收', '慢走不送',
        '一面之緣', '互相傷害', '新仇舊恨', '來龍去脈', '將心比心', '行有餘力', '打情罵俏', '大驚小怪', '死不認帳', '恬不知恥', '有所長進',
        '鑽牛角尖', '戰戰兢兢', '隨機殺人', '關你屁事', '关我屁事', '不離不棄', '無時無刻', '更待何時', '前情提要', '深感遺憾', '火力全開',
        '佔地為王', '黑白兩道', '硬著頭皮', '不成問題', '從頭到尾', '與眾不同', '一介書生', '一口答應', '人際關係', '唧唧歪歪', '不以為然',
        '全民公投', '不聞不問', '一模一樣', '無中生有', '連名帶姓', '理所當然', '大聲嚷嚷', '虛情假意', '敢作敢當', '憤世忌俗', '滔滔不絕',
        '三天兩頭', '以一敵百', '怒戰群雄', '盡釋前嫌', '雙腿一軟', '強顏歡笑', '不動如山', '自言自語', '技高一籌', '半斤八兩', '稀裡嘩啦',
        '上吐下洩', '未看先猜', '月夜朦朧', '雲霧繚繞', '人滿為患', '沉魚落雁', '半夢半醒', '同文同種', '同祖同源', '中元普渡', '四方恭迎', 
        '少見多怪', '孤陋寡聞', '有待加強', '吃飽太閒', '荒腔走板', '繁文縟節', '從重量刑', '不得不說', '一一列出', '狗屁倒灶', '鐵口直斷', 
        '良心建議', '吵吵鬧鬧', '任意妄為', '無能為力', '禁止飲食', '無所不在', '面無表情', '總而言之', '嬉皮笑臉', '黑人問號', '與世隔絕', 
        '有說有笑', '西西簌簌', '頭腦簡單', '四肢發達', '理直氣壯', '嘰嘰喳喳', '壯大聲勢', '化外之地', '如膠似漆', '蟲鳴鳥叫', '欺善怕惡',
        '義憤填膺', '平白無故', '三經半夜', '物以類聚', '比手畫腳', '吾皇萬歲', '有錯在先', '偷換概念', '廢話連篇', '弊端叢生', '各說各的',
        '感激不盡', '七夜怪譚', '強勢回歸', '洪荒之力', '保護措施', '你儂我儂', '見識短淺', '現身說法', '入鄉隨俗', '另有規劃', '下面留言',
        '身體健康', '送完為止', '各位同學', '社會參與', '世界和平', '沒有解決', '怪東怪西', '送完為止', '賣完為止', '舊雨新知', '四處碰壁',
        '搖擺不定', '創造卓越', '不必多言', '政治正確', '巴黎和會', '種族平等', '由來久矣', '一帶一路', '保守主義', '民粹主義', '國際組織',
        '南北戰爭', '氣候協定', '中程導彈', '孤立主義', '保護主義', '一世英明', '衝鋒陷陣', '多元文化', '一閃而過', '團隊合作', '自主學習',
        '性別友善', '無殼蝸牛', '左搖右晃', '非講不可', '地廣物博', '單一校區', '繞來繞去', '只出不進', '眾所期待', '品質保證', '以此類推',
        '越堆越多', '越來越多', '越來越少', '從早到晚', '茶的專家', '三不五時', '細嚼慢嚥', '放你一馬', '想盡辦法', '鍋碗瓢盆', '不塑之客',
        '閒來無事', '名符其實', '基本素養', '野人獻曝', '高矮胖瘦', '親朋好友', '轉型正義', '遊手好閒',
    ], 

    '新聞電視': [
        '中視新聞', '中視', '進擊的巨人', '電視台', '新聞稿', '中共', '派大星', '你的名字', '二刷', '俠盜列車', '惡魔獵人', '霸氣',
        '知情人士', '海賊團', '大媽', '山治', '白鬍子', '黑鬍子', '魯夫', '娜美', '索隆', '喬巴', '灌籃高手', '玩命光頭',  '頭文字', 
        '紫羅蘭', '麵包超人', '肥皂劇', '目擊者',
    ],

    '人名': [
        '莊瑋倫', '徐常恩', '陳柔安', '何宣蓉', '李明霓', '王姓', '林姓', '董智森', '黃智賢', '蔡姓', '陳昕', '陳明暉', '王絨毫', '廖守恩',
        '侑恩', '吳佳潓', '志祥', '晨翔', '波多野結衣', '劉瑩三', '尹盛', '東華阿滴', '阿扣哥', '吃屎哥', '北極熊', '富二代', '館長',
        '許楉亞', '雷歐', '祐賢', '祐希', '竹鼠', '染髮妹', '心機婊', '習近平', '小孬孬', '魔術師', '祥偉', '蔡明樺', '羅雪柔', '涵捷', 
        '趙涵捷', '傅崐萁', '陳時中', '拓也', '希拉蕊', '民主黨', '川普', '共和黨', '麥克阿瑟', '國民黨', '民進黨', '民眾黨', '親民黨', 
        '世代力量', '陳惠萍', '陳其南', '王崧興', '崔媽媽', '李靖詠', '陳星翰',
    ],

    '正負向詞': [
        '不喝', '不喝',
        '看好', '不看好', '通過', '不通過', '履行', '未履行', '意義', '無意義', '辦法', '沒辦法', '尊重', '不尊重', '合理', '不合理',
        '妨礙', '不妨礙', '忘記', '別忘記', '一定', '不一定', '方便', '不方便', '禮貌', '不禮貌', '可能', '不可能', '適應', '不適應',
        '一樣', '不一樣', '記得', '不記得', '好嗎', '不好嗎', '見過', '沒見過', '符合', '不符合', '能說', '不能說', '捨得', '不捨得',
        '完成', '未完成', '交到', '交不到', '同意', '不同意', '調查', '未調查', '遺忘', '不遺忘', '希望', '不希望', '刪掉', '未刪掉',
        '吃文', '不吃文', '直屬', '非直屬', '專心', '不專心', '送中', '反送中', '問題', '沒問題', '公開', '不公開', '可愛', '不可愛',
        '無聊', '不無聊', '分類', '不分類', '準時', '不準時', '單純', '不單純', '對勁', '不對勁', '刪除', '未刪除', '熟悉', '不熟悉',
        '適用', '不適用', '負責', '不負責', '發生', '未發生', '作為', '不作為', '採取', '未採取', '進化', '沒進化', '繳清', '未繳清',
        '聽到', '沒聽到', '信心', '沒信心', '良心', '沒良心', '看到', '沒看到', '覺得', '不覺得', '喜歡', '不喜歡', '值得', '不值得',
        '健康', '不健康', '辦事', '不辦事', '包含', '不包含', '處理', '冷處理', '打掃', '不打掃', '準備', '沒準備', '長大', '沒長大',
        '知道', '不知道', '應該', '不應該', '告知', '未告知', '會有', '不會有', '認識', '不認識', '反對', '不反對', '公告', '未公告',
        '分類', '沒分類', '討厭', '不討厭', '黑特', '非黑特', '發現', '沒發現', '知名', '不知名', '友善', '假友善', '承認', '不承認',
        '好聽', '不好聽', '公平', '不公平', '開心', '不開心', '問題', '沒問題', '爭取', '不爭取', '難吃', '不難吃', '難喝', '不難喝',
        '難聽', '不難聽', '難看', '不難看', '能力', '沒能力', '優勢', '沒優勢', '注意', '沒注意', '相信', '不相信', '喜歡', '不喜歡',
        '規則', '潛規則', '能夠', '不能夠', '長眼', '不長眼', '識相', '不識相', '成熟', '不成熟', '可以', '不可以', '記住', '記不住',
        '貼心', '不貼心', '重要', '不重要', '懂得', '不懂得', '認識', '不認識', '屬於', '不屬於', '拿到', '拿不到', '努力', '不努力',
        '容易', '不容易', '開燈', '不開燈', '做事', '不做事', '效率', '沒效率', '遇到', '沒遇到', '衛生', '不衛生', '涉及', '不涉及',
        '認為', '不認為', '討喜', '不討喜', '進過', '沒進過', '捨得', '捨不得', '出去', '不出去', '印象', '沒印象', '聽過', '沒聽過',
        '吃藥', '不吃藥', '認帳', '不認帳', '落地', '不落地', '帶腦', '不帶腦', '還錢', '不還錢', '搶到', '搶不到', '悔意', '無悔意', 
        '相残', '勿相残', '吃過', '沒吃過', '看過', '沒看過', '聽過', '沒聽過', '喝過', '沒喝過', '打開', '不打開', '找到', '沒找到', 
        '授權', '未授權', '營業', '沒營業', '考慮', '沒考慮', '加薪', '不加薪', '影響', '不影響', '洗手', '不洗手', '提醒', '沒提醒', 
        '清理', '不清理', '好笑', '不好笑', '丟掉', '沒丟掉', '愉快', '不愉快', '正常', '不正常', '想要', '不想要', '聽到', '聽不到', 
        '必要', '沒必要', '睡著', '睡不著', '素質', '沒素質', '聽見', '沒聽見', '自覺', '沒自覺', '禮讓', '不禮讓', '睡覺', '不睡覺',
        '需要', '不需要', '適合', '不適合', '意外', '不意外', '客氣', '不客氣', '禮貌', '沒禮貌', '更換', '不更換', '留下', '不留下',
        '通融', '不通融', '確定', '不確定', '好吃', '不好吃', '會開', '不會開', '道歉', '不道歉', '公開', '不公開', '曉得', '不曉得',
        '接受', '不接受', '扣除', '未扣除', '吃文', '不吃文', '期待', '不期待', '面子', '沒面子', '收到', '沒收到', '保留', '不保留',
        '找到', '沒找到', '了解', '不了解', '安全', '不安全', '認同', '不認同', '經驗', '無經驗', '理會', '不理會', '滿意', '不滿意',
        '重複', '不重複', '干預', '未干預', '成年', '未成年', '結紮', '不結紮', '照做', '不照做', '有錯', '沒有錯', '起來', '不起來',
        '正常', '正常嗎', '注意', '不注意', '有用', '沒有用', '小心', '不小心', '好看', '不好看', '而是', '而不是', '抽煙', '不抽煙',
        '吸煙', '不吸煙', '抽菸', '不抽菸', '吸菸', '不吸菸', '順暢', '不順暢', '想吃', '不想吃', '浪費', '不浪費', '環保', '不環保',
        '看見', '沒看見', '學乖', '學不乖', '檢舉', '被檢舉', '講理', '不講理', '放生', '被放生', '關注', '不關注',
        '負能量', '正能量', '有意義', '沒有意義', '沒意義', '願意', '不願意', '願不願意', '燒', '沒燒', '出來', '不出來', '不要出來',
        '來的及', '來不及',
        '好', '不好', '好不好', '想', '不想', '想不想', '對', '不對', '對不對', '有', '沒有', '有沒有', '是', '不是', '是不是',
        '能', '不能', '能不能', '做', '不做', '做不做', '該', '不該', '該不該', '敢', '不敢', '敢不敢', '會', '不會', '會不會',
        '夠', '不夠', '夠不夠', '屌', '不屌', '屌不屌', '爽', '不爽', '爽不爽',
        '合理', '不合理', '合不合理',
        '對得起', '對不起', '沒注意', '不處理', '沒處理', '不用睡覺',
        '有問題', '沒問題', '沒有問題',
        '有意見', '沒有意見', '在房間', '不在房間', '要不要', '可不可以', '要用', '沒有要用', '長眼睛', '沒長眼睛', '搭便車','禁搭便車',
        '受歡迎', '不受歡迎', '有幫助', '沒有幫助', '好相處', '不好相處', '負責任', '不負責任', '交出來', '交不出來', '公德心', '沒公德心',
        
    ],

    '慣用語': [
        '莫須有', '不貳過',  '白老鼠', '紅玫瑰', '相似度', '單方面', '一份子', '有圖有真相', '順手捐發票', '一發不可收拾', '學長學弟制',
        '三寸不爛之舌', '家醜不可外揚', '惡人先告狀', '我也是醉了', '好人有好報', '垃圾不落地', '躺著也中槍', '兩岸一家親', '中国人不打中国人', 
        '可以嗎', '有事嗎', '還好嗎', '講不停', '講真的', '所以說', '不分青紅皂白', '錢乃身外之物', '你她媽', '你他媽', '卡實在',
        '讓我們繼續看下去', '潮水退了', '提一下', '給我', '好好的', '是怎樣', '我管你', '雖小', '講出去', '聽聽看', '住海邊',
        '自顧自', '有點吵', '動不動', '三小', '林北', '皮皮挫',
    ],

    '顏色/穿著': [
        '藍色', '白色', '黑色', '銀灰色', '綠色', '白色', '黃色', '寶藍色', '土黃色', 
        '飛行', '外套', '髮圈', '條紋', '長褲', '情侶裝', '青蛙裝', '手錶', '鑰匙圈', '花襯衫', '長夾', '牛仔褲', '運動鞋',
        '長袖', '戴眼鏡',
        
    ],

    '活動': [
        '角落藝術節', '古藝市集', '假日學校', '同志大遊行', '萬聖節', '東華盃', '羅馬競技生死鬥', '與你相癒', '聖趴場', '場復',
        '第一屆', '第二屆', '第三屆', '第四屆', '第五屆', '第六屆', '第七屆', '第八屆', '第九屆', '第十屆', '新生盃',
        '本次', '這次', '上次', '前次', '活動', '治療犬', '參加', '人數', '貼心', '提醒', '校際盃', '系際盃', '神秘嘉賓',
        '密室逃脫', '製作團隊', '會計週', '置頂', '宣傳', '系季盃', '爛裁判', '老馬盃', '特賣會', '恐同', '反恐同', '新航之舟', 
        '洄瀾盃', '東京奧運', '運動員', '辯論會', '搶宿舍', '獎盃', '獎牌', '家聚', '拍賣會', '購票', '攝影機', '放音樂',
        '打廣告', '先驅', '伍佰', '照過來', '彩虹旗', '旗桿', '百鬼夜行', '搶破頭', '劇本殺', '夏令營', '療癒', '音樂會',
        '音樂精靈', '魔法學院', '體育周', '校慶盃', '場佈', '奉獻', '新生健檢', '分階段', '響應', '原價',
        '第一', '第二', '第三', '梯次', '系隊', '校隊', '企劃書', '開業', '接近', '唸大學', '拉贊助', '走進來', '手作小物', '試圖',
        '捧場','雙手空空', '回頭', '影印店', '期末大會', '期初大會', '反亞泥', '封路', '懶人包', 
    ],

    '停車/交通': [
        '機車', '黃牛', '外環', '車棚', '運輸工具', '臨停區', '腳踏車', '青年返鄉', '列車', '鑰匙', '騎士', '二輪仔', '訂票', '側柱', '飛翼',
        '踏板', '車速', '過快', '辨識系統', '靈骨塔', '塔位', '移動式', '神主牌', '抓交替', '頭燈', '視線', '滑板車', '車道', '走道', '機車道',
        '夜間停車', '兩段式左轉', '直行車', '路燈', '騎機車', '騎腳踏車', '騎自行車', '騎單車','方向燈', '學運', '水溝蓋', '舊麵包', '新麵包', '位置',
        '國旅卡', '急剎車', '車', '單車', '移車', '搬車', '挪車', '刮車', '麵包坡', '立中柱', '側翼', '後照鏡', '切出去', '切出來',
        '衝出來', '衝出去', '安全帽', '紅綠燈', '路燈', '對向', '遠光燈', '近光燈', '車燈', '迴轉', '火車票', '美利達', '手續費', '訂到票','訂不到票',
        '車', '停好', '別台車', '亂移', '擦撞', '摔車', '甩尾', '開車', '機車棚', '腳踏車棚', '出事', '停機車', '停汽車', '停自行車',
    ],

    '法規': [
        '誹謗罪', '學術網路', '公約', '告訴乃論', '損害賠償', '責任', '動物保護法', '訴願法', '行政訴訟', '第一', '第二', '第三', '審',
        '條款',  '道交', '條例', '敗訴', '非告訴乃論', '個資法', '行政處分', '上級', '程序法', '條款', '民事起訴狀', '第貳章',
        '新臺幣', '道路交通安全', '規則', '板規', '附註', '條例', '主管機關', '罰鍰', '統一編號', '護照號碼', '身分證', '第肆章', '準則',
        '身分證字號', '非公眾人物', '公眾人物', '政治人物', '公共場所', '求償', '被害妄想症', '反社會人格', '駕駛人', '連署', '開庭',
        '具狀人', '第一條', '第二條', '第三條', '第四條', '第五條', '第六條', '第七條', '第八條', '第九條', '個人資料', '防治', '陳情',
        '買賣', '契約', '十八歲', '強制罪', '就學貸款', '酒駕', '陳請', '搶錢', '社會住宅', '住宅法', '實價登錄', '房地合一','稅租賃專法',
    ],

    '網路/APP': [
        '交友', '程式', '狄卡', '迪卡', '軟體', '維基百科', '貼文', '靠北東華', '塗鴉牆', '靠北慈大', '專頁', '頁面', '靠北學校', '正妹',
        '醜女', '帥哥', '醜男', '匿名交友', '下圖', '謾罵', '下限', '頁面', '互助東華', '烘焙王', '梗圖', '留言', '愛心', '私訊',
        '約跑東華', '西斯東華', '通訊', '軟體', '車友互助平台', '批踢踢', '黑特板', '發文者', '簽名檔', '黑特文', '投稿系統', '約砲',
        '板主', '著作權', '註明', '出處', '板規', '未盡', '網站', '注音文', '火星文', '底下', '留言', '約炮', '推課東華', '東華學苑',
        '課金', '本尊', '異次元', '遊戲序號', '一組', '序號', '自婊文', '打炮', '嗆聲', '權利遊戲', '大招', '九陽神功', '九陰白骨爪',
        '詠唱', '虐殺', '癱坐', '背刺', '踢出', '野放東華', '西施東華', '鬥陣', '釣魚', '跑跑卡丁車', '低能卡', '非黑特文', '求春趴', 
        '引戰', '靠北平台', '幽閉恐懼症', '精神衰落', '鬥陣特攻', '雷姆', '蘿莉控', '傳說', '傳說對決', '網路', '迦娜', '標註',
        '澄清文', '感謝文', '匿名文', '道歉文', '黑特文', '表特東華', '粉絲頁', '底下留言', '密語東華', '台版', '假帳號', '硬碟',
        '隨身碟', '英雄聯盟', '斷網', '斷線', '威廉斯氏症', '買書', '賣書', '就飽了', '砲火', '地圖砲', '縮網址', '舊頁面', '新頁面',
        '本頁面', '爆卦', '女用機', '懂的人', '賣東西', '發文', '刪文', '電競賽', '比賽', '寄信', '公告信', '校版', '吃起來', '喝起來',
        '約起來', '好好說', '蝦皮', '幹你媽', '靠爸族',
    ],

    '費用': [
        '學雜費', '學生會費', '註冊費', '住宿費', '系學會費', '服務費', '清潔維護費', '生活費', '停車費', '處理費', '公基金', '保證金',
        '叫車費', 
        
    ],

    '性別/感情': [
        '男男', '同性戀', '異性戀', '性平', '環境', '小三', '女朋友', '男朋友', '配偶', '非配偶', '汁男', '懶趴', '慾望',
        '婚姻平權', '溫柔', '賢淑', '甲甲', '寶貝', '小狼狗', '前任', '女權', '自助餐', '處男', '在一起', '妨礙家庭', '冷戰',
        '公主病', '閃瞎', '挺同', '反同', '分手', '和平', '綁架', '渣男', '渣女', '毀謗', '勸世', '挑撥', '近距離', '遠距離', 
        '接納', '軟趴趴', '不舉', '伸狼爪', '猥褻', '跳蛋', '想你', '愛你', '叫春', '第三者', '工具人', '打砲', '嘿咻',
        '綠帽子', '希望你', '希望妳', '祝你', '祝妳', '當朋友', '臭婊子', '騙砲',
    ],


    '居家生活': [
        '四層櫃', '三層櫃', '兩層櫃', '雙層櫃', '保險套', '驗孕棒', '全家禮物卡', '小米', '耳機', '傘骨', '掃把', '快煮鍋', '禮卷', '淘寶',
        '吹風機', '罵來罵去', '小聲', '手環', '檯燈', '涼被', '除濕機', '偷聽', '隔壁間', '不包電', '包電', '包水', '不包水', '耳聾', 
        '紗窗', '塑膠袋', '高分貝', '壓低', '音量', '刮鬍泡', '生活習慣', '新宿舍', '舊宿舍', '換宿舍', '蜜袋鼯', '繫鈴鐺', '夜行性動物',
        '鉛筆盒', '帆布', '牛皮', '拉鍊', '正中間', '小聲', '搬宿舍', '行李', '托運', '吵死人', '偷東西', '搬行李', '換宿舍', '徵室友',
        '洗衣服', '烘乾', '烘衣服', '社會化', '大剌剌', '菸蒂', '缺室友',  '回宿舍', '收衣服', '買東西', '不是說', '拿會來', '放回來',
        '賠錢', '偷錢', '垃圾桶', '臭味', '煙味', '菸味', '洗髮精', '外頭', '吵鬧', '二手菸', '偷車賊', '就該', '被黑',
    ],

    '衛生': [
        '鞋', '臭', '襪子', '洗衣蓋', '襪', '洗衣籃', '丟進去', '小強', '狗窩',
    ],

    '其他': [
        '沒人', '沒有人', '有沒有人', '來啦', '來囉', '國罵', '都要', '等你', '黨中央', 
        '跑出來', '印象中', '實在', '讓人', '心酸', '沒戴口罩', '復仇', '吵鬧', '上位者',
        '一個人', '二個人', '兩個人', '三個人', '四個人', '五個人', '六個人', '七個人', '八個人', '九個人', '十個人', '築夢', '對談', '記者會',
        '一句話', '一群人', '一回事', '一開始', '土著化', '內地化', '社會化', '學分', '心動', '軟實力', '硬實力', '聆聽', '大學城', '身心靈',
        '每一個', '每一間', '共同體', '連手', '提告', '佔領', '華爾街', '運動', '以來', '註定', '二戰', '撤軍', '驅逐', '出境', '萬一',
        '請妳', '請你', '請我', '請他', '請她', '往後', '勸導', '遷徙', '放映所', '人權', '廟埕', '影展', '紀錄片', '上學', '生活', '保證人',
        '社會', '學習', '教育', '意義', '過濾', '外面', '鑑於', '屆時', '各位', '個人', '更新', '完全', '還沒', '找齊', '任何', '普拉蘇', 
        '備份', '網路', '大家', '任何', '囧境', '澄清', '有關', '儘快', '釐清', '根本', '處於', '被動', '無需', '薪資', '所得', '其中', 
        '發佈', '才是', '儘快', '置頂', '兼課', '辭去', '絕不', '在此', '也要', '粗口', '事後', '有關', '責任感', '都是', '教訓', '好想', 
        '高達', '罵爆', '請問', '全體', '調查', '不戴口罩', '遺留', '儘速', '返還', '過後',  '撥打', '有時候', '你們', '真的', '走過', '啞鈴', 
        '重點', '哈菸', '拿起來', '有什麼', '住在', '自私', '對吧', '大多數', '為了', '沒理由', '沒洗過', '本來', '情緒性', '再多',
        '真的', '失敗', '已經', '拜託', '哪個', '不要', '戰校', '同一掛', '笑話', '幹話', '這些', '已經', '是不是', '就是', '大獎', '這種人', 
        '神邏輯', '哈囉', '結束', '兇三小', '說話', '誰知道', '他媽的', '妳們', '成癮', '本來', '就是', '不要', '再來', '然後', '一般', 
        '明知道', '滿嘴', '令人', '浮雲', '我們', '學校', '真的', '喝完', '超噁', '表定', '名額', '篩選',  '感謝', '躲貓貓', '蹤影', '記憶力', 
        '貼心', '透氣',  '打從', '砲聲', '膚淺', '感覺', '佔位子', '試一下', '切線', '後台', '打不好', '出列', '誤傳', '小酌', '無妨', '到底', 
        '為什麼', '我覺得', '好笑', '才要', '就會', '每天', '不停地', '飽嗝', '還是', '冷風', '單字', '真的', '遲早', '把拔', '馬麻', 
        '零用錢', '貢獻', '我們', '第一類', '水災', '存在', '意義', '住處', '年齡', '來自', '彷彿', '當我', '思鄉', '感覺', '頒獎人', '從未',
        '肉食動物', '有點少', 
        
        '特別多', '對了', '沒什麼', '或者', '低於', '大家好', '又來了', '安裝', '自主式', '發報器', '都可以', '複習',
        '歐趴糖', '就能', '得獎', '品項', '二手', '後果', '不捨', '愛情', '劇本', '國旗', '我們', '學校', '長大', '就讀', '傳播', '成立', 
        '跳脫', '舒適圈', '請問', '出面', '手工藝',  '以上', '到底', '是誰', '下課', '鬼叫', '上課',  '枉顧', '意願', '殺小', '躺著', '啥時', 
        '官腔', '壓下去', '外租', '場域', '防治', '事件',  '拒選', '惡夢', '亂丟',  '叫來叫去', '髒話',  '年頭', '鬆掉', '活躍',  '洗手乳', 
        '所有人', '守著', '走廊', '朋友', '經典', '不見', '真的', '只是', '想要', '硬舉', '亂吼亂叫', '水溝', '污染', '東西', '靠近', '自己', 
        '你媽', '菸蟲', '陽痿',  '煙鬼', '過分', '一首', '每天',  '還可以', '真的', '破掉', '水瓶', '滿地', '還給我', '左右', '偷車', '馬的', 
        '狗', '衝到', '嚇死', '社會化', '到處', '不見', '球網', '到現在', '大亂鬥', '羊', '偉哉', '名聲', '事蹟', '塊逃', '這是', '拜託', 
        '不要', '無處可說', '貼近', '暫行', '爭議文', '不當', '字數', '狀聲詞', '大東華', '行情價', '還有', '什麼', '礙於', '砲轟', '而不是', 
        '完畢', '家樂福', '或者', '重要', '張貼', '指證', '攻擊性', '防護措施', '父母', '子女', '複雜', '官腔', '夢遺', '主動式', '試用', 
        '感謝狀', '升學', '以後', '身心障礙', '選擇題', '看錯', '請求', '複製本', '罷工', '印製', '自製', '催眠術', '快去', '校版', '汙水處理場', 
        '基於', '罵人', '一樓', '這個', '現象', '希望', '此處', '認為', '通知單', '電子信箱', '視為', '隔年', '邁入',  '修復', '吸菸', '志學所', 
        '禁菸', '影響', '菸蟲', '鬼樣', '直接', '師生戀', '找人', '做不到', '籌備期', '你們', '大家', '裡面', '還要', '太少', '觀光', '槓片', '夾到手',
        '併排', '打給後', '小魯', '本魯', '只是', '開抽', '別難過', '言詞', '骯髒', '價值觀', '殭屍', '休學', '戶外', '商討', '候補', '和室', 
        '同寢', '鼻樑', '噁爛', '衛生習慣', '想哭', '嗚嗚', '同一層', '兩個人', '好處', '好了', '解開', '心中', '這學期', '閩南語', '情緒化', 
        '感受', '腔調', '南島語系', '土地', '退錢', '一點點', '虛偽', '踐踏', '言論',  '每個人', '才不會', '是吧', '好吧', '臉上', '翻臉', '在線', 
        '追殺', '都有', '五個月', '那篇',  '送你', '不差', '草泥馬', '同上', '根本', '沒人', '文字', '記錄', '想說', '組員', '想看', '看起來',
        '長進', '值得', '等待', '不錯吃', '大小聲', '經營方式', '上一篇', '說出來', '自己人',  '太大', '安寧', '一般垃圾', '都說', '就好', '後來',
        '紙類', '表達能力', '欽佩', '但是', '東西南北', '說詞', '說真的', '怎麼想', '送你', '肉搜', '有問題', '拿來', '對啦', '怎麼會', '和平', 
        '公道話', '罪惡感',  '單獨', '失敗率', '該不該', '短暫', '又不是',  '成發', '母親節', '水母腦', '水果', '好嘛', '你自己',  '果蠅', '這條路',
        '了吧', '不夠慘', '哇靠', '看不出來', '導生聚', '追隨', '前輩', '白目', '拼盤', '誰的', '約莫', '雷射筆', '本日', '只因', '砲灰', '維修部',
        '洗衣間', '教科書', '甚至於', '生命故事', '撥冗', '樂趣', '第一人', '好啊', '角錐', '或是', '出去', '同理心', '那裏', '是嗎', '開打', '也是',
        '即使', '開玩笑', '前陣子', '五月底', '留學', '學子', '口中', '沒人權', '不多說', '不想', '哪時候', '不想說', '酷炫', '還沒', 
        '環頸雉', '沒問題', '死黨', '媽寶', '要求', '合租',  '碎碎唸', '氣質', '不要', '再見', '害我', '過年', '紅包', '除了', '下意識', 
        '樂於分享', '好朋友', '裝可憐', '是說', '很好', '都會', '只要', '不為過', '沒人', '不在', '他說', '造成', '的確', '責怪', '繼續', '短髮',
        '心裏', '總是', '沒多久', '要好', '一起', '過夜', '不會', '好像', '老實說', '校狗', '過路人', '路上', '粉絲', '不對', 
        '對不對', '出頭鳥', '開砲', '一般人', '別傻了', '影響', '要不要', '生活', '慢慢', '沒說', '到了', '那時候', '於是', '碎唸', 
        '一臉凶狠', '幾個月', '感到不齒', '險惡', '我', '自己', '隔壁', '演員', '好啦', '餿主意', '看在', '來日', '之後', '誤認', '路人', '另外', 
        '一個', '停下腳步', '巨大', '聲響', '卡到陰', '個性', '蠻好', '搭話', '尷尬癌', '發作', '在於', '沒交集', '說法', '事實上', '非得', 
        '吃相', '保祐',  '付出', '一切', '每個系',  '當場', '那時侯', '捨棄', '出國', '過期', '瓦斯桶', '落單', '來電', '粗口', '有病', '逼死誰', 
        '港澳會', '女仔', '校板', '想不透', '想過', '嘴臉', '還會', '男廁', '女廁', '大號間', '偷窺', '核心宗旨', '只能說', '不太合理', '非系隊', 
        '美德', '有些人', '升級', '完了', '外包', '新的', '機掰', '不練球', '先發', '怪誰', '檢討', '落落長', '沒重點', '還好', '同溫層', '二手拍', 
        '保險金', '好幾週', '隔壁場', '排球場', '鋁箔包', '紙容器', '聚合膜', '回收', '成本', '燒掉', '塑膠瓶', '再製', '埋起來', '大型垃圾', '大嬸', 
        '也行', '稱為', '別忘了',  '內心', '遠距離', '第一個', '三小時', '不要吵', '四腳獸', '小七', '新生入學', '火車站', '車站', '資訊中心', 
        '道歉函', '沖天炮', '看完', '長方形', '也有', '直接', '公眾', '好窩', '二手社團', '把妹', '很吵', '有夠吵', '聽得到', '耳機', 
        '不戴耳機', '戴耳機', '被迫', '下來', '失敗論', '結果論', '影響力', '諸如', '退學', '勸勸', '健檢', '對面', '透透氣', '諮商',
        '好聲好氣', '打開', '近一點', '不讀書', '行嗎', '說好', '有一點', '誰來', '洗留言', '傢伙', '等等', '敢做', '不要怕', '有糖吃', '不敢靠近', 
        '還不如',  '最前面', '心態', '說不定', '只希望', '存在感', '復原', '言論', '得第一', '不只', '就像', '輪不到', '仗著', '嘴砲', '聽不懂', 
        '沒常識', '度假中心', '网咖',  '别用', '你他妈', '這麼大', '沒爛掉', '爛掉', '回去', '抽籤', '求標記', '花點錢', '幹你老師', '沒時間', 
        '有點多', '不唬爛', '傢具', '報應', '勾勾纏', '狗黨', '長相', '取消', '不回家', '找房子',  '很好聽', '雞八', '來了', '下一個', '沒有意見', 
        '還有', '踩雷', '超多', '大蟑螂', '熱水器', '水上樂園', '沒下文', '看房子', '心得', '限女性', '是什麼', '不說', '晚一點', '行李', '還沒', 
        '忘了', '說改就改', '抽宿舍', '脾氣', '活在',  '別人家',  '不是說',  '任何事', '聞到', '紙膠帶', '小錢', '忘了', '密你', '飯盒', '臺版', 
        '運動相機', '防水殼', '全景', '鏡頭', '電池', '藍綠', '通吃 ',  '報名', '網址', '簡稱', '椅子', '評審',  '請多指教', '過頭', '靠腰', '出資', 
        '強逼', '教學', '心跳不已',   '解決', '問題', '越來越多', '尖峰', '時段', '離峰', '越來越好', '同學', '開放', '留言', '吃重', '還以為',
        '時後', '怎麼', '回事', '再度', '出現', '後果', '自負', '反對票', '同意票', '票倉', '心裡', '往上', '大一', '投資報酬率', '更多', 
        '路權', '長官', '旁觀者', '旁聽', '學長學弟制', '第三人', '罔顧', '客觀', '主觀', '政績', '戀愛', '加入', '厲害', '根本', '亂搞', '撿球', 
        '換我', '重要', '憂鬱', '關我屁事', '月經', '講不聽', '自嗨', '借錢', '男女比', '哭夭', '嘲諷', '自行', '雙胞胎', '兄弟', '姐妹','處女座',
        '打輸', '挑釁', '體型', '不敢', '共勉之', '夥伴', '閉嘴', '醉了', '好正', '鬍子', '雨好大', '濃醇香', '電燈泡', '講義', '二審', '妖嬈',
        '亂跑', '黃豆', '嚇醒', '犯賤', '又是', '搭訕', '才華', '追蹤器', '復活', '尬車', '够了', '中国人', '搭船', '上學', '蟹堡', '残体字', 
        '宗侖餐', '一起衝', '無線網絡', '力抗', '手機殼', '多少錢', '複製', '檳友', '項鍊', '啥米碗糕', '差勁', '一起玩', '端午節', '長頸鹿',
        '新古典主義', '秀下限', '刷下限', '公開場合', '上進', '光復', '主辦', '興起', '合併', '被吉', '關起來', '身心科', '某天', '下雨', '很乖', 
        '據說', '二選一', '三選一', '多一點', '活著', '系統忙碌中', '歸屬感', '慶祝', '破紀錄', '稱讚', '質感', '衝三小', '睜大', '亞軍', '鬨笑',
        '對外', '說出', '小黑蚊', '總和', '揮拳', '用詞', '書卷獎', '行車記錄器', '看書', '愛惜', '壞習慣', '二手物', '灰塵', '好一點', '均分', 
        '傢俱', '延長線', '蹲廁', '隔壁棟', '電錶', '隔壁房', '馬桶蓋', '塑膠杯', '維修單', '沒辦法', '回去', '名義', '宣傳車', '宿舍區', '有多少',
        '獻給', '經血', '第四台', '沒錢', '黃垢', '歸零', '自來水', '清冰箱', '熱水壺', '一副', '尖叫聲', '重聽', '不耐煩', '消費者','耳機', 
        '悅耳', '活下來', '上廁所', '按掉', '到時候', '銀髮', '低吼', '製造機', '豬肉', '停靠處', '電視劇', '哭腰', '惡臭', '想念書', '取消', '打麻將', 
        '筊杯', '抖腳', '踹共', '畢業歌', '幾十年', '瑪德', '製仗', '住戶們', '二手煙', '止癢', '達人', '擇優', '看電影', '觸控板', '去死', '小動作', 
        '買晚餐', '買宵夜', '關鍵詞', '冷氣機', '後腦勺', '雞掰', '樓上', '樓下', '操你媽', '儘管', '笑聲', '對話', '碎碎念', '調查表', '粗魯', '杯子', 
        '準確率', '不太懂', '不懂', '沒實力', '馬戲團', '厚臉皮', '遣返', '單挑', '干我屁事', '翹課', '代簽', '模擬考', '待在', '走廊', '的','沒用',
        '少在那邊', '說話', '幹話', '之前', '之後', '早點睡', '選擇', '新選擇', '跑來', '好天氣', '無法接受', '不能接受', '很忙', '一貫',
        '全台灣', '沒朋友', '留下來', '再教育', '還沒', '幫幫忙', '沒了', '沒穿', '就知道', '幫幫忙', '最重要', '重要', '看板', '豪棒棒', '種植',
        '有請', '金湯匙', '嚇死誰', '靠么', '詐欺', '但是', '不要', '路中央', '沒人', '教你', '走路', '靠邊', '滾出來', '搞甚麼', '隔壁', '該死',
        '跑流程', '倒垃圾', '倒廚餘', '清冰箱', '大航海時代', ' 決定權', '這張', '改造營', '更大', '廣東話', '大砲', '回收場', '挖寶', '心態',
        '這回事', '那回事', '一定是', '取回', '米克斯', '申請書', '開冷氣', '好蚌蚌', '頭上', '肉墊', '遠一些', '摔下來',
        
    ]
}



deps = ['諮臨系', '中文系', '臺文系', '台文系', '經濟系', '公行系', '華文系', '英美系', '歷史系', '社會系', '法律系', '應數系', '生科系',
        '光電系', '材料系', '物理系', '化學系', '電機系', '資工系', '企管系', '國企系', '資訊系', '觀遊系', '會計系', '財金系', '管科系',
        '教育系', '課程系', '特教系', '教行系', '體育系', '幼教系', '音樂系', '藝創系', '藝設系', '族文系', '民發系', '民傳系', '民社系',
        '民樂系', '自資系']


stop_words = [
    
    '00', '01', '02', '03', '04', '05', '06', '07', '08', '09', 
    '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
    '20', '21', '22', '23', '24', '30', 
    'ar', 'er', 'and', 'you', 'ing', 'if', 'AR', 'ER', 'AND', 'ING', 'IN', 'LE',

    '我', '的', '年', '月', '日', '半', '字', '常', '吧', '將', '有', '之', '仍', '一', '阿', '是', '了', '較', '就', '看', '很', '啊', 
    '你', '的', '都', '啦', '欸', '人', '又', '嗎', '內', '他', '她', '想', '及', '位', '會', '邊', '在', '要', '喔', '請', '去', '跟', 
    '也', '妳', '來', '被', '到', '與', '呢', '把', '您', '上', '和', '讓', '完', '好', '是', '求', '哦', '但', '這', '囉', '不', '拿',
    '打', '沒', '用', '或', '話', '誰', '找', '說', '再', '能', '那', '對', '它', '多', '長', '走', '等', '們', '唷', '還', '後', '照'
    '開', '已', '為', '小', '前', '於', '可', '中', '而', '時', '著', '卻', '該', '搞', '某', '加', '進', '從', '做', '才', '個', '連',
    '女', '男', '耶', '馬', '便', '當', '鳥', '得', '原', '陳', '第', '往', '者', '早', '嗨', '各', '帶', '三', '雖', '仔', '太', '更',
    '真', '勒', '大', '還', '兩', '接', '最', '呀', '喲', '呦', '給', '此', '九', '外', '口', '是', '黃', '試', '成', '據', '故', '文',
    '牠', '寫', '美', '期', '猜', '掉', '問', '超', '過', '林', '正', '發', '忙', '差', '化', '只', '快', '擠', '水', '以', '過', '下',
    '聽', '放', '點', '跑', '凡', '總', '學', '週', '啥', '補', '六', '四', '攤', '久', '剛', '下', '朝', '抽', '樣', '越', '公', '生',
    '群', '土', '少', '回', '像', '收', '快', '寄', '二', '鋪', '改', '嘛', '別', '需', '系', '版', '間', '約', '詞', '杯', '摳', '冷',
    '哪', '組', '事', '唸', '幫', '臺', '社', '算', '同', '耍', '國', '行', '遠', '選', '台', '趙', '低', '比', '佳', '立', '敢', '讀',
    '惹', '吹', '冰', '弄', '方', '店', '自', '包', '管', '先', '排', '開', 
     
    
    '什麼', '或是', '就是', '而已', '但是', '是誰', '這樣', '如果', '時候', '然後', '我要', '點在', '其他', '那個', '人要', '人有', '哪個',
    '自己', '他們', '我們', '你們', '妳們', '現在', '真的', '剛剛', '一個', '有個', '因為', '可是', '兩個', '還有', '三樓', '有位', '昨天',
    '這個', '一半', '所以', '知道', '已經', '了還', '這麼', '那麼', '這種', '一起', '只是', '一下', '最近', '還是', '一邊', '想問', '請問',
    '一點', '有夠', '哪位', '非常', '剛好', '不然', '下次', '別人', '這些', '也是', '其實', '有點', '了吧', '非常', '是否', '好了', '那些',
    '為了', '而且', '意思', '令人', '相當', '事情', '亦可', '人來', '一一', '給我', '一家', '一碗', '我會', '一名', '一篇', '可能', '也要',
    '由於', '小編', '在此', '你是', '妳是', '總之', '好像', '反正', '一定', '那種', '本來', '怎麼', '兩天', '不管', '怎樣', '甚麼', '一樣',
    '可以', '明天', '今天', '昨天', '後天', '前天', '之前', '之後', '就會', '只好', '各位', '你能', '這位', '記得', '他人', '麻煩', '讓我', 
    '那邊', '幹嘛', '沒有', '對方', '他人', '問題', '這句', '不同', '都是', '認為', '等等', '不行', '怎麼', '怎麼', '人家', '以前', '這屆', 
    '是吧', '那種', '還會', '也沒', '只有', '發現', '表示', '當時', '大約', '應該', '也沒', '底下', '留言', '直接', '拜託', '看到', '想說',
    '根本', '甚至', '大家', '就算', '需要', '模擬', '開放', '這次', '到處', '開始', '直接', '看到', '那條', '左右', '兩位', '不是', '覺得',
    '還能', '不會', '一堆', '只會', '幾個', '好嗎', '打開', '還把', '使用', '一些', '想要', '感到', '也有', '更多', '平台', '各種', '不看',
    '好嗎', '還要', '還好', '原來', '不能', '問個', '突然', '根本', '尤其', '連續', '終於', '想必', '當年', '一人', '過去', '這是', '哪裡',
    '不要', '小弟', '小妹', '來啦', '改為', '謝謝', '只能', '還沒', '哪裡', '得知', '這是', '一間', '一種', '還想', '回復', '匿名', '想想',
    '好看', '而是', '才會', '新聞', '孩子', '這裡', '還沒', '真是', '一聲', '一看', '要用', '一次', '都沒', '東華', '一句', '就好', '不了',
    '他說', '最後', '彼此', '大概', '一張', '一位', '一杯', '同學', '學校', '既然', '當初', '再來', '有些', '順利', '是說', '有人', '這門',
    '上去', '不過', '合理', '心中', '或許', '哪來', '那位', '兩三', '你當', '旁邊', '不好', '後續', '三次', '今年', '去年', '一支', '安安',
    '那裡', '半年', '很多', '個月', '還請', '對於', '如何', '並且', '比較', '進到', '繼續', '才是', '一樓', '二樓', '三樓', '四樓', '小小',
    '裡的', '吃過', '哪家', '我點', '各自', '討論', '比起', '行為', '而言', '相關', '提供', '個人', '不可', '感恩', '一本', '設立', '願意',
    '猴子', '大學', '系上', '看來', '幾乎', '都有', '就要', '起來', '也許', '說個', '給他', '例如', '當個', '爸媽', '以為', '認真', '呼籲',
    '竟然', '結果', '快要', '原本', '國立', '前面', '哈囉', '經過', '或者', '一天', '特別', '看看', '那樣', '那篇', '一件', '還蠻', '小時',
    '九點', '位子', '到底', '請你', '好好', '一台', '活動', '登記', '友善', '原po', 
    '另外', '像是', '不知', '人們', '某位', '好幾', '一提', '早上', '中午', '下午', '晚上', '私訊', '抱歉', '學生', '時間', '點多', '出來',
    '大前天', '大後天', '是什麼', '想請問', '或其他', '有時候', '一個月', '有沒有', '這回事', '那回事', '的樣子', '是不是', '要不要', '怎麼樣',
    '我相信', '怎麼會', '我覺得', '會不會', '什麼事', '之類的', '留個言', '想知道', '一群人', '就算了', '點多在', '能不能', '為什麼', '讓我們',
    '小弟我', '小妹我', '不知道', '學弟妹', '要怎麼', '學長姐', '跟我說', '不管你', '在這裡', '同學們', '都不用', '是一種', '有什麼', '全部都',
    '明明就', '還以為', '大家好', '怎麼辦', '在這邊', '第一次', '而且還',
    '想問一下', '黑特東華', '東華大學', '不好意思', '下面留言',
   
]
stop_words = list(set(stop_words))
