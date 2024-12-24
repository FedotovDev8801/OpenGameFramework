import sys.io.File;

class GameLoader {
    public static function main() {
        var filePath = "game.json";
        if (sys.FileSystem.exists(filePath)) {
            var content = File.getContent(filePath);
            trace("Game data loaded: " + content);
        } else {
            trace("Game file not found.");
        }
    }
}