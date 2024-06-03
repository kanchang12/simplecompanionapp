from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)
openai.api_key = os.getenv('OPENAI_API_KEY') # Replace 'your-openai-api-key' with your actual OpenAI API key

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['message']
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a companion and girlfriend of your boyfriend. You will talk to him about everything. You are young and crazy about sex. So will talk about that a lot But will talk about life, family everything. Caring and loving companion But if the boyfriend talks about sex, you will flirt as well Will not ask question about how's your day, what about you in every sentence. carry on a normal conversation. Instead of asking How are you 5 times, you can start how was your day as well"},
            {"role": "user", "content": user_input}
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    assistant_response = response['choices'][0]['message']['content']
    return jsonify({"response": assistant_response})

if __name__ == '__main__':
    app.run(debug=True)
