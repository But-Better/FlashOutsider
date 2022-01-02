## Flash on Pi

Da der `build` prozess auf einem anderem System geschehen ist, muss der `flash` Prozess zunächst vorbereitet werden. Diese Vorbereitung beinhaltet einzelne Schritte, welche die Verlinkung zu bestimmten Pfaden abändert, sodass diese sich im Einklang mit dem System vom Pi verhalten. Die gebrauchten Pfade (Verlinkungen), die geändert werden müssen, können sich praktischerweise in einer Datei wiederfinden.

#### CMakeCache.txt

Diese Datei kann man fast als Informationsausgabe vom `build` Prozess bezeichnen. Sie beinhaltet viele verschiedene Informationen, welche unteranderem auch die Umgebung umfasst, in welcher der `build`  Prozess stattfand(generiert wird sie vom Tool: `cmake`). 

Die für uns wichtigsten Informationsteile zum vorbereiten des flash-prozesses sind folgende:

- ```ceylon
  // Application Binary Directory
  APPLICATION_BINARY_DIR:PATH=/home/user/zephyr/samples/basic/fade_led/build
  ```

- ```ceylon
  // Application Source Directory
  APPLICATION_SOURCE_DIR:PATH=/home/user/zephyr/samples/basic/fade_led
  ```

- ```ceylon
  //Path to CMake executable.
  CMAKE_COMMAND:INTERNAL=/usr/bin/cmake
  ```

- ```ceylon
  //Zephyr SDK install directory
  ZEPHYR_SDK_INSTALL_DIR:PATH=/home/user/zephyr-sdk-0.13.2
  ```

- ```ceylon
  //Zephyr base
  ZEPHYR_BASE:PATH=/home/user/zephyrproject/zephyr
  ```

#### Vorgang der Vorbereitung

Um das build-directory für den `flash` vorzubereiten, werden diese Informationsschnipsel in Zusammenarbeit mit dem gegeben Informationen aus der `.env` Datei genutzt, um Teile aus Dateien umzuschreiben.

Um das Umändern der Verlinkungen durchzuführen verwende ich eine kleine Menge an Python-Scripten.

```bash
- env_utils.py
- prepare_flash.py
- rework_build_link.py
- rework_cmake_link.py
- rework_original_path_links.py
- rework_zephyr_base_link.py
- rework_zephyr_toolchain_link.py
```

#### prepare_flash.py

Das um die Vorbereitungen durchzuführen, nutzt das dafür entworfene Python-Script mehrere Scans. 

![prepare_flowchart](/home/note/PycharmProjects/westflashs/preparation_flowchart.png)

Folgende Schritte werden durchlaufen:
