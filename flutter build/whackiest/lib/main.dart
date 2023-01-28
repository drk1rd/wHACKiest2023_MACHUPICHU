import 'package:flutter/material.dart';
import 'package:whackiest/subPage.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: MyHomePage(),
      debugShowCheckedModeBanner: false,
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage();

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
          backgroundColor: Colors.green,
          centerTitle: true,
          title: Text(
            "Next Match",
            style: TextStyle(color: Colors.black, fontWeight: FontWeight.bold),
          )),
      body: Container(
        padding: EdgeInsets.symmetric(vertical: 10.0, horizontal: 10.0),
        height: MediaQuery.of(context).size.height,
        color: Color.fromARGB(255, 20, 79, 22),
        child: Column(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Expanded(
                child: Row(
                    crossAxisAlignment: CrossAxisAlignment.stretch,
                    children: [
                      getExpanded('football', 'Football'),
                      getExpanded('basketball', 'Basketball'),
                    ]),
              ),
              Expanded(
                child: Row(
                    crossAxisAlignment: CrossAxisAlignment.stretch,
                    children: [
                      getExpanded('cycling', 'Cycling'),
                      getExpanded('tennis', 'Lawn Tennis'),
                    ]),
              ),
              Expanded(
                child: Row(
                    crossAxisAlignment: CrossAxisAlignment.stretch,
                    children: [
                      getExpanded('golf', 'Golf'),
                      getExpanded('fitness', 'Other'),
                    ]),
              )
            ]),
      ),
      bottomNavigationBar: BottomNavigationBar(
        type: BottomNavigationBarType.fixed,
        items: <BottomNavigationBarItem>[
          getBottomNavigationItem(
            'Home',
            IconData(0xead0,
                fontFamily: 'outline_material_icons',
                fontPackage: 'outline_material_icons'),
          ),
          getBottomNavigationItem(
            'Chat',
            IconData(0xe9ca,
                fontFamily: 'outline_material_icons',
                fontPackage: 'outline_material_icons'),
          ),
          getBottomNavigationItem(
            'Profile',
            IconData(0xe90c,
                fontFamily: 'outline_material_icons',
                fontPackage: 'outline_material_icons'),
          ),
        ],
        currentIndex: 0,
        selectedItemColor: Colors.black,
      ),
    );
  }

  BottomNavigationBarItem getBottomNavigationItem(
      String title, IconData iconName) {
    return BottomNavigationBarItem(
      icon: Icon(
        iconName,
        size: 35.0,
      ),
      label: "$title",
    );
  }

  Expanded getExpanded(String image, String mainText) {
    return Expanded(
      child: TextButton(
        child: Container(
          child: Center(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Image.asset(
                  "images/$image.png",
                  height: 80.0,
                ),
                SizedBox(
                  height: 5.0,
                ),
                Text(
                  mainText,
                  style: TextStyle(
                    fontWeight: FontWeight.bold,
                    fontSize: 20.0,
                  ),
                )
              ],
            ),
          ),
          margin: EdgeInsets.only(top: 10, left: 10, right: 10, bottom: 10),
          decoration: BoxDecoration(
              color: Colors.white,
              borderRadius: BorderRadius.only(
                  bottomLeft: Radius.circular(5),
                  bottomRight: Radius.circular(5),
                  topLeft: Radius.circular(5),
                  topRight: Radius.circular(5)),
              boxShadow: [
                BoxShadow(),
              ]),
        ),
        onPressed: () {
          Navigator.push(context,
              MaterialPageRoute(builder: (context) => SubPage(mainText)));
        },
      ),
    );
  }
}
