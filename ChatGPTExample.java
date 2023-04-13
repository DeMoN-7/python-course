import okhttp3.*;
import org.json.*;


public class ChatGPTExample {
  
  public static final MediaType JSON = MediaType.get("application/json; charset=utf-8");
  public static final String OPENAI_API_KEY = "YOUR_API_KEY_HERE";
  
  public static void main(String[] args)throws Exception {
    try {
      String response = getResponseFromGPT("What is the capital of France?");
      String answer = extractAnswerFromResponse(response);
      System.out.println(answer);
    } catch (Exception e) {
      System.out.println("Error: " + e.getMessage());
    }
  }
  
  public static String getResponseFromGPT(String prompt) throws Exception {
    OkHttpClient client = new OkHttpClient();
    RequestBody requestBody = RequestBody.create(JSON, "{\"prompt\": \"" + prompt + "\"}");
    Request request = new Request.Builder()
        .url("https://api.openai.com/v1/engines/davinci-codex/completions")
        .post(requestBody)
        .addHeader("Content-Type", "application/json")
        .addHeader("Authorization", "Bearer " + OPENAI_API_KEY)
        .build();
    Response response = client.newCall(request).execute();
    return response.body().string();
  }
  
  public static String extractAnswerFromResponse(String response) throws JSONException {
    JSONObject jsonObject = new JSONObject(response);
    JSONArray choices = jsonObject.getJSONArray("choices");
    JSONObject answer = choices.getJSONObject(0);
    return answer.getString("text");
  }
}
