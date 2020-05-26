import numpy as np
import pandas as pd
from flask import Flask, render_template, request
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def create_sim():
    data = pd.read_csv('data.csv')
    # creating a count matrix
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(data['comb'])
    # creating a similarity score matrix
    sim = cosine_similarity(count_matrix)
    return data,sim


def top_recommendation( movie , n):
    
    try:
        data.head()
        sim.shape
    except:
        data, sim = create_sim()

    mov_data = pd.read_csv('movie.csv')
    mov_data['movie_title1'] = mov_data['movie_title'].str.lower().apply( lambda s  : s[:-1])
    
    movie = movie.lower()

    if movie in mov_data['movie_title1'].unique():
        indx = mov_data.query('movie_title1 == @movie').index[0]
        sim_list = [ (k,v) for k,v in list(enumerate( sim[indx , : ] ) ) if k!= indx ]
        sim_list = sorted( sim_list , key = lambda x : x[1] , reverse = True )
        sim_list = [ k for k,v in sim_list[ : n ] ] 
        return  mov_data.loc[ sim_list , 'movie_title' ].values.tolist() , n
    else:
        return 'The movie is not available in the database or please check for the spelling..' , n

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')

@app.route("/recommend")
def recommend():
    movie = request.args.get('movie')
    n = request.args.get('k_rec')
    n = int(n)
    print( movie , n )
    print(type(n))
    r , n = top_recommendation( movie = movie , n = n )
    movie = movie.upper()
    if type(r)==type('string'):
        return render_template('result.html',movie=movie,r=r,t='s' )
    else:
        return render_template('result.html',movie=movie,r=r,t='l' , n = n )
        
if __name__ == '__main__':
    app.run(debug = True)
