import * as ko from 'knockout';

import "css/style";
import mapViewModel from 'js/mapViewModel';

ko.applyBindings(new mapViewModel("Planet", "Earth"));
