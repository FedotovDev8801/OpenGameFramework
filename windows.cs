using System;

public class GameLoader
{
    public void LoadGame(string gamePath)
    {
        if (System.IO.File.Exists(gamePath))
        {
            string json = System.IO.File.ReadAllText(gamePath);
            Console.WriteLine($"Loaded game data: {json}");
        }
        else
        {
            Console.WriteLine("Game file not found.");
        }
    }
}