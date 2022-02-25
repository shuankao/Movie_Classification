# NLP-project

分析八部電影劇本，四種類型，分別為浪漫愛情、科幻、恐怖、動作
電影類別：
1. 浪漫愛情：LA LA Land','Before Sunrise'(樂來越愛你，愛在黎明破曉時)
2. 科幻：'The Matrix','Avatar'(駭客任務，阿凡達)
3. 恐怖：'Insidious','It'(陰兒房，牠)
4. 動作：'Mission Impossible 2','The Bourne Identity'(不可能的任務2，神鬼認證)

分析步驟：
1.資料前處理
  (1)劇本存檔為「電影名稱.txt」
  (2)用dict型態儲存電影名稱與對應之劇本
  (3)將分成多段list之劇本合併成一個string
  (4)用pandas中的dataframe產生一張表格，以dict之key(電影名稱)作為列，value(劇本)所在之行欄位命名為'script'
  (5)將標點符號等去除使版面變乾淨
2.分析各電影最常出現哪些字詞，比較差異
  (1)為了計算每個詞語出現次數，用CountVectorizer建立以單詞為行、電影名稱為列之二維矩陣，矩陣中存每個單詞在各電影中出現次數
  (2)過濾掉英語中幾乎不具意義的詞語(stop words)
  (3)用dict的sort_values找出每部電影出現頻率前30名之字詞
  (4)比較每部電影出現頻率前30名之間有無重疊，重疊者多為口語中無意義的詞語，例如：like,look,etc.
  (5)過濾多部電影都出現之共同詞語
  (6)此時，頻率高之詞語多為人名，因此手動過濾電影人名
  (7)用WordCloud產生圖像(結果請詳見topwords_wordcloud.png)
3.Sentiment Analysis
  (1)用textblob計算每部電影的主觀度、正負面程度
  (2)用matplotlib產生以主觀性為縱軸、正負面程度為橫軸之散布圖，呈現各電影劇本的情緒氛圍(結果請詳見sentiment_analysis.png)

conclusion:
1. Top Words Calculation (using worcloud)
  (1)BeforeSunrise出現think, people, life, really等較主觀之詞語

2. Sentiment Analysis (using scatter plot)
  (1)BeforeSunrise、LA LA Land較其他類型電影正向
  (2)BeforeSunrise主觀度高，與wordcloud中該電影常出現主觀字眼結果一致
